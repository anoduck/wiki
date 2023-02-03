```text
#  ___ ____   ___     ____
# |_ _/ ___| / _ \   / ___| __ _ _ __ ___   ___  ___
#  | |\___ \| | | | | |  _ / _` | '_ ` _ \ / _ \/ __|
#  | | ___) | |_| | | |_| | (_| | | | | | |  __/\__ \
# |___|____/ \___/   \____|\__,_|_| |_| |_|\___||___/
#
```

## Working with ISOs

The usual commands needed to work with ISO images are different in OpenBSD than they are in Linux. So, keeping
this in mind, let's go over some basic iso commands.

### Writing an iso to disc

To write an iso to file, you use the `cdio` command, which is much simplier than the `dd` command in linux.
Simply use `cdio` followed by `tao`, then the image you wish to write to disc. So when writing an iso to disc,
think of the TAO.

```bash
cdio tao install.iso
```

### Mount an iso image

This one is less commonly used, and quite different from Linux. In linux you simply would mount the iso image
on loop and mount it to a node. On OpenBSD on the other hand, you have to configure a pseudo disk device
first, and then use `mount_cd9660` to mount the disc image. As you can see there is no "loop" involved. Once
you are ready to umount, you unmount as usual, AND you have to remove the pseudo device.

```bash
# To Mount
vnconfig vnd0 /path/to/iso/file.iso
mount_cd9660 /dev/vnd0c /mnt/cdrom

# To unmount
umount /mnt/cdrom/
vnconfig -u vnd0
```
