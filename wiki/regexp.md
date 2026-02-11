``` text
#  ____  _____ ____ _______  ______
# |  _ \| ____/ ___| ____\ \/ /  _ \
# | |_) |  _|| |  _|  _|  \  /| |_) |
# |  _ <| |__| |_| | |___ /  \|  __/
# |_| \_\_____\____|_____/_/\_\_|
```

# Regular Expressions

It was debated whether to include this section under programming languages, or create a section for itself
outside of the programming language tree, and it was decided the importance of understanding regular
expressions entitled it to a section all to itself. 

So, what is REGEXP? REGEXP, also abbreviated REGEX (preferred), is an acronym for "Regular Expressions". 
REGEX can be summarized in one word, "matching". IF you wanted to be more technical, "Pattern Matching".
Using REGEX allows the user to match complex patterns and search text with a realtively high precision. It is
distinct from globbing, due to it's extensiveness and complexity. Where globbing primarily relies on wildcard
symbols/characters, the forumulation of a regular expression is very technical and can incorporate any number
and/or combination of characters and symbols. 

REGEX also comes in many forms, and nearly every programming language has it's own REGEX syntax. The Perl
Common Regular Expressions is the most commonly accepted REGEX syntax, but it is not universally accepted, not
by a long shot. Although REGEX has many variations, there are some symbols that are almost always the same
regardless of what language the syntax is in. These are referred to as wildcards, and wildcards includes
symbols like `*`, `+`, and `.`. Furthermore, regex often is indicated by it's inclusion in backslashes, 
sometimes begins with a `^` and ends with a `$`.

This was supposed to be a closing sentence, but unfortunately I can't think of what else to write. So, I will
leave a regex here for you to match yourself.

``` c++
/^[-a-zA-Z0-9\ \.]*$/
```

## Javascript REGEX

In JS a regex expression is placed between two backslashes followed by a flag to indicate what the REGEX is supposed
to be used for, or what is the language supposed to do with it. A table of JS regex flags is found below.

| Javascript |   regex flags    |
| :--------: | :--------------: |
|    `g`     |      Global      |
|    `i`     | Case Insensitive |
|    `m`     | Multiline regex  |
|    `s`     |   Single line    |
|    `u`     |     Unicode      |
|    `y`     |      sticky      |

So taking what we already know, a regex to match any character one or more times would look like: `\.+\g`.

A noncapturing group, referred to as a fixed string in other languages, is written like so: `\(?:string)\g`

| Patterns |    Description     |    Example     |
| :------: | :----------------: | :-----------:  |
| `(?:  )` | Noncapturing Group | `\(?:duck)?\g` |
|  `[^]`   |    Negated set     |  `\[^&\s]+\g`  |
|          |                    |                |
|          |                    |                |
|          |                    |                |

## Sources
- [Regexer](https://regexr.com/)
- [Regex and Globbing](https://the-engineering-corner.com/bash-in-depth/0018-Regular-Expressions-and-Globbing.html)
