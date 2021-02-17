from pydriller import RepositoryMining

repos = ["https://github.com/torvalds/subsurface-for-dirk",
         "https://github.com/bitronix/btm",
         "https://github.com/EdwardRaff/JSAT",
         "https://github.com/github/VisualStudio",
         "https://github.com/jtablesaw/tablesaw",
         "https://github.com/barryvdh/laravel-debugbar",
         "https://github.com/terryyin/lizard",
         "https://github.com/torvalds/uemacs",
         "https://github.com/apple/swift-llbuild",
         "https://github.com/docker-library/php"]

with open("commits_logs/--temp.txt", "w") as txt_file:
    for repo in repos:
        i = 0
        commits = RepositoryMining([repo], only_no_merge=True).traverse_commits()
        txt_file.write('\n---project---\n')
        txt_file.write(repo)
        for commit in commits:
            if i < 100:  # only first 100 commit (implemented this way cuz pydriller raises exception otherwise)
                i += 1
                txt_file.write('\n---commit---\n')
                txt_file.write(commit.hash)
                txt_file.write('\n---message---\n')
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



