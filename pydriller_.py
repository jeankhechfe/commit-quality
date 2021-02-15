from pydriller import RepositoryMining

repos = ["https://github.com/torvalds/pesconvert",
         "https://github.com/terryyin/lizard"]

with open("commits_logs/--temp.txt", "w") as txt_file:
    for repo in repos:
        i = 0
        commits = RepositoryMining([repo], only_no_merge=True).traverse_commits()
        txt_file.write('\n---project---\n')
        txt_file.write(next(commits).project_name)
        for commit in commits:
            i += 1
            if i <= 30:  # only first 30 commit (implemented this way cuz pydriller raises exception otherwise)
                txt_file.write('\n---commit---\n')
                txt_file.write(commit.msg)
                txt_file.write('\n---files---\n')
                editedFilesCount = str(len(commit.modifications))
                txt_file.write(editedFilesCount)
                for m in commit.modifications:
                    txt_file.write('\n----\n')
                    fileDetails = m.filename + '|' + m.change_type.name
                    txt_file.write(fileDetails)
                    if m.changed_methods:
                        txt_file.write('\n---methods---')
                        for method in m.changed_methods:
                            txt_file.write('\n')
                            txt_file.write(method.name)

                # print(commit.dmm_unit_size, '|', commit.dmm_unit_complexity, '|', commit.dmm_unit_interfacing, '\n')
                # if commit.dmm_unit_size is not None:
                #     txt_file.write('\n---dmm---\n')
                #     dmm = (commit.dmm_unit_size + commit.dmm_unit_complexity + commit.dmm_unit_interfacing) / 3
                #     txt_file.write(str(dmm))



