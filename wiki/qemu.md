```text
#   ___
#  / _ \  ___ _ __ ___  _   _
# | | | |/ _ \ '_ ` _ \| | | |
# | |_| |  __/ | | | | | |_| |
#  \__\_\\___|_| |_| |_|\__,_|
#
```

Qemu
----

Qemu is a flexible lightweight full virtualization solution that allows the user to emulate a wide variety of
different hardware architectures and can emulate an infinite variety of operating systems. By itself, qemu
lacks the same performance as other virtualization solutions, but does interactwith and take advantage of the
hypervisor of these other solutions, which when combined will provide comparable performance results.

### FreeBSD on Qemu

Just writing this from shear memory as I do it, so if you have problems let me know. 

Even with kvm enabled, FreeBSD's performance is significantly less 

#### Installing the image.

1. Virtual machine images are available from [FreeBSD's website](https://download.freebsd.org/ftp/releases/VM-IMAGES/13.2-RELEASE/amd64/Latest/). They come in three formats; qcow2, vhd, and vmdk.
For working with qemu you will want to download the qcow2 image. Once downloaded you will need to extract it.

```bash
xz -d FreeBSD(...).qcow2.xz
```

1. Next, you will need to create a "backing file" for your image. If you fail to do this, all freespace left
   in the virutal image will be consumed within a matter of minutes on your virtual disk image. "Backing Files" are
   often referred to as overlay images. They write changes made to the original image, and it's
   current state. It is a handy feature, because it keeps the original image in a pristine state, and allows
   the creation of a disposable environment if needed. 
   ```bash
   qemu-img create -f qcow2 -o backing_file="$ORIGINAL_IMAGE",format=qcow2 "$NEW_FILE".qcow2 
   ```
2. Now you can start your virtual macine instance in a graphical environment. Personally, because of the
   loftiness of the command, I always create a one line script to make it easier to execute in the future.
```bash
service netif restart
service sshd start
```

#### Reference Material

1. [qemu wiki](https://wiki.qemu.org/Hosts/BSD)
2. [The qemu book](https://en.wikibooks.org/wiki/QEMU/Images)
3. [Qemu's Documentation](https://qemu.weilnetz.de/doc/6.0/)


