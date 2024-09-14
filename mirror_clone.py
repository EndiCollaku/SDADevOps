import os
import subprocess
import sys

def usage():
    print("Usage: python mirror_clone_gitlab.py <old-repo-url> <new-repo-url>")
    sys.exit(1)

def run_command(command, cwd=None):
    """Run a shell command and handle errors"""
    try:
        result = subprocess.run(command, shell=True, check=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8')}")
        sys.exit(1)

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        usage()

    old_repo_url = sys.argv[1]
    new_repo_url = sys.argv[2]

    # Clone the old repository as a mirror
    print("Cloning old repository...")
    run_command(f"git clone --mirror {old_repo_url} old-repo.git")

    # Set up the new repository as a mirror
    print("Setting up new repository mirror...")
    run_command(f"git remote set-url --push origin {new_repo_url}", cwd="old-repo.git")

    # Push all branches, tags, and refs to the new repository
    print("Pushing to new repository...")
    run_command("git push --mirror", cwd="old-repo.git")

    # Cleanup: Remove the old-repo.git directory
    print("Cleaning up...")
    run_command("rm -rf old-repo.git")

    print("Repository successfully mirrored!")

if __name__ == "__main__":
    main()
