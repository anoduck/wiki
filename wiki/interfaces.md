```text
#  _   _      _                      _
# | \ | | ___| |___      _____  _ __| | __
# |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
# | |\  |  __/ |_ \ V  V / (_) | |  |   <
# |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
#
#  ___       _             __
# |_ _|_ __ | |_ ___ _ __ / _| __ _  ___ ___  ___
#  | || '_ \| __/ _ \ '__| |_ / _` |/ __/ _ \/ __|
#  | || | | | ||  __/ |  |  _| (_| | (_|  __/\__ \
# |___|_| |_|\__\___|_|  |_|  \__,_|\___\___||___/
#
```

Interfaces: The complex and the simple
---------------------------------------

There are many different types of network interfaces, each one distinct in their own right, designed for a
particular purpose in mind, and possessing their own benefits and limitations. Creating a definitive survey of
all the different types would be a job best left to a graduate student, but providing a general idea of what
is out there is something we can definitely provide. (Worst intro ever...)

### Basics

There is no reason to review the basic varieties that everyone is or should be familiar with. There would be
your ethernet interfaces, wireless interfaces, and perhaps if you remember your ppp interfaces. If you are a
mac junkie, you would be familiar with the firewire, which I have never touched personally. There are also
serial interfaces that everyone should know, and let's not forget the USB interface. These we know.

### Interfaces for Virtual Networking

Some of these, have been around for sometime now, while others are so new they were not used until only the past few
years. The one thing they all have in common is that they are not associated with an actual physical device,
and most of them are used to work with virtual machines of one form or another. In typical fashion, we will
provide a table that review all of these, and explains them. Then afterwards might review a few of them we are
specifically interested in afterwards.

Also, there is an entire page dedicated to the [Veth Device](virt_eth)

| Type             | Purpose                                 |
| ------           | -------------------------------------   |
| Bridge           | Forwarding packets between interfaces   |
| Bonded           | Aggregation and load balancing          |
| Team             | Like Bonded, but more featureful        |
| Vlan             | Allows separation of subnets            |
| Vxlan            | Allows more hosts than vlan             |
| Veth             | Allows communication between namespaces |
| MACVTAP / IPVTAP | Simplifies virtual bridge networking    |
| Dummy            | Testing and debugging                   |
| NetDevSim        | Used for simulating and testing         |

### Virtual Interface Tunnels

We are only going to touch two or three of these as we have not had the fortune to encounter them too often.
IPIP and GRE are the most commonly implemented forms, but again unless you are implementing or encountering a
network facilitating IpSec, they are not that common.

| Type | Purpose                           |
| ---  | --------                          |
| Ipip | connect two internal ipv4 subnets |
| GRE  | Used for encapsulation of traffic |

### Good ole tun and tap interfaces

The primary reason for creating this page was to stress the distinguishment of the above virtual tunnel and tap
interfaces. This is because the two can be easily confused. A Tun/Tap interface is virtual and does perform tunneling,
but yet is distinct from the above due to it not being associated with virtual applications, machines, or containers.
As such, it understandibly has a longer history of established use, and is more commonly encountered than any of the
above examples. If you have ever configured a VPN, then you should already be familiar with the tun/tap types
of interfaces.

Configuration of the tun/tap interface are both managed by an iproute2 prefix as is customary with the other
interface types mentioned, the prefix of such being, `ip tuntap ...`. Except for performing routine functions
such as assigning an address or adding the interface to a bridge, all other configuration methods shall employ
this command / prefix combination. Here are a few examples.

1. create a tunnel device = `ip tuntap add name tun0 mode tun`
2. create a tap device = `ip tuntap add name tap0 mopde tap`
3. delete a device = `ip tuntap delete tun0 mode tun`
4. show devices = `ip tuntap show`
5. linking to another device = `ip tuntap change tun0 dev br0`
6. changing name = `ip tuntap change tun0 name tun1`

More need to be discovered in regards to the numerous configuration options the iproute2 interface provides,
specifically the `dev` parameter.

#### Pointless python tunnel creating script

After reviewing the two last references, I learned that you can create and configure tunnel devices
programmatically without using any of the cli tools. Playing with this concept I wrote the following.

```python
#!/usr/bin/env python3

import fcntl
import struct
import os
from scapy.layers.inet import IP
from warnings import warn
from dataclasses import dataclass, field
from typing import List
import subprocess


@dataclass
class apData:
    IFNAMSIZ: int = 16
    IFF_TUN: int = 0x0001
    IFF_TAP: int = 0x0002  # Should we want to tunnel layer 2...
    IFF_NO_PI: int = 0x1000
    TUNSETIFF: int = 0x400454ca
    IP_ADDRESS: str = "10.1.1.1"
    NETMASK: str = "255.255.255.192"
    IP_NETWORK: str = "10.1.1"
    NET_BROADCAST: str = "10.1.1.63"
    DHCP_MIN: str = "10.1.1.2"
    DHCP_MAX: str = "10.1.1.62"
    DHCP_EXPIRY: int = 28800
    AP_HIDE: bool = False


def create_tun():
    name = "rogue1"
    if len(name) > apData.IFNAMSIZ:
        raise Exception(
            "Tun interface name it too big"
        )
    fd = open('/dev/net/tun', 'r+b')
    ifr_flags = apData.IFF_TUN | apData.IFF_NO_PI
    ifreq = struct.pack('16sH', name, ifr_flags)
    fcntl.ioctl(fd, apData.TUNSETIFF, ifreq)
    if subprocess.call(['ip', 'addr', 'add', apData.ip, 'dev', self.dev]):
        warn("Failed to assign ip address to dev")
    if subprocess.call(['ip', 'link', 'set', 'dev', self.dev, 'up']):
        warn("failed to bring device up")


if __name__ == "create_tun.py":
    create_tun()
```

### References

- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/configuring-ip-tunnels_configuring-and-managing-networking
- https://developers.redhat.com/blog/2019/05/17/an-introduction-to-linux-virtual-interfaces-tunnels#
- https://developers.redhat.com/blog/2018/10/22/introduction-to-linux-interfaces-for-virtual-networking#vlan
- https://john-millikin.com/creating-tun-tap-interfaces-in-linux
- https://blog.cloudflare.com/virtual-networking-101-understanding-tap/
