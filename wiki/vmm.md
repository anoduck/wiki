``` text
# __     ____  __ __  __
# \ \   / /  \/  |  \/  |
#  \ \ / /| |\/| | |\/| |
#   \ V / | |  | | |  | |
#    \_/  |_|  |_|_|  |_|
#
```

Virtual Machine Manager
========================

VMM is the virtualization platform for the OpenBSD OS platform. For years the only virtualization solution for
OpenBSD systems was Qemu without KVM acceleration. This meant virtual machines were painfully slow to use, and
very limited by resources. It took several years before a solution for virtualization on OpenBSD systems was
created, and by then virtualization had become an old hat. Comparatively, VMM is still in its infancy, and
still does not provide graphical support for desktop environments. There is also confusion over how to
properly configure networking to allow virtual machine instances to access an external network. This confusion
comes from the active development status of the VMM solution. Perhaps one day, the mysteries of this method
will be further ironed out. (Whatever the fuck that means.)

Primer on OpenBSD VM Creation
------------------------------

At the timer of writing this, VMM only supports Linux and BSD systems, and there is no graphical
functionality. Before beginning creation of a virtual machine be sure to enable port forwarding on your
system. Then enable the virtual machine daemon using `sudo rcctl enable vmd && sudo rcctl start vmd`.


### References

- https://xosc.org/vmm.html
- https://blog.strus.guru/2021/10/containerized-development-environment-on-openbsd-with-podman/
- http://www.h-i-r.net/2017/04/openbsd-vmm-hypervisor-part-2.html
- https://giocher.com/words/2018/ubuntu-on-openbsd-vmm/
