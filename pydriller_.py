from pydriller import RepositoryMining


with open("commits_logs/--temp.txt", "w") as txt_file:
    # i = 0
    for commit in RepositoryMining(["https://github.com/torvalds/pesconvert"], only_no_merge=True).traverse_commits():
        txt_file.write(commit.msg)
        # i += 1
        # if i > 1:
        #     break
        editedFilesCount = str(len(commit.modifications))
        txt_file.write('\n--\n')
        txt_file.write(editedFilesCount)
        txt_file.write('\n----\n')
        for m in commit.modifications:
            print(commit.hash, '|', m.filename, '|', m.change_type.name, '|',  m.complexity)
        print(commit.hash, commit.dmm_unit_size, '|', commit.dmm_unit_complexity, '|', commit.dmm_unit_interfacing, '\n')



