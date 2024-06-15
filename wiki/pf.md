```text
#  ____  _____
# |  _ \|  ___|
# | |_) | |_
# |  __/|  _|
# |_|   |_|
#
```

PF: Packet Filter
==================

Forward
--------

A word of warning. Understanding the nuances of your operating system is critical in the proper configuration
of PF. Although PF grew out of the OpenBSD project, it is implemented in nearly, if not all, of the BSD's. I
imagine it could be implemented in OpenIndiana as well, and might be mistaken, but vaguely remember seeing a
blip that referenced it's use on Haiku. Funny as it is, the beg three are some of the few operating systems
which are not capable of running PF, due to their kernel limitations.

What might work in a FreeBSD implementation, might not work in the OpenBSD implementation, so please take this
into consideration.

The purpose of this wiki entry is to clarify the meaning of keywords in configuration of PF, and provide a
"only slightly better than average" pf implementation. So without further ado, here is pf.

### Keywords

| keyword   | type         | meaning                                                  | example |
| -------   | ----         | -------                                                  | ------- |
| pass      | Action       | pass the packet to the kernel for processing             |         |
| block     | Action       | Either drops or returns the packet                       |         |
| drop      | block policy | Drops the packets immediately / ignores it               |         |
| return    | block policy | Returns the packet to the source.                        |         |
| in        | Direction    |                                                          |         |
| out       | Direction    |                                                          |         |
| log       | Parameter    | Initiates state dependent logging of packet              |         |
| quick     | Parameter    | perform action and do not attempt to match further rules |         |
| interface | device       | Preceeded by "on" keyword.                               |         |
| egress    | device       | Group of interfaces that possess a the default route     |         |

### Example



### Reference Material
