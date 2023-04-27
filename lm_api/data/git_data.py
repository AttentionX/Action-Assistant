# Todo
# Add example usage of each git command
# Save to list
# Save to db


# Examples
git_add = '''
git add
Moves changes from the working directory to the staging area. This gives you the opportunity to prepare a snapshot before committing it to the official history.
'''

git_add_explanation = '''
'''

git_add_examples = '''
Common options
git add <file>
Stage all changes in <file> for the next commit.

git add <directory>
Stage all changes in <directory> for the next commit.

git add -p
Begin an interactive staging session that lets you choose portions of a file to add to the next commit. This will present you with a chunk of changes and prompt you for a command. Use y to stage the chunk, n to ignore the chunk, s to split it into smaller chunks, e to manually edit the chunk, and q to exit.

Examples
When you're starting a new project, git add serves the same function as svn import. To create an initial commit of the current directory, use the following two commands:

git add .
git commit
Once you've got your project up-and-running, new files can be added by passing the path to git add:

git add hello.py
git commit
The above commands can also be used to record changes to existing files. Again, Git doesn't differentiate between staging changes in new files vs. changes in files that have already been added to the repository.
'''

git_branch = '''
git branch
This command is your general-purpose branch administration tool. It lets you create isolated development environments within a single repository.
'''

git_branch_explanation = '''
A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process. You can think of them as a way to request a brand new working directory, staging area, and project history. New commits are recorded in the history for the current branch, which results in a fork in the history of the project.

The git branch command lets you create, list, rename, and delete branches. It doesn’t let you switch between branches or put a forked history back together again. For this reason, git branch is tightly integrated with the git checkout and git merge commands.
'''

git_branch_examples = '''
Common Options
git branch
List all of the branches in your repository. This is synonymous with git branch --list.

git branch <branch>
Create a new branch called <branch>. This does not check out the new branch.

git branch -d <branch>
Delete the specified branch. This is a “safe” operation in that Git prevents you from deleting the branch if it has unmerged changes.

git branch -D <branch>
Force delete the specified branch, even if it has unmerged changes. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.

git branch -m <branch>
Rename the current branch to <branch>.

git branch -a
List all remote branches. 
'''

git_checkout = '''
git checkout
In addition to checking out old commits and old file revisions, git checkout is also the means to navigate existing branches. Combined with the basic Git commands, it's a way to work on a particular line of development.
'''

git_clean = '''
git clean
Removes untracked files from the working directory. This is the logical counterpart to git reset, which (typically) only operates on tracked files.
'''

git_clone = '''
git clone
Creates a copy of an existing Git repository. Cloning is the most common way for developers to obtain a working copy of a central repository.
'''

git_commit = '''
git commit
Takes the staged snapshot and commits it to the project history. Combined with git add, this defines the basic workflow for all Git users.

git commit --amend
Passing the --amend flag to git commit lets you amend the most recent commit. This is very useful when you forget to stage a file or omit important information from the commit message.
'''

git_config = '''
git config
A convenient way to set configuration options for your Git installation. You'll typically only need to use this immediately after installing Git on a new development machine.
'''

git_fetch = '''
git fetch
Fetching downloads a branch from another repository, along with all of its associated commits and files. But, it doesn't try to integrate anything into your local repository. This gives you a chance to inspect changes before merging them with your project.
'''

git_init = '''
git init
Initializes a new Git repository. If you want to place a project under revision control, this is the first command you need to learn.
'''

git_log = '''
git log
Lets you explore the previous revisions of a project. It provides several formatting options for displaying committed snapshots.
'''

git_merge = '''
git merge
A powerful way to integrate changes from divergent branches. After forking the project history with git branch, git merge lets you put it back together again.
'''

git_pull = '''
git pull
Pulling is the automated version of git fetch. It downloads a branch from a remote repository, then immediately merges it into the current branch. This is the Git equivalent of svn update.
'''

git_push = '''
git push
Pushing is the opposite of fetching (with a few caveats). It lets you move a local branch to another repository, which serves as a convenient way to publish contributions. This is like svn commit, but it sends a series of commits instead of a single changeset.
'''

git_rebase = '''
git rebase
Rebasing lets you move branches around, which helps you avoid unnecessary merge commits. The resulting linear history is often much easier to understand and explore.

git rebase -i
The -i flag is used to begin an interactive rebasing session. This provides all the benefits of a normal rebase, but gives you the opportunity to add, edit, or delete commits along the way.
'''

git_reflog = '''
git reflog
Git keeps track of updates to the tip of branches using a mechanism called reflog. This allows you to go back to changesets even though they are not referenced by any branch or tag.
'''

git_remote = '''
git remote
A convenient tool for administering remote connections. Instead of passing the full URL to the fetch, pull, and push commands, it lets you use a more meaningful shortcut.
'''

git_reset = '''
git reset
Undoes changes to files in the working directory. Resetting lets you clean up or completely remove changes that have not been pushed to a public repository.
'''

git_revert = '''
git revert
Undoes a committed snapshot. When you discover a faulty commit, reverting is a safe and easy way to completely remove it from the code base.
'''

git_status = '''
git status
Displays the state of the working directory and the staged snapshot. You'll want to run this in conjunction with git add and git commit to see exactly what's being included in the next snapshot.
'''