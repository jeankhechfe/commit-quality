# import quality
import csv
import textwrap
# import requests
import imperative

file = open("commits_logs/--new.txt", "r")
commits = file.read().split("\n----")
print(len(commits))

########################################################
# convert log file to be separated with double dash (--)
# file = [''] * 12092
# j = 0
# for i in range(1, len(commits)):
#     j += 1
#     if 'Date: ' in commits[i]:
#         file[j-2] = '--'
#         j -= 2
#     else:
#         file[j] = commits[i]
# with open("commits_logs/--.txt", "w") as txt_file:
#     for line in file:
#         txt_file.write(line + '\n')

#########################################################
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


def export_to_csv():
    try:
        with open('commits.csv', 'w', newline='') as csvfile:
            spam_writer = csv.writer(csvfile)
            spam_writer.writerow(
                ['number', 'Commit', 'Subject Line', 'character count', 'subject_15_50', 'Blank Line', 'Capital', 'dot',
                 'imperative', 'wrap'])
            for j in range(1, len(commits_dashed)):
                subject_line = textwrap.dedent(commits_dashed[j].split("\n")[0])

                subject_15_50 = 1 if 10 < len(subject_line) < 51 else 0
                blank_line = separated_with_blank(commits_dashed[j])
                capital = 1 if str.isupper(subject_line[0]) else 0
                dot = 1 if subject_line[-1] != "." else 0
                imperative_mode = 1 if subject_line.split(" ")[0].lower() in imperative.words else 0
                wrap_72 = 1 if wrap(commits_dashed[j]) else 0

                spam_writer.writerow(
                    [j, commits_dashed[j], subject_line, len(subject_line), subject_15_50, blank_line, capital, dot,
                     imperative_mode, wrap_72])

    except PermissionError:
        print('\x1b[0;30;41m', 'Make sure CSV file is not open', '\x1b[0m')


export_to_csv()

#########################################################
# total_score = 0
# count = 0
# good = 0
# acceptable = 0
# bad = 0
# for i in range(1, len(commits)):
#     commitMessagesText = commits[i].split("\n")
#     score = quality.get_quality(commitMessagesText)
#     total_score += score
#     count += 1
#     if score in [6, 7]:
#         good += 1
#     elif score in [4, 5]:
#         acceptable += 1
#     else:
#         bad += 1
#
# print("Commits Count :", count)
# print("Commits Quality Average:", "{:.2f}".format(total_score/count), "out of 7")
# print("Good quality:", "{:.2f}".format(good * 100 / count), "%")
# print("Acceptable quality:", "{:.2f}".format(acceptable * 100 / count), "%")
# print("Bad quality:", "{:.2f}".format(bad * 100 / count), "%")


##########################################################
# with open("commits_logs/--temp.txt", "w") as txt_file:
#     response = requests.get('https://api.github.com/repos/benawad/create-graphql-api/commits')
#     print(len(response.json()))
#     for res in response.json():
#         txt_file.write(res['commit']['message'])
#         txt_file.write('\n----\n')
