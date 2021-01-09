import csv
import textwrap
import imperative
import spacy
from spacy.symbols import ORTH

nlp = spacy.load("en_core_web_lg", disable=['ner'])

file = open("commits_logs/--new.txt", "r")
commits = file.read().split('\n----\n')


def separated_with_blank(commit_message):
    message_array = commit_message.split('\n')
    if len(message_array) > 1 and textwrap.dedent(message_array[1]) != '':
        return 0
    return 1


def wrap(commit_message):
    message_array = commit_message.split('\n')
    for line in message_array:
        if len(line) > 72:
            return False
    return True


def subject_length(subject_line):
    if 20 < len(subject_line) < 51:
        return 2
    elif 10 < len(subject_line) < 21 or 50 < len(subject_line) < 73:
        return 1
    else:
        return 0


def check_direct_obj(subject_line):
    subject_line = subject_line.replace(' .', ' ')
    subject_line = subject_line.replace('\'', '')
    subject_line = subject_line[0].lower() + subject_line[1:]
    nlp.tokenizer.add_special_case('fix', [{ORTH: 'fixing'}])  # treat fix as verb
    doc = nlp(subject_line)
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


def export_to_csv():
    try:
        with open('data/commits.csv', 'w', newline='') as csvfile:
            spam_writer = csv.writer(csvfile)
            spam_writer.writerow(
                ['number', 'Commit', 'Subject Line', 'character count', 'subject_len', 'and_or_count', 'Blank Line',
                 'Capital', 'dot',
                 'imperative', 'wrap', 'verb_direct_obj'])
            for j in range(1, len(commits)):
                subject_line = textwrap.dedent(commits[j].split("\n")[0])

                subject_len = subject_length(subject_line)
                and_or_count = 0 if ' and ' in subject_line or ' or ' in subject_line else 1
                blank_line = separated_with_blank(commits[j])
                capital = 1 if str.isupper(subject_line[0]) else 0
                dot = 1 if subject_line[-1] != "." else 0
                imperative_mode = 1 if subject_line.split(" ")[0].lower() in imperative.words else 0
                wrap_72 = 1 if wrap(commits[j]) else 0
                verb_direct_obj = check_direct_obj(subject_line)

                spam_writer.writerow(
                    [j, commits[j], subject_line, len(subject_line), subject_len, and_or_count, blank_line,
                     capital, dot,
                     imperative_mode, wrap_72, verb_direct_obj])

            print('\x1b[6;30;42m', len(commits), 'commit messages exported', '\x1b[0m')

    except PermissionError:
        print('\x1b[0;30;41m', 'Make sure CSV file is not open', '\x1b[0m')


export_to_csv()
