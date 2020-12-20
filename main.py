import quality
import csv
import textwrap

file = open("commits_logs/libdc-for-dirk-no-merges.txt", "r")
commits = file.read().split("\n")


# convert log file to be separated with double dash (--)
# file = ['None'] * 13657
# j = 1
# for i in range(1, len(commits)):
#     file[j] = commits[i]
#     j += 1
#     if 'Date: ' in commits[i]:
#         file[j] = '--'
#         j -= 1
# with open("commits_logs/--.txt", "w") as txt_file:
#     for line in file:
#         txt_file.write(line + '\n')


def export_to_csv():
    try:
        with open('commits.csv', 'w', newline='') as csvfile:
            spam_writer = csv.writer(csvfile)
            spam_writer.writerow(['number', 'Subject Line', 'Blank Line', 'character count'])
            for j in range(1, len(commits)):
                subject_line = textwrap.dedent(commits[j].split("\n")[4])
                separated_with_blank = 1 if textwrap.dedent(commits[j].split("\n")[5]) == '' else 0

                spam_writer.writerow([j, subject_line, separated_with_blank, len(subject_line)])

    except PermissionError:
        print('\x1b[0;30;41m', 'Make sure CSV file is not open', '\x1b[0m')

export_to_csv()


total_score = 0
count = 0
good = 0
acceptable = 0
bad = 0
for i in range(1, len(commits)):
    commitMessagesText = commits[i].split("\n")
    score = quality.get_quality(commitMessagesText)
    total_score += score
    count += 1
    if score in [6, 7]:
        good += 1
    elif score in [4, 5]:
        acceptable += 1
    else:
        bad += 1

print("Commits Count :", count)
print("Commits Quality Average:", "{:.2f}".format(total_score/count), "out of 7")
print("Good quality:", "{:.2f}".format(good * 100 / count), "%")
print("Acceptable quality:", "{:.2f}".format(acceptable * 100 / count), "%")
print("Bad quality:", "{:.2f}".format(bad * 100 / count), "%")
