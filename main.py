import spacy


nlp = spacy.load("en_core_web_lg")

doc13 = nlp("zzzzz")
print([(token.text, token.dep_, token.pos_) for token in doc13])

# file = open("commits_logs/--new.txt", "r")
# commits = file.read().split('\n----\n')[0]
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
