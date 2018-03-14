from github import Github
import csv
from collections import defaultdict
from config import GITHUB_USER, GITHUB_PASSWORD
g = Github(GITHUB_USER, GITHUB_PASSWORD)
myDict = defaultdict(dict)
repo = g.get_repo('medialab-ufg/tainacan')


with open('teste.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    for issue in repo.get_issues(state='closed'):
        Id = issue.id
        Title = issue.title
        Body = issue.body
        Created_at = issue.created_at
        Closed_at = issue.closed_at
        Number = issue.number

        if issue.assignee == None:
            Assignee = 'Sem Info'
        else:
            Assignee = issue.assignee.login

        if issue.closed_by != None:
            Closed_by = issue.closed_by.login
        else:
            Closed_by = 'Sem Info'
        writer.writerow([Id, Title, Body, Created_at, Closed_at, Number, Assignee, Closed_by])
        print(issue)
