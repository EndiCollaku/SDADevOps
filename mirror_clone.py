import git
import os
def mirror_clone(old_repo_url, new_repo_url):
    # Clone the old repository as a mirror
    repo_dir = 'temp_repo'
    if os.path.exists(repo_dir):
        os.system(f'rm -rf {repo_dir}')
    repo = git.Repo.clone_from(old_repo_url, repo_dir, mirror=True)
    
    # Set the new repository URL
    repo.remotes.origin.set_url(new_repo_url) 
    # Push to the new repository
    repo.git.push('--mirror')
    
    # Clean up
    os.system(f'rm -rf {repo_dir}')
    print(f'Successfully mirrored {old_repo_url} to {new_repo_url}')

# Example usage
old_repo = 'git@github.com:old_org/old_repo.git'
new_repo = 'git@github.com:new_org/new_repo.git'
mirror_clone(old_repo, new_repo)
