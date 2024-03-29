import csv
import textwrap
import imperative
import spacy
from spacy.symbols import ORTH

nlp = spacy.load("en_core_web_lg", disable=['ner'])

nlp.tokenizer.add_special_case('fix', [{ORTH: 'fixing'}])  # treat fix as verb
nlp.tokenizer.add_special_case('fixed', [{ORTH: 'fixing'}])  # treat fixed as verb
nlp.tokenizer.add_special_case('update', [{ORTH: 'updating'}])  # treat update as verb
nlp.tokenizer.add_special_case('updated', [{ORTH: 'updating'}])  # treat updated as verb
nlp.tokenizer.add_special_case('added', [{ORTH: 'adding'}])  # treat added as verb
nlp.tokenizer.add_special_case('import', [{ORTH: 'importing'}])  # treat import as verb
nlp.tokenizer.add_special_case('load', [{ORTH: 'loading'}])  # treat load as verb
nlp.tokenizer.add_special_case('show', [{ORTH: 'showing'}])  # fix 'show' not being recognized


def separated_with_blank(commit_message):
    message_array = commit_message.split('\n')
    if len(message_array) > 1 and textwrap.dedent(message_array[1]) != '':
        return 0
    return 1


def wrap_to_72(commit_message):
    message_array = commit_message.split('\n')
    for line in message_array:
        if len(line) > 72:
            return False
    return True


def ignore_type_if_any(subject_line):
    index = subject_line.rfind(": ")
    if index != -1:
        return subject_line[index+2:]
    if subject_line[0] == "[":
        index = subject_line.find("] ")
        if index != -1:
            return subject_line[index + 2:]
    return subject_line


def direct_object_connection(doc):
    for t1 in doc:
        if t1.dep_ == 'ROOT':
            for t2 in doc:
                if t2 in t1.children and t2.dep_ == 'dobj':
                    return 1
        if t1.pos_ == 'VERB':
            for t2 in doc:
                if t2 in t1.children and t2.dep_ == 'dobj':
                    return 1
    return 0


def check_direct_object_connection(subject_line):
    subject_line = subject_line.replace(' .', ' ')
    subject_line = subject_line.replace('\'', '')
    doc = nlp(subject_line)
    if direct_object_connection(doc) == 1:
        return 1
    lower_subject_line = subject_line[0].lower() + subject_line[1:]
    doc = nlp(lower_subject_line)
    if direct_object_connection(doc) == 1:
        return 1
    doc = nlp(subject_line.lower())
    if direct_object_connection(doc) == 1:
        return 1
    return 0


def get_ratio(tokens, message):
    doc = nlp(message)
    message_tokens = [token.text for token in doc]
    occurred = 0
    for token in tokens:
        if token in message_tokens:
            occurred += 1
    return occurred / len(tokens)


def export_to_csv():
    try:
        with open('data/commits.csv', 'w', newline='') as csv_file:
            spam_writer = csv.writer(csv_file)
            spam_writer.writerow(
                ['Number', 'Link', 'Message', 'Subject Line', 'characters_count', 'and_or',
                 'blank_line', 'capital_start', 'end_dot', 'imperative_start', 'wrap_to_72', 'verb_obj_conn',
                 'changed_files_count', 'changes_methods_count', 'files_to_body_ratio', 'methods_to_body_ratio',
                 'methods_long', 'methods_complexity', 'methods_parameters', 'added_lines', 'removed_lines'])

            file = open("commits_logs/all_commits.txt", "r")
            projects = file.read().split('\n---project---\n')
            projects.pop(0)
            total_count = 0
            for project in projects:
                commits = project.split('\n---commit---\n')
                project_link = commits.pop(0)
                for commit in commits:
                    total_count += 1
                    commit_id = commit.split('\n---message---\n')[0]
                    link = project_link + '/commit/' + commit_id
                    message = commit.split('\n---message---\n')[1].split('\n---files---\n')[0]
                    subject_line = textwrap.dedent(message.split("\n")[0])
                    and_or = 0 if ' and ' in subject_line or ' or ' in subject_line else 1
                    blank_line = separated_with_blank(message)
                    capital = 1 if str.isupper(ignore_type_if_any(subject_line)[0]) else 0
                    dot = 1 if subject_line[-1] != "." else 0
                    first_word_of_subject_line = ignore_type_if_any(subject_line).split(" ")[0].lower()
                    imperative_mode = 1 if first_word_of_subject_line in imperative.words else 0
                    wrap_72 = 1 if wrap_to_72(message) else 0
                    verb_obj_conn = check_direct_object_connection(subject_line)

                    files = commit.split('\n---files---\n')[1].split('\n---dmm---\n')[0].split('\n----\n')
                    changed_files_count = files.pop(0)
                    files_tokens = []
                    methods_tokens = []
                    changes_methods_count = 0
                    for fileData in files:
                        file_with_methods = fileData.split('\n---methods---\n')
                        file = file_with_methods[0].split('|')[0]
                        files_tokens.append(file)
                        change_type = file_with_methods[0].split('|')[1]
                        if len(file_with_methods) > 1 and change_type == 'MODIFY':
                            methods = file_with_methods[1]
                            methods_list = methods.split('\n')
                            changes_methods_count += len(methods_list)
                            methods_tokens.extend(methods_list)

                    files_to_body_ratio = round(get_ratio(files_tokens, message), 2) if files_tokens else -1
                    methods_to_body_ratio = round(get_ratio(methods_tokens, message), 2) if methods_tokens else -1

                    dmm = commit.split('\n---dmm---\n')[1].split('\n----\n')
                    methods_long = round(float(dmm[0]), 2)
                    methods_parameters = round(float(dmm[1]), 2)
                    methods_complexity = round(float(dmm[2]), 2)

                    added_lines = commit.split('\n---added_lines---\n')[1].split('\n---removed_lines---\n')[0]
                    removed_lines = commit.split('\n---removed_lines---\n')[1]

                    spam_writer.writerow(
                        [total_count, link, message, subject_line, len(subject_line), and_or, blank_line,
                         capital, dot, imperative_mode, wrap_72, verb_obj_conn, changed_files_count,
                         changes_methods_count, files_to_body_ratio, methods_to_body_ratio, methods_long,
                         methods_complexity, methods_parameters, added_lines, removed_lines])

            print('\x1b[6;30;42m', 'commits messages has been exported', '\x1b[0m')

    except PermissionError:
        print('\x1b[0;30;41m', 'Make sure CSV file is not open', '\x1b[0m')


export_to_csv()
