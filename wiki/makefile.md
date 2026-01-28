```text
#  __  __       _         __ _ _        ____              _
# |  \/  | __ _| | _____ / _(_) | ___  / ___| _   _ _ __ | |_ __ ___  __
# | |\/| |/ _` | |/ / _ \ |_| | |/ _ \ \___ \| | | | '_ \| __/ _` \ \/ /
# | |  | | (_| |   <  __/  _| | |  __/  ___) | |_| | | | | || (_| |>  <
# |_|  |_|\__,_|_|\_\___|_| |_|_|\___| |____/ \__, |_| |_|\__\__,_/_/\_\
#                                             |___/
```

# Makefile Syntax

You have used them thousands of times to compile anything and everything, now it is time to get off your lazy
ass and start to learn how to write them.

A superiorly commentated makefile is [Isaac's](https://gist.github.com/isaacs/62a2d1825d04437c6f08)

> [!info] Whatever you do, if you notice a grammatical error in Isaac's tutorial, do not offer any suggestions
> toward making a correction. Isaac will get really pissed.

## What are Makefiles?

Makefiles are basically scripts that include a set of instructions to be followed by the program `make` or
`bmake`. The files contain markup which is used to form the instruction set. There is really very little to
them, and although they can possess quite a lot of markup, learning how to create them is actually quite easy.

> [!info] Each line of a makefile is parsed first using the makefile syntax, and **THEN** the result is passed
> to the shell.

## The Syntax

Before you write your first makefile, you need to decide which make are you planning to target. There is the
original unix `make` included in unix and BSD systems, which is referred to `bmake` on linux machines, and
then there is the newer and more robust Gnu `make`, which is referred to as `gmake` on bsd machines. Also,
there is the option to write a makefile that can be run by either of the two if desired. The choice is really
a matter of choosing between simple and complex. If you need a complex makefile that uses more robust
features, then Gnu make is the best of the two options, but if you want to make it simple, go with the
original.

To be rather unoriginal and lazy, we will simply follow the layout provided in the [BSD Make Manpage](https://man.openbsd.org/make).

### Dependency 

|  symbol  | meaning                                                     |
| :------: | ---------------------------------------------------------   |
|   `:`    | Target considered out-of-date if prerequisites are newer    |
|   `!`    | First examines all prerequisites and re-creates if required |
|   `::`   | Consider each dependency independently, eval if newer       |

### Variables

The make system has many predefined variables, many of which you may never use. Make also allows for you to
define your own variables using the make variable syntax.

| Symbol | Meaning                                                             |
| :----: | ------------------------------------------------------------------- |
|  `=`   | Assign a value                                                      |
|  `:=`  | Assign with expansion                                               |
|  `+=`  | Append the value                                                    |
|  `?=`  | Assign if not defined                                               |
|  `!=`  | Expand variable, execute with shell, and return result as variable. |
| `!!=`  | Expand variable,execute only when needed, and assign value.         |

### BSD Rule Syntax

> [!info] Stem:
> a filename without the last extension.

Both BSD and GNU Make possess a rule syntax that is particular to that version of make. Since we have
primarily focused on the BSD variant, we will continue with the BSD rule syntax first.

| Symbol | Meaning                                                |
| :----: | ------------------------------------------------------ |
|  `@`   | Target name                                            |
|  `%`   | Archive member name (only valid for library rules).    |
|  `!`   | Archive file name (only valid for library rules).      |
|  `?`   | Out of date prerequisites array for target             |
|  `<`   | The first prerequisite.                                |
|  `*`   | The "stem" portion that matched the rule's definition. |

There are numerous other variables and environmental variables that are not mentioned in this overview. For
more information on those please refer to [the Make man page.](https://man.openbsd.org/make.1)

### Gnu Rule Syntax

For each target a rule can be added that informs the shell on what to do. These are the special variables for
those rules. (Confirmed for Gnu Make.)

|  Symbol  | Meaning                                                |
| :------: | ---------                                              |
|   `$@`   | The Target file                                        |
|   `$<`   | The first prerequisite                                 |
|   `$^`   | An array of all the input files                        |
|   `$?`   | All files newer than the target                        |
|   `$$`   | Represents a literal "$"                               |
|   `$*`   | The "stem" portion that matched the rule's definition. |
| `$(@D)`  | The Directory portions of the target.                  |
| `$(@F)`  | The File portions of the target.                       |
| `$(<D)`  | The Directory portions of the prerequisite.            |
| `$(<F)`  | The File portions of the prerequisite.                 |

### Statements

The make system also allows the use of include statements, conditionals, and "for" loops. More information can
be found on these along with "phonys" in the [the Make man page.](https://man.openbsd.org/make.1)

