```text
#  ____        _ _     _   ____            _
# | __ ) _   _(_) | __| | |  _ \ _ __ ___ | |__  ___
# |  _ \| | | | | |/ _` | | |_) | '__/ _ \| '_ \/ __|
# | |_) | |_| | | | (_| | |  __/| | | (_) | |_) \__ \
# |____/ \__,_|_|_|\__,_| |_|   |_|  \___/|_.__/|___/
#
```

## Common Issues Building in OpenBSD

_** This List is in no way, shape or form exhaustive or comprehensive. **_

1. `/usr/local/includes` -- The hierarchy of OpenBSD is different than most Linux distributions and FreeBSD.
   Not only is the includes folder located int `/usr/local`, but it's contents vary as well. Libraries
   often found in the `/usr/local/lib` folder may be moved to the includes directory. 
2. Gmake not Make -- OpenBSD does not use gnumake, but gnumake is available for installation as a pkg and/or
   is located in the ports tree. So, if make does not work, try gmake.
3. Egcc not gcc AND Eg++ not g++ -- In a similar fashion to gnumake, OpenBSD does not use the Gnu C or Gnu C++
   libraries. Rather, it uses Clang as it's default compiler. Gcc and g++ are still available for installation
   though, but they have been renamed to 'egcc' and 'gcc'. ALSO, for future reference, 'gdb' has been renamed
   to 'egdb' as well. `export CC=/usr/local/bin/egcc CXX=/usr/local/bin/eg++`
4. Kernel File monitoring -- The OpenBSD kernel does not allow watching individual files for changes, rather
   it only allows monitoring directories for changes. Which is why it is not compatible with services such as
   the dropbox client. 
5. Permission issues -- for languages such as cargo and at one time go, the use of sudo or doas is required as
   the libraries for those languages lies beyond the user's userspace.
6. Qt dilemna -- compiling anything with qt can be somewhat problematic. This is due to the includes folder.
   So keep this in mind and if trouble is encountered, designate the folder manually.
7. Gcc versioning -- Currently, libraries such as lablas and boost require version 9 of gcc. This is because
   of an issue with getting llvm to work with gcc 11. Unfortunately, applications such as the lua language
   server require the use of gcc 11.

