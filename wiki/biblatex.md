```text
#  ____  _ _     _       _
# | __ )(_) |__ | | __ _| |_ _____  __
# |  _ \| | '_ \| |/ _` | __/ _ \ \/ /
# | |_) | | |_) | | (_| | ||  __/>  <
# |____/|_|_.__/|_|\__,_|\__\___/_/\_\
#     _              _
#    / \   _ __   __| |
#   / _ \ | '_ \ / _` |
#  / ___ \| | | | (_| |
# /_/   \_\_| |_|\__,_|
#  ____  _ _
# | __ )(_) |__   ___ _ __
# |  _ \| | '_ \ / _ \ '__|
# | |_) | | |_) |  __/ |
# |____/|_|_.__/ \___|_|
```

Biblatex and Biber
===================

This is where I write an introduction to the page, that is basically a lot of bullshitting about accumulated
knowledge.

Biblatex
--------

This is where I will put shit about Biblatex, and more importantly how it differentiates from the ancient
relic known as Bibtex.

### Intro

This is where I will write an intro to Biblatex

### Biblatex Vs. BibTex

This is where I will write about the differences between the two. 

Biber
------

This is a short introduction to Biber.

### Installing Biber on OpenBSD

Now, here is what I wanted to write about.

Keep in mind, you do not want to use `sudo` or `doas` for any of the following commands. You also want to
avoid using the root account for these commands as well. Doing so will result in the corruption of your
system's perl distribution.

#### Install Perlbrew

To install Biber on OpenBSD, Perlbrew is required. 

```bash
\curl -L https://install.perlbrew.pl | bash
```

Open your shell's rc file and ensure the following lines are in it.

```bash
source ~/perl5/perlbrew/etc/bashrc
```

This can be done with a quick grep, `cat ~/.bashrc | grep perlbrew`, and if you do not see it you can use
echo to add it, `echo "source ~/perl5/perlbrew/etc/bashrc" >> ~/.bashrc`.

##### Setup Perlbrew

You will need to install the latest release of perl with perlbrew. This will take some time for perlbrew
to finish building and installing.

```bash
perlbrew install perl-stable > /dev/null 2>&1 | tail -f ~/perl5/perlbrew/build.perl-*.log
```

Then install cpm, the perl package manager. If your not used to using cpm, it is a little different from cpan,
but it is much faster. Cpm by defaults install packages in a local project folder, this is not what we want.
So, everytime we run cpm we will need to use the `-g` flag for global, just like you would with npm. 

```bash
perlbrew install-cpm
```

Open up a new shell, and inform perlbrew you want to use the perl release you just installed.

```bash
perlbrew use $(perlbrew list)
```

This should complete setup of perlbrew.

#### Acquire dependencies and source

Go ahead and clone the repository with the source code.

```bash
git clone https://github.com/plk/biber && cd biber
```

It is time to install the required perl dependencies for the build, which will be done with cpm.

```bash
cpm install -g Module::Build bibtex Readonly::XS Pod::Simple Pod::Simple::TranscodeSmart \
  Pod::Simple::TranscodeDumb pod::PerlDoc Text::BibTex Text::CSV
```

Next you will need to extract the files 
