```text
# __     ___      _               _ _          _   _
# \ \   / (_)_ __| |_ _   _  __ _| (_)______ _| |_(_) ___  _ __
#  \ \ / /| | '__| __| | | |/ _` | | |_  / _` | __| |/ _ \| '_ \
#   \ V / | | |  | |_| |_| | (_| | | |/ / (_| | |_| | (_) | | | |
#    \_/  |_|_|   \__|\__,_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
#
```

## Virtualization

### Virtualbox

#### FreeBSD as guest in Virtualbox

Get the ports tree.

```sh
cd /usr/ports/emulators/virtualbox-ose-additions && make install clean
```

Then enable the guest additions.

```sh
vboxguest_enable="YES"
vboxservice_enable="YES"
```

Make FreeBSD use the vbox graphics driver. edit `/etc/X11/xorg.conf`

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

configure the host for folder sharing.

```bash
vboxmanage sharedfolder add 'BSDBox' --name myshare --hostpath /mnt/bsdboxshare
```

Mount the shared folder on FreeBSD.

```sh
mount_vboxvfs -w myshare /mnt
```
