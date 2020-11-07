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


total = 0
count = 0
for i in range(1, len(commits)):
    commitMessagesText = commits[i].split("\n")
    total += quality.get_quality(commitMessagesText)
    count += 1
print(total/count)
