import csv
import textwrap
import imperative


file = open("commits_logs/--new.txt", "r")
commits_dashed = file.read().split('\n----\n')


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


def export_to_csv():
    try:
        with open('data/commits.csv', 'w', newline='') as csvfile:
            spam_writer = csv.writer(csvfile)
            spam_writer.writerow(
                ['number', 'Commit', 'Subject Line', 'character count', 'subject_len', 'and_or_count', 'Blank Line',
                 'Capital', 'dot',
                 'imperative', 'wrap'])
            for j in range(1, len(commits_dashed)):
                subject_line = textwrap.dedent(commits_dashed[j].split("\n")[0])

                subject_len = subject_length(subject_line)
                and_or_count = 0 if ' and ' in subject_line or ' or ' in subject_line else 1
                blank_line = separated_with_blank(commits_dashed[j])
                capital = 1 if str.isupper(subject_line[0]) else 0
                dot = 1 if subject_line[-1] != "." else 0
                imperative_mode = 1 if subject_line.split(" ")[0].lower() in imperative.words else 0
                wrap_72 = 1 if wrap(commits_dashed[j]) else 0

                spam_writer.writerow(
                    [j, commits_dashed[j], subject_line, len(subject_line), subject_len, and_or_count, blank_line,
                     capital, dot,
                     imperative_mode, wrap_72])

    except PermissionError:
        print('\x1b[0;30;41m', 'Make sure CSV file is not open', '\x1b[0m')


export_to_csv()
