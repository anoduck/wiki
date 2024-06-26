```text
#  ____           _
# |  _ \ ___   __| |_ __ ___   __ _ _ __
# | |_) / _ \ / _` | '_ ` _ \ / _` | '_ \
# |  __/ (_) | (_| | | | | | | (_| | | | |
# |_|   \___/ \__,_|_| |_| |_|\__,_|_| |_|
#
```

Podman
-------

Podman is an open source alternative to Docker (which is free, but closed) for virtual containers. It appears
to be backed by Red Hat, which we are pleased to see has not died off yet. Podman is supposed to be a straight
drop-in replacement for docker and docker-compose, and although it is pretty damn close, it isn't exactly the
clean fit. This is cool, because along with being a pretty close drop-in, podman also comes with some extra
features that were not presently available with docker, or at least in a manner we are familiar with. Some of
podman's parts are actually wrappers around docker programs, so keep this in mind if you plan on exploring it
more.

Podman provides a tool called "podman toolbox" which provides the ability for users to create rootless containers
for which to run terminal applications inside of. This tool can be useful to complete isolate applications
inside of their own virtualized environment.


### Podman Containers vs. Podman Machine

Primarily podman is intended to be used to manage virtual containers, and this is what it does best. It is
important to distinguish the difference between podman containers and podman machine. Podman relies on podman
machine to run containers for operating systems that do not provide a native virtual abstraction layer. So, in
effect, the two are two different layers of the same system that implement separate functionality of the virtual
environment ecosystem. On Linux, Podman Machine is not implemented by default, and is not required for use of the
podman ecosystem.

-----

### Podman Rootless Configuration

Basic podman rootless container setup in a nutshell

```bash
usermod --add-subuids 100000-165535 --add-subgids 100000-165535 "$USER"
usermod --add-subgids 2000-2000 "$USER"
```

For here you can run rootless containers with the `--group-add keep-groups` and the `--gidmap="+g102000:2000`
commands.

Although these configurations were made, in our system they have yet to have taken effect. For information on
the shortcomings of podman rootless please see the second reference below.

#### References

- https://github.com/containers/podman/blob/main/rootless.md
- https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md

-----

### Podman Machine 

Podman Machine is the interface to the podman virtual machine layer, which is the fully virtualized environment
podman uses to manage and run virtual containers on. For linux systems this feature is not required and is not
implemented by default, and it's primary application is intended for use with MacOS and Windows systems which
do not provide virtual abstraction layer. Linux systems can access and use the podman virtual machine layer to
perform other tasks. The benefit one recieves from using podman in this manner is access to peripheral
devices that are not normally accessible to docker images. The default image used for doing this is
fedora-core, but podman can be configured to use other OCI images. 

#### Podman Machine Init

To use this feature, simply initialize a new podman machine with:

```bash
podman machine init
```

Do not use sudo for this, as podman machines are not intended to be run as root ever. 

#### Podman Machine Post Init

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

#### Podman Machine Set 

If you would like to add a USB device along with this new image you can use:

```bash
podman machine set --usb vendor=XXX,product=XXX
# OR
podman machine set --usb bus=XXX,devnum=XXX
```

Using bus and id are also accepted for these values, although they will change if the device is moved to a
different usb port or another usb is removed.

If you need your podman machine to have root permissions, you can run: `podman machine set --rootful`.

