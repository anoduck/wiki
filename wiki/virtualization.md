```text
# __     ___      _               _ _          _   _
# \ \   / (_)_ __| |_ _   _  __ _| (_)______ _| |_(_) ___  _ __
#  \ \ / /| | '__| __| | | |/ _` | | |_  / _` | __| |/ _ \| '_ \
#   \ V / | | |  | |_| |_| | (_| | | |/ / (_| | |_| | (_) | | | |
#    \_/  |_|_|   \__|\__,_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
#
```

## Virtualization

### Podman

Podman is an open source alternative to Docker (which is free, but closed) for virtual containers. It appears
to be backed by Red Hat, which we are pleased to see has not died off yet. Podman is supposed to be a straight
drop-in replacement for docker and docker-compose, and although it is pretty damn close, it isn't exactly the
clean fit. This is cool, because along with being a pretty close drop-in, podman also comes with some extra
features that were not presently available with docker, or at least in a manner we are familiar with. Some of
podman's parts are actually wrappers around docker programs, so keep this in mind if you plan on exploring it
more.

#### Podman Toolbox

Podman toolbox is a really neat tool that allows users to create rootless containers to run terminal
applications inside. 

#### Podman Containers

Primarily podman is intended to be used to manage virtual containers, and this is what it does best. Although,
there will several things that are unique to podman that could possibly trip up an unfamiliar user.

#### Podman Machine 

If your running linux, podman can be used as more than just a substitute for docker, it can be used to manage
qemu containers as well. The benefit one recieves from using podman in this manner is access to peripheral
devices that are not normally accessible to docker images. The default image used for doing this is
fedora-core, but podman can be configured to use other OCI images. 

##### Podman Machine Init

To use this feature, simply initialize a new podman machine with:

```bash
podman machine init
```

Do not use sudo for this, as podman machines are not intended to be run as root ever. 

##### Podman Machine Post Init

In order for podman machine to run, the user will need to perform a few extra steps. 

1. Run `ls /usr/libexec/podman` and take note of the binary executables listed. There should be three symbolic
   links to binary executables; catatonit, conmon, and gvproxy. There should also be two binary files; quadlet
   and rootlessport.
2. If you see these five files, you can move on. If you don't see these five files, you have a few more quick
   steps to perform.
3. For each missing file, you need to check and see if you already have it installed on your system. This can
   usually be performed using `which $MISSING_FILE_GOES_HERE`, for example `which gvproxy`. This command will
   check if the file is in your path, and it should be. If this does not work and you have mlocate installed,
   you could run `sudo updatedb && locate $MISSING_FILE_GOES_HERE`.
4. If you are unable to locate the file, then install it from your package manager and proceed to the next
   step. `sudo apt install $MISSING_FILE_GOES_HERE`
5. Afterward, you should then create a symbolic link from where the file is installed into `/usr/libexec/podman`.
   This can be done quickly with `sudo ln -sf $(which $MISSING_FILE_GOES_HERE) /usr/libexec/podman/$MISSING_FILE_GOES_HERE`.
6. Once this is done, and you have all the files inside the podman dir. You should be good to go.

##### Podman Machine Set 

If you would like to add a USB device along with this new image you can use:

```bash
podman machine set --usb vendor=XXX,product=XXX
# OR
podman machine set --usb bus=XXX,devnum=XXX
```

Using bus and id are also accepted for these values, although they will change if the device is moved to a
different usb port or another usb is removed.

If you need your podman machine to have root permissions, you can run: `podman machine set --rootful`.

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
service netif restart
service sshd start
```

#### Reference Material

1. [qemu wiki](https://wiki.qemu.org/Hosts/BSD)
2. [The qemu book](https://en.wikibooks.org/wiki/QEMU/Images)
3. [Qemu's Documentation](https://qemu.weilnetz.de/doc/6.0/)


