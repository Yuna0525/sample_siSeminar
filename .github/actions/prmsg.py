from github import Github

def post(message: str):
    """Post message to PR"""
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    with open(os.getenv("GITHUB_EVENT_PATH"), "r") as f:
        github_event = json.load(f)
    pr_number = github_event["number"]

    gh = Github(token)
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(body=message)
    