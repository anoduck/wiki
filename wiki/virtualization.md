```text
# __     ___      _               _ _          _   _
# \ \   / (_)_ __| |_ _   _  __ _| (_)______ _| |_(_) ___  _ __
#  \ \ / /| | '__| __| | | |/ _` | | |_  / _` | __| |/ _ \| '_ \
#   \ V / | | |  | |_| |_| | (_| | | |/ / (_| | |_| | (_) | | | |
#    \_/  |_|_|   \__|\__,_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
#
```

## Virtualization

### FreeBSD as guest in Virtualbox

#### Vbox Additions Installation Options

You have two options.

1. Build from the ports tree. This comes from the FreeBSD documentation.
2. Install with pkg. This comes from the FreeBSD foundation wiki, and is reccommended by me.

It will take several hours to compile the guest additions AND all the required dependencies. For one of my
instances then resulted in exhausted memory. Where, installing from a package will take only a few (<5)
minutes.

##### Using the ports tree.

Get the ports tree.
```sh
portsnap auto
```

```sh
cd /usr/ports/emulators/virtualbox-ose-additions && make install clean
```

At this point you should expect it to take over eight hours to complete.

__If or when complete, do not reboot. There is more work to be done.__

##### Using pkg

```sh
pkg install emaulators/virtualbox-ose-additions
```

__Same as above. Once complete move on to the configuration.__

#### Configure FreeBSD to use the 

Then enable the guest additions by editing the `/etc/rc.conf` file with vi. Add the two lines below to it at
the end.

```sh
vboxguest_enable="YES"
vboxservice_enable="YES"
```

Make FreeBSD use the vbox graphics driver by creating the `/etc/X11/xorg.conf` file, and place both blocks
of code for the graphics driver AND the mouse driver in it.

```conf
Section "Device"
	Identifier "Card0"
	Driver "vboxvideo"
	VendorName "InnoTek Systemberatung GmbH"
	BoardName "VirtualBox Graphics Adapter"
EndSection
```

Configure the mouse for use.

```conf
Section "InputDevice"
	Identifier "Mouse0"
	Driver "vboxmouse"
EndSection
```

At this point, you should power off the sytem.

```sh
poweroff
```

Once the computer is powered down, open virtualbox settings and change the graphics controller to "VBoxSVGA".
Then power back on the machine.

#### configure the host for folder sharing.

```bash
vboxmanage sharedfolder add 'BSDBox' --name myshare --hostpath /mnt/bsdboxshare
```

Mount the shared folder on FreeBSD.

```sh
mount_vboxvfs -w myshare /mnt
```

After this is done, you may now go to setting up whatever you want for your installation.

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
   #!/usr/bin/env bash
   sudo qemu-system-x86_64 -m 2048 \
   -hda "$NEW_FILE".qcow2 -enable_kvm \
   -netdev user,id=mynet0,hostfwd=tcp:0.0.0.0:7722-:22 \
   -device e1000,netdev=mynet0
   ```
3. You should have your fresh installation running. The first thing to do is to enable sshd and configure it,
   so you no longer need the graphical environment to access the machine. This is done by adding a few lines
   to `/etc/rc.conf` listed below, and enabling root login for the root user.
   ```bash
   # open vi with
   vi /etc/rc.conf
   # next add these two lines
   sshd_enable="YES"
   ifconfig_em0="DHCP"
   # save the file and exist with:
   :wq
   # Then allow root login in sshd by opening /etc/ssh/sshd_config in vi.
   vi /etc/ssh/sshd_config
   #look for the line below and uncomment it.
   PermitRootLogin prohibit-password
   # This tells ssh to allow root login as long as a password is used.
   ```
4. Then restart system services
```bash
service netif restart
service sshd start
```

#### Reference Material

1. [qemu wiki](https://wiki.qemu.org/Hosts/BSD)
2. [The qemu book](https://en.wikibooks.org/wiki/QEMU/Images)
3. [Qemu's Documentation](https://qemu.weilnetz.de/doc/6.0/)


