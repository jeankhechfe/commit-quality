
file = open("log.txt", "r")

commitMessage = file.read().split("commit ")

print(commitMessage[1])
