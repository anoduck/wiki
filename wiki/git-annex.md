```text
#   ____ ___ _____      _    _   _ _   _ _______  __
#  / ___|_ _|_   _|    / \  | \ | | \ | | ____\ \/ /
# | |  _ | |  | |     / _ \ |  \| |  \| |  _|  \  /
# | |_| || |  | |    / ___ \| |\  | |\  | |___ /  \
#  \____|___| |_|   /_/   \_\_| \_|_| \_|_____/_/\_\
```

Git Annex: The not so git, file system
=======================================

> [!info] Git-annex is a nontraditional distributed file system that allows users to share very large files
> without the requirement of a centralized server system.

The "git" in git-annex comes from git-annex's use of git to provide the index for the file system. Usage of
git-annex actually involves the management of a git repository, and git-annex is used almost as if it was an
extension of git.

Steps to creating a git annex file system
------------------------------------------

Here is a basic demonstration on how simply git annex is.

1. Create a git repository = `git init`
2. Initialize git annex for that repo = `git annex init`
3. Add your files to the annex = `git annex add .`
4. Commit your files to the filesystem = `git commit -am 'I did stuff.'`
5. Add your origin = `git remote add origin https://your.repo/server`

And your done.

Daily operations
-----------------

Below are several examples which explain how to use git-annex.

### Making changes to files

Here is where git-annex differs from a normal git repo. In order to modify a file, you first have to issue
the command for git-annex to unlock the file. If you forget to, you will be notified the file is "read only".
Once you have completed modifying the file, you will want your changes reflected in the annex, so you will
then need to commit your changes to the file system. 

```bash
$> echo "Here is a failed effort to modify a commited file in git-annex" > testfile.text
permission denied: testfile.text
# Now I unlock the file first.
$> git annex unlock testfile.text
unlock testfile.text ok
(recording state in git...)
# Now modify the file
$> echo "This testrun was successful" > testfile.text
# since we are creating a new file, we need to add it.Then commit the file to the file system
$> git annex add .
# Then we commit
$> git commit -am 'Created and added new file'
```

### Cloning a file system

Cloning an annex is almost exactly the same as cloning a git repo, except for one additional step. Once you
clone the repo, you have to then recreate the "git-annex part" of the repo/filesystem. You do this by performing
`git annex init .` again in the newly cloned repo. This is because git only handles the cloning, it does not handle
what it is cloning. 

```bash
git clone https://your.repo/address/repo
cd repo
git annex init .
```

### Syncing the file system and removing files

Git-annex synchronizes it's file system with remote annexes in the exact same manner it synchronizes repositories, except
it provides you with the shortcut command, which is "sync". 

So to sync a git repo with committed changes, you first have to pull from the remote repository, and then you have to push
everything back to the remote repository. Where git-annex combines both of these into the `sync` command.

Finally, you remove files from the annex by using the `git annex drop $FILE` command.
