# convert log file to be separated with double dash (--)
file = open("commits_logs/libdc-for-dirk-no-merges.txt", "r")
commits = file.read().split("\ncommit ")
file = [''] * 12092  # this depends on the number of lines
j = 0
for i in range(1, len(commits)):
    j += 1
    if 'Date: ' in commits[i]:
        file[j - 2] = '--'
        j -= 2
    else:
        file[j] = commits[i]
with open("commits_logs/--.txt", "w") as txt_file:
    for line in file:
        txt_file.write(line + '\n')

# --------------------------STATISTICS--------------------------
# print("Commits Count :", count)
# print("Commits Quality Average:", "{:.2f}".format(total_score/count), "out of 7")
# print("Good quality:", "{:.2f}".format(good * 100 / count), "%")
# print("Acceptable quality:", "{:.2f}".format(acceptable * 100 / count), "%")
# print("Bad quality:", "{:.2f}".format(bad * 100 / count), "%")
