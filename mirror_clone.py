import os
from git import Repo
from github import Github

# GitHub username and token
username = "your-github-username"
token = "your-github-token"

# List of old repositories and their corresponding new repositories
repos = {
    "old-repo1": "new-repo1",
    "old-repo2": "new-repo2",
    # Add more repositories as needed
}

# Initialize GitHub API client
g = Github(token)

for old_repo, new_repo in repos.items():
    # Clone the old repository as a bare repository
    old_repo_url = f"https://github.com/{username}/{old_repo}.git"
    Repo.clone_from(old_repo_url, f"{old_repo}.git", mirror=True)
    
    # Create the new repository on GitHub if it doesn't exist
    user = g.get_user()
    try:
        user.create_repo(new_repo)
    except Exception as e:
        print(f"Repository {new_repo} already exists or could not be created: {e}")
    
    # Mirror-push to the new repository
    new_repo_url = f"https://github.com/{username}/{new_repo}.git"
    repo = Repo(f"{old_repo}.git")
    repo.remotes.origin.set_url(new_repo_url)
    repo.remotes.origin.push(mirror=True)
    
    # Clean up the temporary local repository
    os.system(f"rm -rf {old_repo}.git")
    
    print(f"Mirrored {old_repo} to {new_repo}")

print("All repositories have been mirrored.")
