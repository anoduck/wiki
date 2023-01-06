## Partitioning in OpenBSD

Performing a detailed and comprehensive partitioning is something that is rarely done these days, and has become even rarer since the
rise of virtualized and containerized technology. All that seems to be needed now these days is a partition for swap, and another
main partition to slap the entire file system together in. In OpenBSD however, there are still many benefits recieved from taking the
time to create a full and comprehensive partition scheme.

Unfortunately, creating a successful partition scheme presents several pitfalls that a user may succome to. First is, when it comes
time to work with disklabel and perform the partitioning, one may feel the urge to take advantage of the available option to automate the
distribution of disk assets to partitions using a system provided scheme. As the user will find, this does break the disk down into
separate partitions, but once the size of these partitions are examined, it will undoubtedly be deemed unusable. The only way to avoid
this pitfall is through preparation of a partitioning template. Which later can be employed to automate the partitioning in disklabel
using the `-t` flag or to manually perform the parititioning.

Creating a partition template is relatively easy by comparison to other configuration file structure and syntax. The syntax of the
template is simply one partition per line, providing partition type, mount point, min-max size range, and/or percentage of disk space for
use. Each of these being separated by a single space. A maximum amount can be declared by using an asterick '*'.

### System Installed Partitioning Template

Below is how OpenBSD will partition your disk using the system installed partition template according to the size of the drive you are
using.

```txt
Disks >= 10 Gigabytes
         /                5% of disk.  150M – 1G
         swap            10% of disk.   80M – 2x max physical memory
         /tmp             8% of disk.  120M – 4G
         /var            13% of disk.   80M – 4G + 2x size of crash dump
         /usr            10% of disk. 1500M – 30G
         /usr/X11R6       3% of disk.  384M – 1G
         /usr/local      15% of disk.    1G – 20G
         /usr/src         2% of disk. 1500M – 3G
         /usr/obj         4% of disk.    5G – 6G
         /home           30% of disk.    1G – 300G

    Disks > 2.5 Gigabytes
         /                5% of disk.  800M – 2G
         swap            10% of disk.   80M – 2x max physical memory
         /usr            78% of disk. 1300M – 3G
         /home            7% of disk.  256M – 2G

    Disks > 700 Megabytes
         /               95% of disk. 700M – 4G
         swap             5% of disk.   1M – 2x max physical memory
```

### Partition Template File Example

The manual page for disklabel does provide the user with an template example to model their own template after.

In the following you will find the example for a unencrypted filesystem:

```txt
         /               250M
         swap            80M-256M 10%
         /tmp            120M-4G 8%
         /var            80M-4G  13%
         /usr            1.5G-3G 5%
         /usr/X11R6      512M-1G 3%
         /usr/local      2G-10G  10%
         /usr/src        1.5G-3G 2%
         /usr/obj        1.3G-2G 4%
         /home           1G-*    45%
```

Note, that the paritition scheme will completely differ when employing disk encryption. This is due to the requirement of creating a
softraid device and incorporating the entire disk into that softraid. So, for encrypted disks the template should merely look something like this:

```txt
RAID    1M-*    100%

```

For further information on how to perform disk encryption, please see the [OpenBSD FAQ](https://www.openbsd.org/faq/).

### Our Partition Scheme

Now that we have examined what a parition template is. Let's create one for actual use. The target disk is a miniscule 60
gigabytes in size, and the intended system setup will be for a web server that will host a website and some web services. So, the
priority of our partitions are first `/var` and `/tmp`, followed by `/home` and `/usr`. Finally the remaining amount of
space will be bulkly allocated to `/`.

Before we begin, let's examine a previous partition layout that is no longer in use, as it will give us some idea as how to best
distribute out the space on our drive.

```text
16 partitions:
#                size           offset  fstype [fsize bsize   cpg]
  a:            29.8G               64  4.2BSD   2048 16384 12958 # /
  b:             8.0G         62512960    swap                    # none
  c:           596.2G                0  unused                    # <-- Remember c: is never used in unix.
  d:            77.5G         79296864  4.2BSD   2048 16384 12958 # /usr
  e:            71.5G        241830368  4.2BSD   2048 16384 12958 # /usr/src
  f:            47.7G        391861312  4.2BSD   2048 16384 12958 # /usr/obj
  g:            17.9G        491881952  4.2BSD   2048 16384 12958 # /usr/X11R6
  h:            89.4G        529389664  4.2BSD   2048 16384 12958 # /usr/local
  i:           125.2G        716928352  4.2BSD   2048 16384 12958 # /var
  j:            41.7G        979482528  4.2BSD   2048 16384 12958 # /tmp
  k:            87.4G       1067000576  4.2BSD   2048 16384 12958 # /home
```

#### Calculations

This is where the tire meets the road, and we develop a basic idea of how the partitions will be laid out.

* In the past, as a rule of thumb, `swap` should not be more than 10% of the available disk space. These days, 5% or less is more of
  the norm. This will make our swap 1 gigabytes in size, which is roughly 1.5% of drive space. Generally the 'b' partition is used for swap.
* Considering we now have five partitions remaining and 58 gigabytes left. If we divide the remaining drive space left evenly across
  the remaining partitions, each parition would be 11.2 gigabytes. Although, this is not what we want, it does give us some idea about
  what planned sizes should be.
* Considering this will be a headless server, we should not need more than 6 gigabytes for `/` to distribute to the base system. That
  gives us 52 gigabytes remaining and consumes 10% of the disk.
* From experience, I have never hosted a site that is over 12G in size. The site being planned will be small and streamlined, so 12 gigabytes of
  space should suffice. This would consume 20% of our drive space, and 30 gigabytes to go.
* `/tmp` should be a third the size of `/var`, which is 4 gigabytes. Consuming 7% of diskspace, with 26 gigabytes to go.
* The entire site needs to fit inside of `/home` for convenience in case a site backup is needed. This also makes site development more
  convenient. 16 gigabytes should do this nicely, and provide ample space for miscellaneous storage. 27% of
	disk space consumed and 10 gigabytes to go.
* From experience, I have discovered that `/usr` stores a lot of the system's resources, and always exceeds
	the size of the `/` partition. So let's give the remainder of the space to the `/usr` partition. Which would
	equate to roughly 17% of disk space.

#### Our template

Taking the above decided partition sizes of our partitioning scheme, a template file should look like this:

```text
/ 6G-8G 10%
swap 1G-1.5G 1.5%
/home 16G-18G 27%
/usr 9G-10G 17%
/tmp 4G-6G 7%
/var 12G-15G 20%
```
