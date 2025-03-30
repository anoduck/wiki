```text
#  _____ _            __  __             _           _
# |_   _| |__   ___  |  \/  | __ _  __ _(_) ___ __ _| |
#   | | | '_ \ / _ \ | |\/| |/ _` |/ _` | |/ __/ _` | |
#   | | | | | |  __/ | |  | | (_| | (_| | | (_| (_| | |
#   |_| |_| |_|\___| |_|  |_|\__,_|\__, |_|\___\__,_|_|
#                                  |___/
# __        __         _     _    ___   __
# \ \      / /__  _ __| | __| |  / _ \ / _|
#  \ \ /\ / / _ \| '__| |/ _` | | | | | |_
#   \ V  V / (_) | |  | | (_| | | |_| |  _|
#    \_/\_/ \___/|_|  |_|\__,_|  \___/|_|
#  _____ _ _        ____            _
# |  ___(_) | ___  / ___| _   _ ___| |_ ___ _ __ ___  ___
# | |_  | | |/ _ \ \___ \| | | / __| __/ _ \ '_ ` _ \/ __|
# |  _| | | |  __/  ___) | |_| \__ \ ||  __/ | | | | \__ \
# |_|   |_|_|\___| |____/ \__, |___/\__\___|_| |_| |_|___/
#                         |___/

⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀⠀⠀⠀⣄⣠⠆⠀
⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⠓⠒⢴⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢨⠀⣰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⢹⡀⠀⠀⠀⠈⠀
⠀⠀⠀⠀⢠⣀⣶⠀⠀⠀⠀⠀⠀⠀⠀⢤⢀⣀⣀⣀⡠⠋⠀⠀⢇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⣄⠊⠁⠀⠀⠀⠀⠀⢀⡨⢦⠀⠀⠀⠀⠀⠀⠀⠘⠒⠤⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠔⠊⠁⢀⡀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠼⠋
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠈⡀⠄⠂⠉⢀⡀⢰⠁⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀
⠀⠀⠀⠀⠀⠀⡠⢊⠠⠒⣁⠤⠐⣀⡁⠤⢤⠃⢀⣀⡠⢄⡀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⡠⡪⢐⡡⢐⠩⠐⠊⠁⠀⠀⠀⠚⠉⠉⠀⠀⠀⠙⠢⣀⡇⠀⠀⠀⠀
⠀⠀⢠⡪⡪⡲⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠃⠀⠀⠀⠀
⠀⣰⣿⠞⠉⠀⠀⠀⠀⠀⡄⡰⡆⠀⠀⠀⠀⠀⠀⢐⣌⡶⠀⠀⠀⠀⠀⠀⠀⠀
⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀
```

The Magical World of File Systems
=================================

A file system is a methodological construct that controls how a computational system stores and organizes information for access, reading, and writing.

As computers have evolved over the years there have been many different file systems. Some of which were
either very inefficient or very unstable. These have been discarded into the proverbial wastebin, but most are
still with us today. File systems are for the most part dependent on which type of medium the data is written
to. Other factors that determine the file system are things such as ram availability, on board memory, and
operating system.

File System Variety
-------------------

There are too many file systems to list all of them here, but we will gloss over a few of the more popular
ones. 

* ReiserFS - A journaling filesystem designed by Hans Reiser at Namesys. Has been removed from the linux
  kernel.
* btrfs - A Copy-on-write filesystem intended to address lack of support for pooling, snapshots, integrity
  checking, datascrubbing, and multidevice spanning in linux systems. It was originally designed by Ohad
  Rodeh, and has slowly grown in popularity.
* Ext4/Ext3/Ext2 - The staple journaling filesystem for Linux for many years. Still default for many OSs.
* 
