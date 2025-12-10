```text
#  ____   ___ _____ _____ ___ _     _____ ____
# |  _ \ / _ \_   _|  ___|_ _| |   | ____/ ___|
# | | | | | | || | | |_   | || |   |  _| \___ \
# | |_| | |_| || | |  _|  | || |___| |___ ___) |
# |____/ \___/ |_| |_|   |___|_____|_____|____/
```

Dotfiles: Your Configuration Files
==================================

There is no great mystery to what dotfiles are, "dotfile" is simply another way of saying "configuration file",
or a file that holds settings. On UNIX systems, these files are either preceded by or are contained in a
folder preceded by a dot ".". This dot indicates the file is "hidden", not like your dirty magazines are "hidden"
from your parents, but simply they are out of the way.

According to the XDG Desktop Specification, these files are usually kept in the "~/.config" directory, but
there are numerous popular programs that do not follow this convention. The long and the short of it, is
dotfiles contain settings and configuration values that tuned to your preferences, and a such you want to keep
them secure and have them available for use on different systems. Which is why this wiki entry is all about
dotfile managers.

Dotfile Managers
----------------

A dotfile file manager is a program that keeps track of the changes to dotfiles by storing them in a
version control managed directory. This directory is then stored on a remote repository server, which provides some
protection by giving you a backup in case you accidentally delete them, and it allows you to access these files from
numerous different locations. So you can install these dotfiles to other systems, and save yourself a lot of
setup time.

Below we will mention a few of these dotfile management programs, and will have to return to them later to
provide further explanation of their features.

### Chezmoi

"Chez moi" literally means "my place" or "home" in French, which is exactly what it does, it helps you to
manage files that make your environment like home. It is incredibly featureful and easy to work with, chezmoi
also integrates nicely with several commonly used programs.

#### Chezmoi Usage

Here is where I planned to discuss using ChezMoi.

### DotDrop

"DotDrop" is another dotfile manager that aims at being easy to use. It isn't as easy to install and work with
as chezmoi, but this is due to it's size being significantly smaller. It uses a templating system to help you
manage file differences across several hosts, which is something we were not pleased with. 

#### Dotdrop Usage

Below is the crash course into setting up dotdrop for the first time. One of the benefits of setting up
dotdrop is that you only have to set it up **once** for all of your hosts.

Requirements: git and python3 virtualenv

```bash
mkdir -p ~/dotfiles && cd $_
git init
git submodule add https://github.com/deadc0de6/dotdrop
# Here is where we diverge from the official docs, which does not account for newer python policy.
wget -O .gitignore https://github.com/github/gitignore/raw/refs/heads/main/Global/VirtualEnv.gitignore
virtualenv .venv
source .venv/bin/activate
python -m pip install -r dotdrop/requirements.txt
./dotdrop/bootstrap.sh
./dotdrop.sh --help
```

### Vcsh 

Vcsh is another dotfile manager which is extremely popular. It does things.

- https://github.com/RichiH/vcsh/blob/main/doc/README.md

#### Myrepos 

Myrepos is a dependency required to run vcsh, and it does something fancy.

- https://myrepos.branchable.com/

#### Vcsh Usage

You can use it.

### Honorable Mentions

Here are some dotfile managers worth mentioning.

1. dotly
2. dotter
3. dotbare
4. lnk

