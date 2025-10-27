```text
#  ____            _
# | __ )  __ _ ___| |__
# |  _ \ / _` / __| '_ \
# | |_) | (_| \__ \ | | |
# |____/ \__,_|___/_| |_|
#
```

Bash: The Bourne Again Shell
=============================

Link to the Shell reference page --> [shell](shell)

## Bash conditional operators 

Conditional operators are used in "if" statements and allow testing for many diffierent modes:

```text
    -n VAR - True if the length of VAR is greater than zero.
    -z VAR - True if the VAR is empty.
    STRING1 = STRING2 - True if STRING1 and STRING2 are equal.
    STRING1 != STRING2 - True if STRING1 and STRING2 are not equal.
    INTEGER1 -eq INTEGER2 - True if INTEGER1 and INTEGER2 are equal.
    INTEGER1 -gt INTEGER2 - True if INTEGER1 is greater than INTEGER2.
    INTEGER1 -lt INTEGER2 - True if INTEGER1 is less than INTEGER2.
    INTEGER1 -ge INTEGER2 - True if INTEGER1 is equal or greater than INTEGER2.
    INTEGER1 -le INTEGER2 - True if INTEGER1 is equal or less than INTEGER2.
    -h FILE - True if the FILE exists and is a symbolic link.
    -r FILE - True if the FILE exists and is readable.
    -w FILE - True if the FILE exists and is writable.
    -x FILE - True if the FILE exists and is executable.
    -d FILE - True if the FILE exists and is a directory.
    -e FILE - True if the FILE exists and is a file, regardless of type (node, directory, socket, etc.).
    -f FILE - True if the FILE exists and is a regular file (not a directory or device).
```

-----

## Anoduck Approved CheatSheet

- [Bash Scripting CheatSheat](https://devhints.io/bash)
- [A Complete Guide to Bash Arrays](https://shell-tips.com/bash/arrays/#gsc.tab=0)

## Bash Tutorials

[Bash Hackers](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/)

[Bash Academy](https://github.com/lhunath/guide.bash.academy)

[Pure Bash Bible](https://github.com/dylanaraps/pure-bash-bible)

## Bash Package Managers

### Basher

Basher is a package manager for bash shell scripts. Particularly shell scripts that within themselves
constitute a package.

[Basher](https://www.basher.it/)

### Basalt

A new alternative to Basher is basalt, which is still in it’s early stages of development, but
appears to have generated quite a large following. 

[Basalt](https://github.com/bash-bastion/basalt)

## Bash Frameworks

### Bash-it

The most popular shell customizatio
simple to use, provides powerful customization, and little overhead. It alos provides a set of ready
to be enabled custom bash prompts.

[Bash-IT](https://github.com/Bash-it/bash-it)

## Bash CLI Frameworks

A good CLI framework provides developers with a ready made library for use in creation of bash
terminal user interfaces. This removes a good of amount of work, as it provides basic references to
customize everything from the color to alignment of output. Below are several noteworthy libraries
to help create CLI’s.

* [bash-cli](https://github.com/SierraSoftworks/bash-cli)
* [Skeleton-Bash](https://github.com/jazzschmidt/skeleton-bash)
* [bashmuiltitool](https://github.com/gavinlyonsrepo/bashmultitool)

## Bash Utilities

* [latest-releases](https://github.com/nickjj/latest-releases)
* [chest](https://github.com/lukechilds/chest)
