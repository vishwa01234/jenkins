import git
from git import Repo


repo_path =r"C:\Users\AvuA\Downloads\clone_12\backup_jen"
repo = git.Repo(repo_path)
current_branch = repo.active_branch
# Check for any changes
if repo.is_dirty(untracked_files=True):
    # Add all changes to the staging area
    repo.git.add(all=True)

    # Commit only the new changes
    repo.index.commit('New changes')

    # Push the changes to the remote repository
    origin = repo.remote(name='origin')
    origin.push(current_branch)
else:
    print('No changes to commit')
