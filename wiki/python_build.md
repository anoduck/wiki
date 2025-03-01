```text
#  ____        _   _                   ____        _ _     _
# |  _ \ _   _| |_| |__   ___  _ __   | __ ) _   _(_) | __| |
# | |_) | | | | __| '_ \ / _ \| '_ \  |  _ \| | | | | |/ _` |
# |  __/| |_| | |_| | | | (_) | | | | | |_) | |_| | | | (_| |
# |_|    \__, |\__|_| |_|\___/|_| |_| |____/ \__,_|_|_|\__,_|
#        |___/
#
```

Building packages in python
============================

The deprecation of ezinstall
----------------------------

Before `pip` grew in popularity one would use a set of tools called "ezinstall", which used a
`setup.py` file to collect all the required dependencies, and prepare the package for use. This method has
finally been deprecated, and is not longer available for use. So, below we shall examine the alternatives to
`ezinstall`.

### Pyinstaller

Pyinstaller is Google's solution to build binary packages for python. It takes a setup.py file and a `*.whl`
file, and compiles the source code into a binary file.

### Pybuilder



