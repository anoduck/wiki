```text
#  ____        _ _     _                 _
# | __ ) _   _(_) | __| |_ __ ___   ___ | |_
# |  _ \| | | | | |/ _` | '__/ _ \ / _ \| __|
# | |_) | |_| | | | (_| | | | (_) | (_) | |_
# |____/ \__,_|_|_|\__,_|_|  \___/ \___/ \__|
```

# Buildroot

Buildroot is a tool for embedded platforms that builds an entire linux system through cross compilation. Cross
compilation is compiling source code for a different achitecture than the host system which is performing the
compilation. A common example of this would be compiling software for arm64 on a x86_64 computer.

## TL, DNR

> Too long, did not read.

For those of us who breeze through life without paying attention to details, here is the speil.

### Config and Make

This should not come as a surprise. To configure build root you use `make menuconfig` to create a configuration file,
and then you use `make` to build your system. The result will be stored in the `output` directory.

### Output directory

Once the system is successfully built, the end result will be placed in the `output` directory as stated
above. Depending on what buildroot is configured to build the following four directories should be populated
with the result.

- *images* = Kernel images, bootloaders, and file system images.
- *host* = Tools and libraries used by the host to build the linux system.
- *staging* = is symbolically linked to the `sysroot` directory inside the `host` directory. The sole purpose of
  this directory is backward compatibility. So, ignore it.
- *target* = This file contains an _almost_ complete replica of the root filesystem for your target. It is used
  to generate the actual image of your file system. Note, it is not meant to be used for installation
  purposes.

## General Usage

General usage of the buildroot environment. This section might as well be considered the "User Manual".

### Configuration

All the available comands to configure buildroot offer help text for details about a particular option, and
all configuration commands provide a search tool that can be used to search for specific options. 

In order for buildroot to build the target system, it will require a toolchain to perform the compilation. As
mentioned previously, since buildroot involves building an linux system through cross compilation, this
toolchain will need to be specific to the target architecture you plan on building linux for. 

#### Toolchain Options

Buildroot allows you to chose among two different solutions to provide this toolchain. The toolchain can
either be (1) internal or (2) external. The former of these options will build the toolchain prior to building
the target system, where as the latter allows the user to designate a pre-built toolchain solution. 

##### Internal toolchain

There are three supported internal toolchains for build root, they are uClibc-ng, glibc, and musl. These are
all different `C` libraries, with glibc being what many consider to be the defacto. 

Once it is decided which of the three toolchains is to be used, buildroot then allows you to select which of
the linux kernal headers to use, which version of GCC to use, and several other options specific to the
toolchain istself. 

The primary drawbacks to using internal toolchains are time and space. As one would deduce, compiling a
toolchain from scratch is time consuming, and takes up additional space on the host machine.

##### External Toolchain

Not only does buildroot recognize external toolchains, but if chosen, it will download, extract, and use the
external function automatically. If this is not desirable, buildroot will also allow the user to provide the
path to where the external toolchain can be located, or a custom toolchain can be configured altogether. 

Buildroot also allows you to build the internal toolchain and configure it to be used as an external toolchain
that can be shared and reused for other projects. This is done by selecting "None" as the Init system options
and "None" as the `/bin/sh` option. Then disable busybox and "tar the root filesyste" option. The toolchain is
then generated as an SDK by executing the command `make sdk`.

#### Primary system configuration options

Before getting to some of the finer details of system configuration, configuration of how the system plans to
manage attached devices, and how the init program is to be implemented. 

##### /dev management

On Linux and "nix" systems, the `/dev` directory contains a set of files referred to as "device files". Each of these
files represent a device that is connected to the system. This includes devices that make up a part of the
system itself. It is through these files that programs and the system are able to interact with connected
devices. The most common example of this interaction would be performing a mount operation, where a storage
device is mounted to the system, and the file system contained with in the storage device is made available. 

In order to properly manage these files, buildroot provides four different options.

1. Static device table
2. Dynamic devtmpfs only
3. Dynamic hybrid devtmpfs and mdev
4. Dynamic hybrid with devtmpfs and eudev.

Of course, the static solution is persistent across boots, and does not change regardless of what is
physically connected to the system. Where the dynamic solutions are not persistent across boots, and change
depending on connected devices. Only the implementation of mdev and eudev provide notification to userpace
applications when this list of devices changes.

Of these four solutions, the buildroot developemtn team reccommends using devtmpfs only until there is a need
for userspace applications to recieve notifications about changes in devices. But, if you want a full featured
linux system, you will more than likely want to select devtmpfs and eudev.

##### Init Systems

Regardless of the literal plethora of available init systems for both linux and unix, buildroot only supports
the tiny wonder busybox, the old favorite Sys-V, the dark knight SystemD, and the retrowave OpenRC.

While the buildroot team recommend keeping the system small and confined by selecting the busybox option, most
of us who desire of full featured linux system will select SystemD for compatibility purposes, but OpenRC is
a highly reccommended alternative.


