import quality


# file = open("demo.txt", "r")
# commitMessages = file.read().split("\n")

file = open("log.txt", "r")
commits = file.read().split("\ncommit ")


# tokens = nltk.word_tokenize(commitMessage)
# s_tokens = nltk.sent_tokenize(f.read())
# print(len(commits))

commitMessagesText = commits[1].split("\n")
# print(quality.get_message_text(commitMessagesText))
# print(quality.get_quality(commitMessagesText))


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
    if score in [4, 5]:
        acceptable += 1
    if score < 4:
        bad += 1
print("Commits Quality Average:", "{:.2f}".format(total_score/count), "out of 7")
print("Good quality:", "{:.2f}".format(good * 100 / count), "%")
print("Acceptable quality:", "{:.2f}".format(acceptable * 100 / count), "%")
print("Bad quality:", "{:.2f}".format(bad * 100 / count), "%")
