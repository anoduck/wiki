``` text
#     ___        ___  __
#    / \ \      / / |/ /
#   / _ \ \ /\ / /| ' /
#  / ___ \ V  V / | . \
# /_/   \_\_/\_/  |_|\_\
#
```

AWK: The most AWKward language
==============================

If there was one word to summarize one's experience with the AWK programming language, then that word would be
"befuddled" (Ha, you thought I was going to say awkward!). In all seriousness, AWK is an incredibly useful
language to know, as it is incredibly powerful, and can do alot with very little code required. It's primary
use is in text processing, but can be used to perform other tasks.

For now, until further experience is acquired, we shall simply list some helpful links for use in learning
more about AWK.

Snippets of Awkness
--------------------

Awk can be both executed from the command line as inline code, and executed as a programmable script file. The
former is quite useful if the desire is to use awk to process the output of a preceding shell command. This is
used quite often. The later, if the desire is to process data contained within a file or database. 

The entirety of awk programs is comprised of pattern/action pairs. Where the pattern is used to define what
awk should process, and the action defines what awk should do to process it. There are several built in
variables that will be discussed later, and there is also a "BEGIN" section that can be used to define
variables before processing. 

The only real drawback to using awk is the absence of local variables. In awk all variables are global, there
are several ways to work around this as defined in several guides. Basically, when it comes to variables, just
create them and use them. Nothing else fancy is needed.

### Split file on empty line

Below are two examples on how to split the output of a command into smaller files.

1. Complex example

``` awk
$ awk -v RS="" '{
    split(FILENAME,a,".")  # separate name and extension
    f=a[1] NR "." a[2]     # form the filename, use NR as number
    print > f              # output to file
    close(f)               # in case there are MANY to avoid running out f fds
}' A.in
```

2. Simpler form

``` awk
awk -v RS= '{print > ("whatever-" NR ".txt")}' file.txt
```

### Using shell variables in AWK

Using shell variables in AWK can be accomplished like so:

``` bash
awk -v var="$variable" '{print var}'
```

Links
-----

I like cheatsheets they are quick.

- [Awk CheatSheet #1](https://quickref.me/awk)
- [AWK Guide](https://opensource.com/sites/default/files/gated-content/a_practical_guide_to_learning_gnu_awk.pdf)
