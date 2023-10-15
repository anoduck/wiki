```text
#   ____ ___ _____
#  / ___|_ _|_   _|
# | |  _ | |  | |
# | |_| || |  | |
#  \____|___| |_|
#
```

## Git

Lorem ipsum viverra elit praesent rhoncus aliquet praesent tempus, adipiscing dictumst sagittis ultricies tincidunt libero arcu nostra, varius sagittis suspendisse eleifend ad nunc aliquam. Viverra ligula luctus pharetra ad nam sed aliquet platea, cras ante diam velit cursus primis scelerisque erat pretium, himenaeos at aliquet nisi ut porta conubia. Sit erat volutpat augue vel enim senectus maecenas tincidunt curae, metus cras arcu leo sagittis odio at risus varius, elementum ligula posuere faucibus eros dolor accumsan libero.

Commodo justo consequat enim orci ut varius aliquam tempus, proin auctor viverra aptent placerat venenatis orci, libero habitant tortor amet nisl sapien est. Torquent praesent lacinia pretium per enim nisi sed suspendisse urna, suscipit donec vestibulum convallis nulla adipiscing tempor quis dui duis, inceptos lorem enim faucibus curabitur sem molestie fermentum. Potenti aenean sit sapien pharetra massa proin ut, id pretium enim rutrum fringilla urna rutrum, consectetur elementum sollicitudin proin volutpat metus.

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

