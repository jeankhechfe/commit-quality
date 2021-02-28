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
        i = -1  # skip first commit
        commits = RepositoryMining(repo, only_no_merge=True).traverse_commits()
        txt_file.write('\n---project---\n')
        txt_file.write(repo)
        for commit in commits:
            i += 1
            if 0 < i < 101:  # only first 100 commit (implemented this way cuz pydriller raises exception otherwise)
                txt_file.write('\n---commit---\n')
                txt_file.write(commit.hash)
                txt_file.write('\n---message---\n')
                txt_file.write(commit.msg)
                txt_file.write('\n---files---\n')
                editedFilesCount = str(len(commit.modifications))
                txt_file.write(editedFilesCount)
                added_lines = 0
                removed_lines = 0
                for m in commit.modifications:
                    txt_file.write('\n----\n')
                    fileDetails = m.filename + '|' + m.change_type.name
                    txt_file.write(fileDetails)
                    added_lines += m.added
                    removed_lines += m.removed
                    if m.changed_methods:
                        txt_file.write('\n---methods---')
                        for method in m.changed_methods:
                            txt_file.write('\n')
                            txt_file.write(method.name.split("::")[-1])
                txt_file.write('\n---dmm---\n')
                methods_long = commit.dmm_unit_size if commit.dmm_unit_size else -1
                txt_file.write(str(methods_long))
                txt_file.write('\n----\n')
                methods_complexity = commit.dmm_unit_complexity if commit.dmm_unit_complexity else -1
                txt_file.write(str(methods_complexity))
                txt_file.write('\n----\n')
                methods_parameters = commit.dmm_unit_interfacing if commit.dmm_unit_interfacing else -1
                txt_file.write(str(methods_parameters))
                txt_file.write('\n----\n')
                txt_file.write('---added_lines---\n')
                txt_file.write(str(added_lines))
                txt_file.write('\n---removed_lines---\n')
                txt_file.write(str(removed_lines))
