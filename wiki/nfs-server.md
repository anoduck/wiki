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
multiple systems. For those interested, NFS is a product of the famed Sun Microsystems (RIP), and was
developed in 1984. 

In linux, NFS comes in two varieties, a kernel base variety and a user based one. As one
could easily deduce, the kernel based server uses a kernel module to provide network accessiblility to the
shared system. Where the user based system relies on a system service to provide the same functionality. Both
have benefits and risks. While the kernel variety is faster, it also poses greater risks to security.
Regardless, most of the time, the kernel variety is what is desired.

Setting up a NFS server
-------------------------------

This set of instructions was intended to be a quick "how-to", but due to recent changes in how the service is
configured for debian derivative distrobutions, it turned into anything but brief. 

At the time of writing, Summer 2025, nearly every article of official documentation concerning setup of the
nfs-kernel-server had not been updated to reflect the new changes. This of course, complicated things
exponentially.

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
sudo apt install nfs-kernel-server 
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


### Support for V3

This is what we will primarily concern ourselves with.

> [!note] Support for V3
> More than likely your NFS client will support V4, and V3 support will not be required.

> [!warning] OpenBSD Requires V3
> For those badasses out there ruling the world with OpenBSD, V4 is not supported, so you will be required to
> keep V3 enabled. Sorry about that, but success comes with many sacrifices.

#### Setup rpcbind

If you are planning to run version 3 of this protocol, then you will need to install an additional package
`rpcbind`. and configure it for use.

```bash
sudo apt install rpcbind
```

##### configure rpcbind

By default, rpcbind only listens for connections on `127.0.0.1`, so in order to share your NFS share with your
local network you will be required to change this. Furthermore, you will need to modify the `hosts.allow`
file.

There are three different ways to modify the rpcbind configuration file. Choose one.

1. As part of a command line perl script: `perl -pi -e 's/^OPTIONS/#OPTIONS/' /etc/default/rpcbind`

2. Using sed: `sudo sed -i 's/OPTIONS/#OPTIONS/g' /etc/default/rpcbind`

3. By hand with a text editor: Simply open the file in an editor and comment out all the lines.

Now add the following line to your `hosts.allow` file and restart the service.

```bash
echo "rpcbind: 192.168.1." >> /etc/hosts.allow
systemctl restart rpcbind.service
```

### Setup `/etc/exports`

The file `/etc/exports` or set of files located in `/etc/exports.d/*` is used by the NFS server to acquire
which folders should be shared with the network. The syntax is very basic, and only requires three parameters;
folder location, client(s) address(or network), and mount options. This file usually comes with examples
provided as comments, but for the sake of learning an example can be found below.

```bash
/some/random/mount/point    192.168.1.1(sync,wdelay,crossmnt,no_subtree_check,sec=sys,rw,insecure,no_root_squash,no_all_squash)
/var/nfs/share   192.168.10.0/255.255.255.0(rw,sync,no_root_squash,no_subtree_check,crossmnt,fsid=0)
```

Which tells nfsd to share the folder at `/some/random/mount/point` with the client on `192.168.1.1`. If you wanted
to share that folder with the entire network, the second parameter would have been something like 
`192.168.1.0/24(sync,wdelay,crossmnt,insecure,rw, etc...)`. Notice the definition of the subnet.

Below are some NFS options used for this case:

- rw : allow read and write access for both NFS server and client to the volume/directory.
- sync: This option forces NFS to write changes to disk before replying. This results in a more stable and consistent environment since the reply reflects the actual state of the remote volume. However, it also reduces the speed of file operations.
- no_subtree_check : disables subtree checking, which has mild security implications, but can improve reliability in some circumstances.
- no_root_sqash : disable root squashing. This option is mainly useful for disk-less clients.
- fsid=0 : for NFSv4, this parameter is used to inform the NFS server that this export is the root of all exported filesystems.

When done restart or start the rpcbind service.

### Modify the configuration file

Before summer of 2025, to configure the server you would have modified two files `/etc/default/nfs-common` and 
`/etc/default/nfs-kernel-server`. Now, this is no longer the case. All configuration should take place in
either the primary server configuration file `/etc/nfs.conf` or in a localized configuration file located
in the configuration file directory at `/etc/nfs.conf.d`. As a matter of server administration "best practices"
the latter of these choices is preferred.

To save time, one could simply copy an example configuration file from
`/usr/share/nfs-commmon/conffiles/nfs.conf` to the localized configuration directory `/etc/nfs.conf.d/`, or
simply copy and paste the example provided below.

```ini
[lockd]
port=32768
udp-port=32768
[mountd]
udp=no
port=32767
[nfsd]
udp=n
tcp=y
vers2=n
vers3=y
vers4=n
vers4.0=n
vers4.1=n
vers4.2=n
[statd]
port=32765
outgoing-port=32766
```

### Mask unused services

You will want to disable and mask unused parts of the NFS service to prevent them from being started by other
services.

#### mask rpcbind if not running version3

Since only version three requires the use of the `rpcbind.service` you will want to disable it, and it's
socket service.

```bash
sudo systemctl mask rpcbind.service
sudo systemctl mask rpcbind.socket
```

#### mask and disable unused services for version4

If you only want to run version three (v3), then you will want to mask these services that are only used on
version 4.

```bash
# nfs-idmapd
systemctl disable nfs-idmapd.service
systemctl mask nfs-idmapd.service
systemct stop nfs-idmapd.service

# nfs-blkmap
systemctl disable nfs-blkmap.service
systemct stop nfs-blkmap.service
```

### Add service ports to `/etc/services`

The `/etc/services` file primarily is used by the system to reference what services are running on what ports.
This file is then used by iptables to provide definitions for firewall rules. At the end of this file is a
location for your local additions. You will want to provide the definitions for your nfs service ports here.

```conf
# Local services

#
# RPC/NFS ports
# Listing here does not mean they will bind to these ports.
#
rpc.statd-bc    32765/tcp                       # RPC statd broadcast
rpc.statd-bc    32765/udp                       # RPC statd broadcast
rpc.statd       32766/tcp                       # RPC statd listen
rpc.statd       32766/udp                       # RPC statd listen
rpc.mountd      32767/tcp                       # RPC mountd
rpc.mountd      32767/udp                       # RPC mountd
rpc.lockd       32768/tcp                       # RPC lockd/nlockmgr
rpc.lockd       32768/udp                       # RPC lockd/nlockmgr
```

### Open up required ports in the firewall

Now that you have defined the ports in the configuration file and in the system service file, you will need to
open those ports on the firewall. Since we manage this system's firewall with uncomplicated firewall manager
`ufw`, this is easy to do.

```bash
sudo ufw allow proto tcp from 192.168.1.0/24 to any port 32765:32768
# You should only have to configure ports for the TCP protocol, but you can open them for the UDP protocol
# just in case.
sudo ufw allow proto udp from 192.168.1.0/24 to any port 32765:32768
```

### Creating facade mount points

Nearly ever tutorial out there suggests one take the extra precautionary measure of setting up what is
referred to as "shares" or as "pseudo file system mount points", whatever they are called, they are the same
thing. These mount points are used to prevent malicious users from acquiring access to parts of the system
they are not supposed to have access to. Which is because NFS is run by the root user, and therefore can be
exploited. (Basically not time to explain.)

#### Modify the configuration file

In order to configure this feature, you will need to modify the configuration file created earlier, adding the
option for `exports` to designate the rootdir for provisioning. You will want to place this option above the
`[mountd]` section. So your configuration file should now look like so:

```ini
[lockd]
port=32768
udp-port=32768
# Place new lines for provisioning below.
[exports]  # <-- Here
rootdir=/var/nfs  # <-- And here.
[mountd]
udp=no
port=32767
[nfsd]
udp=n
tcp=y
vers2=n
vers3=y
vers4=n
vers4.0=n
vers4.1=n
vers4.2=n
[statd]
port=32765
outgoing-port=32766
```

#### Stop both rpcbind and nfs-service

Since this involves tinkering with drives that are already mounted AND currently
busy being used by the nfs service, it is good idea to stop the rpcbind and nfs-service.

```bash
sudo systemctl stop rpcbind.socket
sudo systemctl stop rpcbind.service
sudo systemctl stop nfs-server.service
```

We will restart both services when we have completed configuration.

#### Make the file system tree

Create the needed directories, change ownership of that tree, and perform a mount.

```bash
sudo mkdir -p /var/nfs
# You can create two directories at once with brackets.
sudo mkdir -p /var/nfs/{mount1,mount2}
sudo chown -R nobody:nobody /var/nfs
sudo mount --bind /path/to/mount1 /var/nfs/mount1
sudo mount --bind /path/to/mount2 /var/nfs/mount2
```

Check to see that everything worked with `sudo df -ah`.

#### Make your pseudo mount points permanent.

Open up `/etc/fstab` and add the mount points to the file. Like so:

```conf
/path/to/mount1 /var/nfs/mount1   none bind
/path/to/mount2 /var/nfs/mount2   none bind
```

#### Modify `/etc/exports`

Now, you will need to modify the `/etc/exports` file to reflect these new mount points. The key difference is
now that you have set `rootdir=/var/nfs`, as far as rpcbind and nfs-server are concerned, `/var/nfs` is now
the root of your filesystem. So, you only need to add the path after `/var/nfs`.

```conf
/mount1    10.0.0.1/255.255.255.255(sync,wdelay,crossmnt,no_subtree_check,sec=sys,rw,insecure,no_root_squash,no_all_squash)
/mount2    10.0.0.1/255.255.255.255(sync,wdelay,crossmnt,no_subtree_check,sec=sys,rw,insecure,no_root_squash,no_all_squash)
```

#### restart services and mount on client

Restart both rpcbind and nfs-server on the host.

```bash
sudo systemctl start rpcbind.service
sudo systemctl start nfs-server.service
```

Check that everything is running on your host machine with `sudo showmount -e`

This is where things get a little sticky, because it is time for you to test your mounts on your client
system. The actual commands to do so, will vary depending on what system that is. Regardless, the key is to
make sure you designate the "tcp only" option. On OpenBSD, the command will look like so:

```bash
sudo mount_nfs -T3 -o nodev,nosuid,rw,soft,intr 10.0.0.1:/mount1 /mnt/mount1
```

The `-T3` flag instructs the system to mount using TCP and with version 3 only.

#### Check to see which NFS versions are running

You can check to ensure you are running the desired versions of nfs like so in linux:

```bash
cat /proc/fs/nfsd/versions
```

### Setting up fstab for NFS client

Personally, I do not do this for my desktop environment. I haven't quite invested the time into discovering
what exactly the hangup was about, but I have had the system hang while executing the sync operation on the
NFS attached drive directly before performing a reboot several times. Everytime this occurred, my drive was
marked as having been unmounted dirty, so the long thirty minute filesystem check was required once booted up
again. This occurred enough to where finally the line mounting the drive was removed from `/etc/fstab`, and 
a script was written to easily and manually mount the drive instead. This seems to have worked better for my
situation.

#### Making it permanent

Once everything is up and running, you probably do not want to mount the nfs volume manually each time. So,
you can set up fstab to mount the NFS volume automatically on boot with the rest of the filesystem.

```conf
host_ip:/var/nfs/general    /nfs/general   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
host_ip:/home               /nfs/home      nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
```

## References

- [How To Forge: NFS Server](https://www.howtoforge.com/tutorial/install-nfs-server-and-client-on-debian)
- [Debian Wiki: NFS Server Setup](https://www.howtoforge.com/tutorial/install-nfs-server-and-client-on-debian)
- [ArchLinux Wiki: NFS](https://www.howtoforge.com/tutorial/install-nfs-server-and-client-on-debian)
- [Legacy NFS v3 on Debian](https://entropux.net/article/legacy-nfs-v3-on-debian-buster-10/)
- [NFS Server on Linux](https://zacks.eu/nfs-server-on-linux/)
