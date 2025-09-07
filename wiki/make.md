```text
#  __  __       _          ____  _          __  __
# |  \/  | __ _| | _____  / ___|| |_ _   _ / _|/ _|
# | |\/| |/ _` | |/ / _ \ \___ \| __| | | | |_| |_
# | |  | | (_| |   <  __/  ___) | |_| |_| |  _|  _|
# |_|  |_|\__,_|_|\_\___| |____/ \__|\__,_|_| |_|
#
```

## The Build System

### Intro

I could, and probably should, take the time to share a some historical information regarding how what is
generally referred to as "the build system" came into existence. Why it came into the sequence in which it
is, how it became adopted, and how it became nearly universal. I am sure, one way or another, Dennis Ritchie
had something to do with it when he ported his new language, `C++`, to unix. Instead, we are going to just
dive into it.

### The process

The standard make system has three main parts.

1. Configure
2. Make
3. Install

Sometimes, one must preconfigure before one can configuring, and often one wants to clean up after
installation.

#### Determine your compiler

Some BSD systems include two different sets of compilers of "C" and "CPP". They are clang and gcc, while only
one version of each can be installed on the same system, both can coexist without any conflicts. So before you
begin to compile any code in "C" or "CPP", you need to determine which of the two or both are compatible with
the code being compiled. This is easy to do, since often it is referred to in the documentation of the source
code, or you simply apply the the time tested approach of trial by error.

The default compiler for BSD systems is clang, although currently the most commonly compatible compiler for "C"
is Gnu's "gcc", which is just the way it is. So if you are going to want to use "gcc" or "g++" to compile the
code, you will need to declare it with an export statement first.

> [!info] Not "gcc", but "egcc"
> It is important to remember that in OpenBSD, GNU's "C" compiler has been renamed from "gcc" to "egcc" to
> avoid confusion. (although, it clearly adds to the confusion.)

```bash
export CC=/usr/local/bin/egcc CXX=/usr/local/bin/eg++
```

If by chance you declared one, but want to use another, then you will need to export the variable again to
your environment.

```bash
export CC=/usr/local/bin/clang CXX=/usr/local/bin/clang-cpp
```

#### Making with Make

`make` and it's cousin, `gnu make`, both accept a ridiculously plentiful amount of different flags. Way too
many flags than to even begin listing here. But there are a few you might want to be familiar with, as they
are used fairly often.

* `-k` = Tells `make` to continue on with the build as long as the encountered error does not affect the
	resulting target.
* `-j(N)` = This one is almost always added. N represents the number of threads the user would like to use for
	the build. This came into play after the creation of multi-core processors. Most often the flag is
	represented like the following. `make -j$(procnum)` Which tells make to use the same number of threads as
	there are processors available.

`make` also accepts commands. Of these commands, `install` and `clean` are the standard for use.

* `make install` is used after `make -j$(procnum)`, and tells make to install the target it just built.
* `make clean` is used after `make install`, and tells make to cleanup the build dir after the target is installed.

### CMAKE: A new way to `make` good.

		You make, I make, we all CMAKE...

Yes, I know these jokes are terrible, but anyways... Cmake is a software development platform that provides
several tools to aid developers in the building, testing, and automation of software. What is important to
remember is that cmake is not a build system itself, it is a generator for build files and configurations that
are then used by other build systems. Cmake is cross-platform and compiler independent. So, if you want to dumb
all the above down to the intellectual level of a potato, CMAKE makes building easier and faster.

#### Important flags in cmake

If you were to perform a standard build without the employment of cmake, because you wanted or needed to set local
system specific variables to be configured for the build or for the target. You would pass most of these variables to
the `./configure` command during the configuration process, but there are also circumstances when these
variables can be set during the `make` process. Now, if you were to employ cmake, they are required to be
passed during the execution of the `cmake` command. Like so:

```bash
cmake -DCMAKE_CXX_COMPILER="clang++" -DCMAKE_INSTALL_PREFIX="/usr/local" -DCMAKE_INSTALL_SYSCONFDIR="/etc" -DCMAKE_CXX_FLAGS="-I/usr/local/include" -DCMAKE_CXX_FLAGS="-I/usr/local/include/inotify" .
```

- Notice how each flag contains only one dash `-`, and then the capital letter `D`. No, I have no idea in this
world why each flags starts this way. What is important is knowing that it does.
- Also, notice how each flag contains a label, followed by the equal sign `=`, and then the value contained in
	matching double quotes `"..."`.
- The last two are different from the others, and very important. That define paths to be included during the
	build. Which is what the `-I` represents.


-----
