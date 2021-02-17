# import spacy
# from pydriller import RepositoryMining
# import timeit

# nlp = spacy.load("en_core_web_lg")

# doc = nlp("zzzzz")
# print([(token.text, token.dep_, token.pos_) for token in doc])


# start = timeit.default_timer()
# i = 0
# commits = RepositoryMining("https://github.com/docker-library/php", only_no_merge=True).traverse_commits()
# for commit in commits:
#     if 0 < i <= 100:
#         print([i, commit.hash, commit.msg])
#     i += 1
# stop = timeit.default_timer()
# print('Time: ', stop - start)


# file = open("commits_logs/--temp.txt", "r")
# projects = file.read().split('\n---project---\n')
# projects.pop(0)
# for project in projects:
#     commits = project.split('\n---commit---\n')
#     commits.pop(0)
#     for commit in commits:
#         hash = commit.split('\n---message---\n')[0]
#         msg = commit.split('\n---message---\n')[1].split('\n---files---\n')[0]
#         files = commit.split('\n---files---\n')[1].split('\n---dmm---\n')[0].split('\n----\n')
#         filesCount = files.pop(0)
#         for fileData in files:
#             fileWithMethods = fileData.split('\n---methods---\n')
#             file = fileWithMethods[0].split('|')[0]
#             changeType = fileWithMethods[0].split('|')[1]
#             if len(fileWithMethods) > 1:
#                 methods = fileWithMethods[1]
#                 methodList = methods.split('\n')
#         dmm = commit.split('\n---dmm---\n')[1].split('\n----\n')
#         methods_long = dmm[0]
#         methods_parameters = dmm[1]
#         methods_complexity = dmm[2]



# doc = nlp(commits)
# doc_text, doc_sent = [d.text for d in doc], [d.sent for d in doc]





# print([sent.root for sent in doc.sents])

# print(spacy.explain('ADJ'))
# print(doc1.similarity(doc3))


# --------------------------STATISTICS--------------------------
# print("Commits Count :", count)
# print("Commits Quality Average:", "{:.2f}".format(total_score/count), "out of 7")
# print("Good quality:", "{:.2f}".format(good * 100 / count), "%")
# print("Acceptable quality:", "{:.2f}".format(acceptable * 100 / count), "%")
# print("Bad quality:", "{:.2f}".format(bad * 100 / count), "%")
