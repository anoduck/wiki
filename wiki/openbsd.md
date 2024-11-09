```text
#   ___                   ____ ____  ____
#  / _ \ _ __   ___ _ __ | __ ) ___||  _ \
# | | | | '_ \ / _ \ '_ \|  _ \___ \| | | |
# | |_| | |_) |  __/ | | | |_) |__) | |_| |
#  \___/| .__/ \___|_| |_|____/____/|____/
#       |_|
#
```

OpenBSD Specific Topics
-----------------------

These are Topics that are specific to the OpenBSD operating system.

| [Partitioning in OpenBSD](OpenBSD_Partitioning) | [Virtualization in OpenBSD](vmm)    | [Working with ISOs](openbsd-iso)     | [restoring ldconfig](ldconfig) |
| [OpenVPN on OpenBSD](open-openvpn)              | [Common Build Issues](build-issues) | [Networking on OpenBSD](openbsd-net) | [Configuring pfstatd](pfstatd) |
| [Wireguard on OpenBSD](openbsd-wireguard)       | [OpenBSD net routes](openbsd-route) | [OpenBSD HTTPD](openbsd-httpd)       | [PF](pf)                       |
| [Kernel Tweaks](kern-tweaks)                    |                                     |                                      |                                |

### Tips

Below are some tips and pointers for the brave. Learned from the experience of living life with OpenBSD.

#### Bad Major / Minor Too Small

If or when you decide to run an OpenBSD system, you are given two options, you can either run the most recent
release or you can follow the development version labeled as "snapshot". In either case, while attempting to
install a package from the package repository you may come across the following error message:

```bash
Can't install zstd-1.5.6 because of libraries
|library z.7.1 not found
| /usr/lib/libz.so.5.0 (system): bad major
| /usr/lib/libz.so.6.0 (system): bad major
| /usr/lib/libz.so.6.1 (system): bad major
| /usr/lib/libz.so.7.0 (system): minor is too small
```

What this means is the package you are attempting to install is looking for a library with a version number
higher than what is available of your system. Specifically the message "minor is too small", denotes this. 

Once you have encountered this error you have two options, you can either upgrade your current system or you
can ONLY TEMPORARILY attempt to bypass this restriction. Although it is advised you upgrade your system as
soon as possible, this may not always be convenient or even an option. It is in these latter situations
performing a restriction bypass is appropriate. By performing a restriction bypass, you are basically hoping
the program is backwards compatible and will accept it. To bypass the restriction simple locate the most
recent version of the library in question on your system that is the closest to what package is looking for.
In the above example version 7.0 is used, because the missing library is version 7.1. Then simply create a
symbolic link from what is available to what the package wants. 

```bash
ln -sf /usr/lib/libz.so.7.0 /usr/lib/libz.so.7.1
```

Once performed, retry the installation.

### Links

- [OpenBSD Handbook](https://www.openbsdhandbook.com/)
- [OpenBSD FAQ](https://openbsd.org/faq) <-- Most of life's answers are found here.
- [Great tutorial on pf configuration](https://www.digitalocean.com/community/tutorials/how-to-configure-packet-filter-pf-on-freebsd-12-1)
