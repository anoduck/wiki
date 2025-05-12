```text
 _____    _       _     _               ____  ____   ____ 
|  ___|__| |_ ___| |__ (_)_ __   __ _  / ___||  _ \ / ___|
| |_ / _ \ __/ __| '_ \| | '_ \ / _` | \___ \| |_) | |    
|  _|  __/ || (__| | | | | | | | (_| |  ___) |  _ <| |___ 
|_|  \___|\__\___|_| |_|_|_| |_|\__, | |____/|_| \_\\____|
                                |___/                     
```

Fetching src with anoncvs
=========================

Fetching source code refers to the process of acquiring the actual source code used to build the OpenBSD
operating system. Very rarely, if almost never, is this needed to be done by the average Linux user for Linux
based OSs. BSDs are quite a different breed though, and not as often as it used to be, one has to acquire
parts of the source tree to perform specific operations. 

There was a time when this was a monthly, if not weekly, routine. Since, at that time the user only had two
means by which to upgrade their system. They could either download an ISO image of the new release and perform
an upgrade, or they could build the new release from source and install it from there. As one could assume, it
was far easier and less time consuming to go the ISO route. Fortunately, OpenBSD implemented a new upgrade
strategy that allowed the system to be easily upgraded through prebuilt binary packages, thus avoiding the
need to perform both of these former options.

Getting your hands on the goods
-------------------------------

Now, it's time to get your hands on the source code. You will need to select a mirror, cd to `/usr/src`, and
execute the command to fetch the source tree. 

### FTP - preload

OpenBSD recommends you preload the source tree from one of the FTP servers found [here](https://www.openbsd.org/ftp.html).
You simply download the src and sys tarballs and extract then in usr. 

More information can be found on [the anoncvs page](https://www.openbsd.org/anoncvs.html).

### AnonCVS

OpenBSD allows anonymous access to it's source tree via "anoncvs". There really isn't anything special about
"anoncvs" other than it grants you anonymous access to read the source tree from a cvs mirror. As previously
discussed in [Version Control](versioning), CVS is a version control system. OpenBSD mirrors the source tree
throughout numerous anoncvs mirrors, who syncronize with each other to maintain they are up to date with the
newest changes. Understand that not all of the CVS mirrors synchronize at the same pace, which is something
you will want to look into when you select a mirror.

#### Select a mirror

You can visit [mirrors](https://www.openbsd.org/anoncvs.html#CVSROOT) and select the nearest mirror to you
from there.

### The rest of the process.

Once again, being long winded has worked against me, and consumed too much time. So, let's get down to the
niddy gritty.

```bash
# add user to wsrc 
sudo user mod -G wsrc $USER
cd /usr
cvs -qd $SERVER:/cvs checkout -rOPENBSD_7_7 -P src
```

later on you can update it simply with `cvs -q up -Pd -rOPENBSD_7_7`

The entire process of building OpenBSD from source can be found in [FAQ 5](https://www.openbsd.org/faq/faq5.html)
