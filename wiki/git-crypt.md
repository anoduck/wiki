```text
   ____ ___ _____      ____ ______   ______ _____
  / ___|_ _|_   _|    / ___|  _ \ \ / /  _ \_   _|
 | |  _ | |  | |_____| |   | |_) \ V /| |_) || |
 | |_| || |  | |_____| |___|  _ < | | |  __/ | |
  \____|___| |_|      \____|_| \_\|_| |_|    |_|
```

Git Crypt
=========

Git-crypt provides low level security for sensitive data contained within a Git Repository, is relatively 
easy to setup, and to manage. It has two modes of operation, both provide different levels of security.
First, is key mode, which provides the lowest amount of security. Second, is GPG mode, which provides a 
slightly higher level of security solely due to it's incorporation of gpg keys. We will cover both of these
separately.

Git-crypt does not encrypt the entirety of a repository, as it was specifically designed not to do that, but
rather it was designed to allow a mix of both encrypted and unencrypted files. Git-crypt, also provides
encryption of sensitive files transparently, which means you will not need to perform the encryption process
manually everytime you make a change to the file. This allows the developer to share contents of a repository
freely with the public.

Just as Git itself is dependent on residing in a folder, git-crypt depends on residing inside of a pre-existing
git repository, and should be viewed upon as an extension of git not as a seperate version management framework.

The `.gitattributes` file
--------------------------

The `.gitattributes` file is used by several plugins / extensions for git, and not just for git-crypt alone.
Although, we will only be covering it's application to git-crypt.

Regardless of which mode you plan to operate git-crypt in, the first thing any user should do is create a
`.gitattributes` file in the root folder of the repository. As this file is what tells git-crypt which files
it needs to manage encryption for, and you create this file first to prevent compromising data to the public.

This file has a basic structure of `{$FILE_PATTERN} label=value label=value` per line. Using this file with
git-crypt means that with each file pattern provided, the two following labels or "attributes" will always be
the exact same pairing, `filter=git-crypt diff=git-crypt`. Which makes it rather easy to configure.

An example of this file can be found below.

```git-config
secretfile filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
secretdir/** filter=git-crypt diff=git-crypt
```

> [!warning] DO NOT ENCRYPT ANY FILES REQUIRED FOR USE BY GIT, GIT MODULES, OR GIT-CRYPT.

Key Mode
---------

Init git-crypt in your repository by running the command `git-crypt init`, which will generate a key file
containing your encryption key. By default, this file is stored in `.git/git-crypt/keys/default` in the base
of your repository. If you need a copy of this key for use on another machine (which is the point), then you
can use `git-crypt export /YOUR/PATH` to export it, then on your remote machine with the generated key
file from the previous command run `git-crypt unlock KEY_FILE.key`, and then you have setup your remote machine
to handle git-crypt encryption.

Gpg Mode
--------

Surprisingly, setting up git-crypt to operate in GPG mode is almost exactly like the above, except it requires
one additional step, `git-crypt add-gpg-user $YOUR_GPG_ID`. Where `YOUR_GPG_ID` can be any unique identifier
used to identify a GPG public key. This will result in the key file originally generated with `git-crypt init`
to be overwritten with a new key file generated with your GPG credentials.

Then to setup a remote machine to manage your git-crypt encrypted files, simply issue the command `git-crypt
unlock`, and you will be prompted for the password to your GPG credentials.

References
----------

- [How to manage your Secrets with git-crypt](https://dev.to/heroku/how-to-manage-your-secrets-with-git-crypt-56ih)
- [Git-crypt: Transparent file encryption in git.](https://www.agwa.name/projects/git-crypt/)
