#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 <old-repo-url> <new-repo-url>"
    exit 1
}

# Check if both old and new repo URLs are provided
if [ "$#" -ne 2 ]; then
    usage
fi

OLD_REPO_URL="$1"
NEW_REPO_URL="$2"

# Clone the old repository as a mirror (clones all branches, tags, and refs)
echo "Cloning old repository..."
git clone --mirror "$OLD_REPO_URL" old-repo.git

# Enter the repository directory
cd old-repo.git || { echo "Failed to enter repository directory"; exit 1; }

# Add the new repository as a remote mirror
echo "Setting up new repository mirror..."
git remote set-url --push origin "$NEW_REPO_URL"

# Push all branches, tags, and refs to the new repository
echo "Pushing to new repository..."
git push –mirror

# Cleanup

cd ..
rm -rf old-repo.git
echo "Repository successfully mirrored!"
