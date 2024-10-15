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

### Strip whitespaces from line endings

This one liner uses the awk function `gsub(str, rep)` to replace the string `str` with `rep` on every
occurrence throughout the entire file. The function `gsub` is truly handy to know. 

```bash
awk '{gsub(/ +$/, ""); print}' $FILE.ext
```

### Remove duplicate lines

Absolutely brilliant way of removing duplicate lines from a file. This example is a excellent way to
demonstrate the power, simplicity, and flexibility of the AWK language.

```bash
 awk '!visited[$0]++' $FILE.ext
```

### Minify a configuration file

A standard configuration file for hostapd that possesses all the available options measures over 2000 lines of
code in length. The overwhelming majority of these configuration options are not used for a valid basic
configuration. It is the only situation where reduction of unused options would greatly benefit usability.
Since hostapd's configuration file indicates commented lines with the standard `#` has mark, we can use this
to our advantage along with a little awk to reduce the file down to only the options that are not commented
out.

```awk
awk -F '=' '!/#/ {if (NF != 0) print $0}' $CONFIG_FILE
```

Links
-----

I like cheatsheets they are quick.

- [Awk CheatSheet #1](https://quickref.me/awk)
- [AWK Guide](https://opensource.com/sites/default/files/gated-content/a_practical_guide_to_learning_gnu_awk.pdf)
