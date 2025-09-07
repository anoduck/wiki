```text
#   ____ ___ _____
#  / ___|_ _|_   _|
# | |  _ | |  | |
# | |_| || |  | |
#  \____|___| |_|
#
```

## Git

First and foremost git is a version control system, and it is the most popular version control
system in use today. Git can do a lot of things for you, and has an intuitive command structure to
allow this. Git would not be as popular as it is today, if it were not for the site Github. Which
allows anyone to host and share software source code for free. 

Below are a few examples on how to use git that are not often encountered. 

### Basic guide to making a pull request

A pull request is how another user can contribute code to a repository they are not the creator
of. This proceess can be performed completely remotely from the command line, but for our purposes
will be performed using both the command line and a browser with Github.

1. The repository needs to be forked from the original repository. This portion must be done with a
   browser and user account on Gihub.
2. The newly forked repository must be cloned locally. 
3. Once cloned, changes then can be made to the source code. `git clone https://github.com/USERNAME/REPOSITORY`
4. Those changes need to be committed. `git add . && git commit -am 'some message about the commit'`
5. Then return back to the forked repository on Github. Select the "Pull requests" tab.
6. Then click "New pull request" and your done.

### Removing sensitive data from git repos.

1. Download and install BFG.jar.
2. Perform a raw clone of the repository with the sensitive data. `git clone --mirror $REPO`
3. Add the sensitive data to a text file, one per line.
4. Run BFG.jar to remove that data. `java -jar BFG.jar -rt $SENSITIVE_DATA_FILE.txt --private $REPO_NAME`
5. Reflog the repo. `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
6. push your changes back. `git push`

### Removing git-LFS from a repository

This is a small script that should perform everything needed to remove git lfs from the repository.
Unfortunately, it will also uninstall git-lfs from your system, but it can be easily installed again.

```bash
#!/usr/bin/env bash

git add .
git commit -am 'preparing for lfs uninstall' && git push
git lfs pull -all
git lfs uninstall
git lfs ls-files | cut -f 3 -d ' ' | xargs git rm --cached
rm -rf .git/lfs .git/hooks/pre-push .gitattributes
git add . && git commit -am 'removed lfs' && git push
git status
```

### Removing a submodule from a repository

When it comes to removing a submodule from a repository, it is not as easy as simply removing the submodule's
directory, not is it as easy as removing the modules entry from `.gitsubmodule`. There is a method to these
things.

1. Delete the relevant section from the `.gitmodules` file.
2. Stage the changes to that file with `git add .gitmodules`.
3. Delete relevant section from `.git/config`.
4. Remove submodule from git cache. `git rm --cached .git/modules/$YOURMODULE`
5. Commit these changes. `git commit -am 'removed module'`
6. THEN remove the submodule directory.

To remove a submodule you need to:

    Delete the relevant section from the .gitmodules file.
    Stage the .gitmodules changes:
    git add .gitmodules
    Delete the relevant section from .git/config.
    Remove the submodule files from the working tree and index:
    git rm --cached path_to_submodule (no trailing slash).
    Remove the submodule's .git directory:
    rm -rf .git/modules/path_to_submodule
    Commit the changes:
    git commit -m "Removed submodule <name>"
    Delete the now untracked submodule files:
    rm -rf path_to_submodule

See also: alternative steps below.

--John Douthat

### Undoing a commit

You committed a change that you were not supposed to and need to undo the commit. In git this is referred to
as "reverting", because you are returning to a previous state.

Before you get over exuberent reverting shit, you need to discover the hash of the latest commit. This can be
done using `git log`.

```bash
git log --all --decorate --oneline --graph 
```

Here is a hint: It is the one on the top line.

Once you discovered your commit hash, you then can revert your commit.

```bash
git revert -m 1 $COMMIT_HASH
```

The addition of the `-m 1` flag tells git to favor changes from the first parent.

> [!caution] Do not use `git reset`
> `git reset` can be a destructive command if used incorrectly.

Git revert will create a new commit reverting the repo to it's previous state.

#### Undoing undoing a commit

Undoing a previous revert is almost identitical to doing the revert. This is because `git revert` does not
wipe the previous undesired commit from the history of the git log. Rather, it creates a new commit that then
changes things back to how they were.

So to undo a previous git revert, you follow the same steps.

```bash
git log --all --decorate --oneline --graph 
```

The commit that reverted the repo to it's previous state should be on the top line. So you will want to use
that hash and run `git revert` again.

```bash
git revert -m 1 $COMMIT_HASH
```

You can also run `git cherry-pick $COMMIT_HASH` for a similar result.
