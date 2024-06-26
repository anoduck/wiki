```text
# __     ___      _               _ ____
# \ \   / (_)_ __| |_ _   _  __ _| | __ )  _____  __
#  \ \ / /| | '__| __| | | |/ _` | |  _ \ / _ \ \/ /
#   \ V / | | |  | |_| |_| | (_| | | |_) | (_) >  <
#    \_/  |_|_|   \__|\__,_|\__,_|_|____/ \___/_/\_\
#
```

VirtualBox
-----------

VirtualBox is a virtualization solution that came out of the no longer existent Sun Microsystem corporation,
and it was originally promoted as being a full virutalization solution built on top of the Java virtual
machine. After the subsequent collapse of Sun, VirtualBox (referred to often as just vbox) became property of
Novell Systems, then was later bought out by Novells progenator Oracle Systems, and finally obtained by the
Apache foundation. At first the platform was was written for use with only temporary instances of virtual
machines, but now allows the ability to run headless virtual machine instances full time.

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

