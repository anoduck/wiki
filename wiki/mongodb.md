```text
#  __  __                         ____  ____
# |  \/  | ___  _ __   __ _  ___ |  _ \| __ )
# | |\/| |/ _ \| '_ \ / _` |/ _ \| | | |  _ \
# | |  | | (_) | | | | (_| | (_) | |_| | |_) |
# |_|  |_|\___/|_| |_|\__, |\___/|____/|____/
#                     |___/
#
```

MongoDB
--------

> [!INFO]
> MongoDB does not supported by OpenBSD, and does not support x86_64 architectures without AVX.

There is not much that can be added to the above, due to the above. Of all the Non-SQL databases, MongoDB has
been reported as the easiest to work with, and from discussions with other developers, it appears that
backwards compatibility of syntax is one of it's strongest points. From personal appearence, looking at it
from a different viewpoint, MongoDB possesses an unusually heavy footprint, and places a considerable load on
the system.

There is a rogue wildcat distribution that has been altered to be compatible with x86_64 architectures without
AVX support. It achieves this by using a docker container with an aged debian release. [It can be found
here](https://github.com/GermanAizek/mongodb-without-avx)
