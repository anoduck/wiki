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

