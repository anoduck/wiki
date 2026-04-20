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

> [!info] Undoubtedly you will be disappointed with this page. Simply because it does not even begin to
> scratch the surface of the topic at hand.

The purpose of this post is to provide a general overview of different file systems. It is in no way
comprehensive, and is not even a good effort towards including the high points.

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
* UFS & FFS - OpenBSD's native file system, and it's derivative the Free File System, used in OpenBSD.
* XFS - Is the original file system of Silicon Graphics IRIX OS, and it still holds it's own. Known for it's
  incredibly fast IO. 
* FAT - The File Allocation Table is the default file system for DOS, and still is ridiculously
  popular today. It is often used for removable media such as USB flash drives and sdcards. FAT has seen a
  resurgence in use due to being implemented as an internal part of the EFI system partition.
* exFAT - Is loosely based on FAT, but is incompatible with FAT. It's benefit over fat is it allows exceeding
  the 4GB file size limitation of FAT. 
* NTFS - NTFS was the default file system for microsoft products for several years. Frankly, I have seen cold
  chills run through computational engineers when someone mentioned NTFS. So, we try not to discuss it.
* ZFS - ZFS was the default file system for the Solaris Operating system, and opinionatedly it was way ahead
  of it's time. 
