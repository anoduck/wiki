```text
#  _  __     _ _   _   _      _                      _
# | |/ /__ _| (_) | \ | | ___| |___      _____  _ __| | __
# | ' // _` | | | |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
# | . \ (_| | | | | |\  |  __/ |_ \ V  V / (_) | |  |   <
# |_|\_\__,_|_|_| |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
#
#   ____             __ _
#  / ___|___  _ __  / _(_) __ _
# | |   / _ \| '_ \| |_| |/ _` |
# | |__| (_) | | | |  _| | (_| |
#  \____\___/|_| |_|_| |_|\__, |
#                         |___/
#
```

Configuring your network on a fresh kali install
=================================================

This may seem rudimentry, but having done it recently there are a few pointers that would make life a hell of
a lot easier. 

For some reason, during the installation process, networking was configured to run on a hotplug
interface labeled `enps2`. This made things quite confusing once the installation had completed and the first
boot was performed. As the hotplug device was no longer present, and the only other device present except for
`lo0` was `eth0`. 

## Setting up the interfaces

Surprisingly Kali still uses the old school route of configuring interfaces via the `/etc/network/interfaces`
file, rather than the new and fancy use of the systemd networking framework, which is out of the scope of this
entry. This works with us as it is a breeze to setup.

### Terminology

* auto - "auto" means something totally different in Linux interface files than it does in OpenBSD
  `hostname.ifX` files. In linux, it brings the interface up, in OpenBSD it configures DHCP.
* iface - designates that you are defining an interface
* inet - designates that you are assigning an IP protocol network address to the interface
* static - designates that the assignment will be made statically.

```conf
# Usually when you open up this file the first interface listed will be the loopback interface. Don't touch
# it, just begin your new configuration variables below.

######################################
## LOOPBACK SETTINGS SHOULD BE HERE ##
######################################

# Now here is where the rubber hits the road.
# Don't place blank spaces between parameters.
# -------------------------------------------

# First we bring the interface up
auto eth0
iface eth0 inet static
    address 192.168.1.1/24
    broadcast 192.168.1.255
    gateway 192.168.1.0

```

## Added bonus

For an added bonus, there are two files that should be points of interest, the `hosts` file and the
`ip-up.d/route` file. The later is custom created. 

### hosts

It can be quite convenient to add important and local hosts to this file, and it will help your system resolve
them.

### route

Any script located in `/etc/network/if-up.d` will be executed upon bringing up the interface. This is a prime
moment to add additional routes to the routing table to prevent connections from being dropped when you work
on the configuration of your network. Just create a file, ensure it has the bang at the top, and write your
script.
