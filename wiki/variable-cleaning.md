```text
# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \
#   \ V / (_| | |  | | (_| | |_) | |  __/
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___|
#
#   ____ _                  _
#  / ___| | ___  __ _ _ __ (_)_ __   __ _
# | |   | |/ _ \/ _` | '_ \| | '_ \ / _` |
# | |___| |  __/ (_| | | | | | | | | (_| |
#  \____|_|\___|\__,_|_| |_|_|_| |_|\__, |
#                                   |___/
```

Variable Cleaning
=================

> Cleaning variables in order to maintain a small footprint.

Almost under every circumstance, removal of previously declared variables is both a waste of resources and a
waste of time. There are circumstances when this would be benefitial. For example, when the system running the
code has extremely limited resources, or maintaining an identical footprint to initialization is required.

garbage collection
------------------

In these circumstances it is usually best to allow Python to manage the removal of these variables with it's
garbage collection class. 

```python
import gc

gc.collect()
```

del keyword
------------

Python also provides the keyword `del`, which will disassociate a variable's identifier with it's meaning.
Note, this does not serve the same purpose as `gc` because the underlying data behind the identifier still
remains stored in memory. 

```python
my_pet = "dogs"

del my_pet
```

As noted, this does not delete "dogs", but disassociates it. You can use `gc.get_objects` to generate a list
of objects tracked by the garbage collection tracker.

