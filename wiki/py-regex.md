```text
#  ____              ____
# |  _ \ _   _      |  _ \ ___  __ _  _____  __
# | |_) | | | |_____| |_) / _ \/ _` |/ _ \ \/ /
# |  __/| |_| |_____|  _ <  __/ (_| |  __/>  <
# |_|    \__, |     |_| \_\___|\__, |\___/_/\_\
#        |___/                 |___/
#
```

## Cheatsheet: Python Regex

In order to use regex in python you will need to import the `re` package. 

### Three Functions

There are three main functions to be aware of in the re package.

1. compile
2. search()
3. findall

### Basic Shit

- `\d` Matches any decimal digit; this is equivalent to the class [0-9].
- `\D` Matches any non-digit character; this is equivalent to the class [^0-9].
- `\s` Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
- `\S` Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
- `\w` Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
- `\W` Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].


