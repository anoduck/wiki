```text
#  _   _       _       _
# | | | | __ _| |_ ___| |__
# | |_| |/ _` | __/ __| '_ \
# |  _  | (_| | || (__| | | |
# |_| |_|\__,_|\__\___|_| |_|
#
```

Hatch Project Manager
======================

Hatch is a beautifully written project manager for Python. When it is initialized it generates a basic, but
thorough, framework for development of python programs. It also creates and manages a virtual environment to
install dependencies into. Last, but not least, Hatch comes with it's own python compiler.

Hatch would be the "go to" tool for anyone wanting to develop programs in python, except for one thing, Hatch
does not handle python package management. In order to work with dependencies and other python packages, Hatch
provides two options, you can use pip or you can use UV, both have downsides. Pip does not handel complex
dependency resolution, which is a bummer. Hatch is supposed to fully support integration with uv, but from our
experience it doesn't, because uv does not reciprocate the integration. Regardless of what your settings are in
the pyproject file, uv wants the virtual environment to be located at `./.venv`, which is not where hatch wants 
to put it. 

The biggest downside to using hatch, is it does not configure the pyproject file for you. It does create
`pyproject.toml`, and it will fill out the basic structure of it, but it doesn't handle all of the
configuration, when it easily can.

So, to say the least, the jury is still out on Hatch. 

Basic Commands
--------------

A few basic commands.

```bash
# Init hatch
hatch init 
# Open a shell in the virtualenv
hatch shell
# Run a command in the virtual env
hatch run $COMMAND
# Find the path to the virtual env
hatch env sho
# Display dependencies
hatch dep
```

