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

- [podman machine](podman-machine)

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

The final step is to run the comman below.

```bash
podman system migrate
```

#### mkdir `/tmp/xxx...` permission denied

To resolve this issue:

```bash
sudo rm -rf ~/.local/containers
```

### Podman Wait-For

As far as podman is concerned, there is no difference between implementations designed for itself or docker.
So when it comes to a solution designed to pause starting a container service until another container's
service is running, there is no difference. 

This solution is commonly referred to as "wait-for", and there are now several different implementations that
can be used with podman. Below is a list of links that provide these solutions.

- https://github.com/eficode/wait-for
- https://www.baeldung.com/linux/docker-compose-container-interdependence
- https://github.com/ufoscout/docker-compose-wait

All of them require that netcat is installed on the system expected to run "wait-for".

#### References

- https://github.com/containers/podman/blob/main/rootless.md
- https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md

