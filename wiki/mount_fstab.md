```text
#  __  __                   _                     _    __     _        _
# |  \/  | ___  _   _ _ __ | |_    __ _ _ __   __| |  / _|___| |_ __ _| |__
# | |\/| |/ _ \| | | | '_ \| __|  / _` | '_ \ / _` | | |_/ __| __/ _` | '_ \
# | |  | | (_) | |_| | | | | |_  | (_| | | | | (_| | |  _\__ \ || (_| | |_) |
# |_|  |_|\___/ \__,_|_| |_|\__|  \__,_|_| |_|\__,_| |_| |___/\__\__,_|_.__/
#
```

## Working with fstab to mount hard drives

Devices that are configured to be mounted on system boot are designated and managed in the `/etc/fstab` file.
So, if you desire to enable a device to be mounted on boot as well, you will need to modify this file. Doing
so requires a little knowledge about what you want to mount before hand. It is good to know the filesystem
that is contained on the device and the mount options that are needed to successfully mount the device.

### Mounting a NFS filesystem on boot with fstab

Several tutorials visited claimed the only options needed to mount an NFS file system were the defaults,
notated as `default`. I tended to disagree from experience. Network file systems should not be "locked" as at
somepoint they may become inaccessible to the rest of the network. The `tcp` flag also needed to be employed
to inform the kernel of the transfer protocol used to communicate with the device. Lastly, a timeout needed to
be added in case inaccessibility occurs, so the system is not constantly attempting to mount a device that is
not accessible.

```config
# DEV 											MNT POINT 	TYPE 	OPTIONS 																					? 	?
$IP_ADDRESS:/route/to/nfs 	/media/nfs 	nfs 	auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 	0 	0
```

You can mount it anywhere you desire, `/media/nfs` was simply used as an example. Be sure to replace "$IP_ADDRESS"
and "/route/to/nfs".

### Designating a persistent device name using udev in Linux (obviously)

To designate a persistent device name with udev, use the devices unique serial ID and add a rule to udev to
label that serial consistently and persistently every time it is mounted. Create a new udev rule if it does
not already exist and name it `/etc/udev/rules.d/69-disk.rules`.

```config
ACTION=="add", KERNEL=="sd[a-z]", ENV{ID_SERIAL_SHORT}=="X5ER1ALX", RUN+="/path/to/script /dev/%k"
```

### Using other identifiers to consistently setup device mounts using fstab

Most modern operating systems have done away with using device names in the fstab file for security purposes,
they now use the devices UUID that is assigned to it upon boot or connection. This way the device is
universally recognized as unique, and the name of the device is still concealed from malicious on lookers.
But, this is not the only way of identifying a device uniquely, there are also partition labels. Below we will
discuss using both.

#### Use partition label to setup persistent mounts with fstab

If one so chooses they can use the partition label to mount devices upon system boot persistently. To acquire
the partition label use `lsblk -dno LABEL /dev/sda0`, then add the following line to your fstab.

*NOTE:* This method is not reccommended.

```config
PARTLABEL=MY_LABEL 	/media/disk1 	ext4 	defaults 	0 	0
```

#### Use UUID to setup persistent device mounts the correct way.

As previously mentioned the reccommended and modern way to setup persistent mounting of a device on boot is by
using the devices uuid. You can discover the uuid of the device by using the following command: `lsblk -dno UUID /dev/sda0`.
Once the UUID has been acquired, one can simply add it to fstab with the following line.

*NOTICE:* File System UUIDs are distinctively different from GPT partition UUIDs. GPT partition UUIDs are
reserved from GPT partitions, the two are not interchangeable or compatible.

```config
UUID=570c31b7-837c-4c22-9971-02f76d5d2664 	/media/disk1 	ext4 	defaults 	0 	0
```
