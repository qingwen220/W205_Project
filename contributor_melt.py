import os

folder = 'Repo_contributors'
with open('contributor.txt', 'w+') as f:
    for file in os.listdir(os.path.join(os.getcwd(), folder)):
        with open(os.path.join(os.getcwd(), folder, file), 'r+') as repo_contrib:
            print(repo_contrib)
            data = repo_contrib.read()
            f.write(data)
