```text
#   ____ _                          _
#  / ___| |__   __ _ _ __ __ _  ___| |_ ___ _ __
# | |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__|
# | |___| | | | (_| | | | (_| | (__| ||  __/ |
#  \____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|
#
#  _____                     _ _
# | ____|_ __   ___ ___   __| (_)_ __   __ _
# |  _| | '_ \ / __/ _ \ / _` | | '_ \ / _` |
# | |___| | | | (_| (_) | (_| | | | | | (_| |
# |_____|_| |_|\___\___/ \__,_|_|_| |_|\__, |
#                                      |___/
```

Character Encoding
------------------

The topic of character encoding truly deserves a more in depth discussion than we are prepared to grant it.
Being completely self taught, we are aware this topic was part of an introductionary lecture we missed out on,
and unfortunately it is one of the foundational pieces of knowledge for computer science. There is an
abundance of different character sets, because computers are required to display a bunch of different forms of
languages and symbols. Different character sets variate in the actual size in bits the character itself is comprised
of. For example the most common character set is UTF-8, which stands for "Universal Transformation Format 8
bits", and each character is comprised of 8 bits. Yada, yada, yada, etc ...

### Encoding tools

If running one of the *nixs, there are four tools at your disposal to handle issues encountered with file
encoding, these are `enca`, `enconv`, `iconv`, `uconv`, and `recode`.

`enca` and `enconv` are sibling tools and commonly come together in the same package named after the first of
these tools, `enca`. `enca` is primarily used to detect charsets, encodings, and language based encodings. Where `enconv` is
used to encode a file into a desired charset, encoding, or language based encoding.

`iconv` and `uconv` are NOT sibling programs at all, but perform similar functions. 

`recode` converts files from one character set to another. 

### Examples

Here is what you came for. Simple examples

`recode utf8..ISO-8859-1 my-file.txt` - converts files encoded with utf8 to iso-8859-1
