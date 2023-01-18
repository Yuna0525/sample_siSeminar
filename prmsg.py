# def post(message: str):
#     """Post message to PR"""
#     token = os.getenv("GITHUB_TOKEN")
#     repo_name = os.getenv("GITHUB_REPOSITORY")
#     with open(os.getenv("GITHUB_EVENT_PATH"), "r") as f:
#         github_event = json.load(f)
#     pr_number = github_event["number"]

#     gh = Github(token)
#     repo = gh.get_repo(repo_name)
#     pr = repo.get_pull(pr_number)
#     pr.create_issue_comment(body=message)
    
import sys
import fileinput
from pathlib import Path


print('start!')

if Path(sys.argv[1]).exists():  # 第一引数がファイルだったら
    for line in fileinput.input():  # ファイルの内容を一行ずつprint
        print('file input')
        print(line)
else:  # 第一引数がファイルではなかったら
    for i in sys.argv[1:]:  # 引数の文字列をprint
        print('args input')
        print(i)