```text
# __     __            _                ____            _             _
# \ \   / /__ _ __ ___(_) ___  _ __    / ___|___  _ __ | |_ _ __ ___ | |
#  \ \ / / _ \ '__/ __| |/ _ \| '_ \  | |   / _ \| '_ \| __| '__/ _ \| |
#   \ V /  __/ |  \__ \ | (_) | | | | | |__| (_) | | | | |_| | | (_) | |
#    \_/ \___|_|  |___/_|\___/|_| |_|  \____\___/|_| |_|\__|_|  \___/|_|
#
```

## Version Control Systems

**One of the great modern marvels of our civilization.**

As the name implies _version control systems_ manage versioning of... well... stuff.
They are most commonly used in computer science to keep track of changes that occur to a specific file
or a set of files. There "versions" can be seen as a snapshot in time, and are undoubtedly userful. Their
implementation and management is a required skill for anyone interested in computational development. Since
not much else can be said, and words are rather difficult to forumulate at this moment, we will just move on
to the meat of this entry.

### Popular Version Control Systems

As computation has developed over time, _version control systems_ (VCS) have evolved with the science. As you can
image they come in all shapes and sizes, and different projects sometimes prefer different _version control
systems_ (VCS). Here are a list of the most popular ones.

- Git: Unquestionably the most popular and widely used.
- CVS: An older, but still highly popular and widely used VCS.
- SVN: "Subversion" can still be found all across the web.

### GIT

As stated above, git is the most popular and widely used VCS in the world, and being such, means you will run
in to it very often. The use of git is fairly straight forward, and easy to understand. You "clone"
repositories, "add" your changes, "commit" those changes to a version, and "push" them back into the
repository. Full disclosure, dealing with conflicts in versions is a pain in the ass, so try to avoid them. As
time goes by, I will add some of the lesser known commands for git below.

#### Removing sensitive data from git repos.

1. Download and install BFG.jar.
2. Perform a raw clone of the repository with the sensitive data. `git clone --mirror $REPO`
3. Add the sensitive data to a text file, one per line.
4. Run BFG.jar to remove that data. `java -jar BFG.jar -rt $SENSITIVE_DATA_FILE.txt --private $REPO_NAME`
5. Reflog the repo. `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
6. push your changes back. `git push`
