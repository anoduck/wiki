```text
#  _   _ _____ ____
# | \ | |  ___/ ___|
# |  \| | |_  \___ \
# | |\  |  _|  ___) |
# |_| \_|_|   |____/
#
```

Setting up an NFS Server
========================

NFS stands for Network File System, and it is a way to share a portion or the entire file system across
multiple systems. In linux, NFS comes in two varieties, a kernel base variety and a user based one. As one
could easily deduce, the kernel based server uses a kernel module to provide network accessiblility to the
shared system. Where the user based system relies on a system service to provide the same functionality. Both
have benefits and risks. While the kernel variety is faster, it also poses greater risks to security.
Regardless, most of the time, the kernel variety is what is desired.

Quick how-to on the NFS server
-------------------------------

Lacking the time to elaborate on the eccentricities on how to properly configure and run the service, we shall
go through a quick crash course on the subject.

### Check for kernel support

Only included in the official Debian wiki, is the step to first ensure that your kernel supports nfs. To do so
run the command below, and check to make sure at least two implementations are listed.

```bash
grep NFSD /boot/config-`uname -r`
```

If you see two lines uncommented, then you are good to go.

### Install the software

First things first, install the software. 

```bash
sudo apt install nfs-common nfs-kernel-server
```

### Support for V3

> [!note] Support for V3
> More than likely your NFS client will support V4, and V3 support will not be required.

If you are planning to run version 3 of this protocol, then you will need to install an additional package
`rpcbind`. and configure it for use.

```bash
sudo apt install rpcbind
```

By default, rpcbind only listens for connections on `127.0.0.1`, so in order to share your NFS share with your
local network you will be required to change this. Furthermore, you will need to modify the `hosts.allow`
file. Below demonstrates how to do this.

```bash
 $ perl -pi -e 's/^OPTIONS/#OPTIONS/' /etc/default/rpcbind
 $ echo "rpcbind: 192.168.1." >> /etc/hosts.allow
 $ systemctl restart rpcbind.service
```

### Setup `/etc/exports`

The file `/etc/exports` or set of files located in `/etc/exports.d/*` is used by the NFS server to acquire
which folders should be shared with the network. The syntax is very basic, and only requires three parameters;
folder location, client(s) address(or network), and mount options. This file usually comes with examples
provided as comments, but for the sake of learning an example can be found below.

```bash
/some/random/mount/point    192.168.1.1(rw)
```

Which tells nfsd to share the folder at `/some/random/mount/point` with the client on `192.168.1.1` and allow
both reading and writing. if you wanted to share that folder with the entire network, the second parameter
would have been something like `192.168.1.0/24(rw)`. Notice the definition of the subnet.

### Disable support for V3

If you plan on only running V4, then you will want to harden the NFS server by disabling it and it's services.
This first involves editing two files `/etc/default/nfs-common` and `/etc/default/nfs-kernel-server`.

We will begin with `/etc/default/nfs-common`.

#### Disabling statd and idmapd

Open up `/etc/default/nfs-common` and set the values for statd and imapd as follows.

```conf
NEED_STATD="no"
NEED_IDMAPD="yes"
```

#### Disabled V2 and V3 on the kernel

The file you will want to edit is `/etc/default/nfs-kernel-server`. You will need to add these lines to the
file as they are not included by default. Adding the `-H $IPADDRESS` option informs the server to only listen
on one ipaddress rather than all.

```conf
RPCNFSDOPTS="-N 2 -N 3 -H 10.0.1.1"
RPCMOUNTDOPTS="--manage-gids -N 2 -N 3"
```

#### Mask the rpcbind service

Since only version three requires the use of the `rpcbind.service` you will want to disable it, and it's
socket service.

```bash
sudo systemctl mask rpcbind.service
sudo systemctl mask rpcbind.socket
```

### Creating facade mount points

Nearly ever tutorial out there suggests one take the extra precautionary measure of setting up what is
referred to as "shares" or as "pseudo file system mount points", whatever they are called, they are the same
thing. These mount points are used to prevent malicious users from acquiring access to parts of the system
they are not supposed to have access to. Which is because NFS is run by the root user, and therefore can be
exploited. (Basically not time to explain.)

#### Make the file system tree

Create the needed directories, change ownership of that tree, and perform a mount.

```bash
sudo mkdir -p /var/nfs/share
# You can create two directories at once with brackets.
sudo mkdir -p /var/nfs/share/{mount1,mount2}
sudo chown -R nobody:nobody /var/nfs/share
sudo mount --bind /path/to/mount1 /var/nfs/share/mount1
sudo mount --bind /path/to/mount2 /var/nfs/share/mount2
```

Check to see that everything worked with `sudo df -ah`.

#### Make your pseudo mount points permanent.

Open up `/etc/fstab` and add the mount points to the file. Like so:

```conf
/path/to/mount1 /var/nfs/share/mount1   none bind
/path/to/mount2 /var/nfs/share/mount2   none bind
```

#### Modify your `/etc/exports` file to enforce this change.

Then open up your text editor and change `/etc/exports` to where it reflects these changes.

```bash 
/var/nfs/share   192.168.10.0/255.255.255.0(rw,sync,no_root_squash,no_subtree_check,crossmnt,fsid=0)
```

Below are some NFS options used for this case:

>rw : allow read and write access for both NFS server and client to the volume/directory.
>sync: This option forces NFS to write changes to disk before replying. This results in a more stable and consistent 
environment since the reply reflects the actual state of the remote volume. However, it also reduces the speed of file operations.
>no_subtree_check : disables subtree checking, which has mild security implications, but can improve reliability in some circumstances.
>no_root_sqash : disable root squashing. This option is mainly useful for disk-less clients.
>fsid=0 : for NFSv4, this parameter is used to inform the NFS server that this export is the root of all exported filesystems.

When done, and the server is running. You should be able to confirm these changes with `sudo showmount -e`

### Setting up fstab for NFS client

Once everything is up and running, you probably do not want to mount the nfs volume manually each time. So,
you can set up fstab to mount the NFS volume automatically on boot with the rest of the filesystem.

```conf
host_ip:/var/nfs/general    /nfs/general   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
host_ip:/home               /nfs/home      nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
```
