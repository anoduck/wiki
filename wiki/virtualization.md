```text
# __     ___      _               _ _          _   _
# \ \   / (_)_ __| |_ _   _  __ _| (_)______ _| |_(_) ___  _ __
#  \ \ / /| | '__| __| | | |/ _` | | |_  / _` | __| |/ _ \| '_ \
#   \ V / | | |  | |_| |_| | (_| | | |/ / (_| | |_| | (_) | | | |
#    \_/  |_|_|   \__|\__,_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
#
```

## Virtualization

Virtualization is the act of creating a virtual replica of something at the same abstraction level. In
computer science you will hear about two different types of virtualization, full virtualization and
paravirtualization, the latter being referred to more commonly as containerization. 

You can do pretty neat stuff with it. Right-O-rooney...

| [Podman](podman) | [VirtualBox](virtualbox) | [Qemu](qemu) |

### Fully removing docker

It is not common to find oneself in a position to desire to wipe docker completely from one's system, but if you
ever arrive at that conclusion, it is good to know how. We will take it in three basic steps.

#### 1. Identify currently installed docker packages

```bash
dpkg -l | grep -i docker
```

#### 2. Remove and Purge them from your system

In two commands:

```bash
# 1. Uninstall and remove configuration files.
sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli docker-compose-plugin

# 2. Purge the package files and cache from your system.
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce docker-compose-plugin
```

#### 3. Remove Images, Containers, Volumes, and configuration files.

If you recieve an error that one or more files are missing, that's totally cool, don't worry about it.

In five:

```bash
# 1. Remove Docker's configuration folder and folder for data.
sudo rm -rf /var/lib/docker /etc/docker

# 2. Remove Docker's apparmor rules. (Not always present)
sudo rm /etc/apparmor.d/docker

# 3. Remove the Docker group
sudo groupdel docker

# 4. Remove Docker's runtime socket
sudo rm -rf /var/run/docker.sock

# 5. Remove folder for container storage.
sudo rm -rf /var/lib/containerd
```
