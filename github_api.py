import requests


with open("commits_logs/--temp.txt", "w") as txt_file:
    response = requests.get('https://api.github.com/repos/benawad/create-graphql-api/commits')
    print(len(response.json()))
    for res in response.json():
        txt_file.write(res['commit']['message'])
        txt_file.write('\n----\n')
