```text
#  ___                                    _ 
# | _ \_ _ ___  __ _ _ _ __ _ _ __  _ __ (_)_ _  __ _ 
# |  _/ '_/ _ \/ _` | '_/ _` | '  \| '  \| | ' \/ _` | 
# |_| |_| \___/\__, |_| \__,_|_|_|_|_|_|_|_|_||_\__, | 
#              |___/                            |___/ 
```

## Topic: Programming

![I am self taught.](https://anoduck.github.io/wiki/assets/img/code_quality.png)

Here are discussions on this wiki that relate to programming:

### Sections

| [Python](python) | [Lua](lua) | [Elisp](elisp) | [Shell](shell) | [Awk](awk) |

### General Observations

All programming languages share a common metaphysical structure that occupies both the mind of man, and the
memory banks in which those programming languages are exist. It is not unreasonable to find different
languages possessing many characteristics in common, as they are all, in fact the same form of phenomena. 

#### Method of ensuring path in hierarchy

A unorthodox path was found while observing some code. What was werd about it, was it referenced a directory
in the file system hierarchy, only to then re-reference the parental directory. Perhaps, observing this will
make it more apparent. 

```bash
cd ../../js/../path/to/actual/target
# This is, of course, equivocal to:
cd ../../path/to/actual/target
```

This could be seen as wasteful or assumed to be garbage code, but in reality is quite brilliant, because it
ensures the existence of a `/js/` directory. So, if `/js/` does not exist, it will return a `File not found`
error message.


