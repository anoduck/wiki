```text
#  _____ _                        _ _
# |  ___(_)_ __ _____      ____ _| | |___
# | |_  | | '__/ _ \ \ /\ / / _` | | / __|
# |  _| | | | |  __/\ V  V / (_| | | \__ \
# |_|   |_|_|  \___| \_/\_/ \__,_|_|_|___/
#
```

## Firewall systems and derivitives

Outside of Windon't, there are two primary firewall implementations. Derivitives of both exist, but only
differ slightly comparatively to the main implementation. These two implementations are PF and NetFilter.

The major difference between the two implementations is how network traffic is treated by the kernel. PF is
the only firewall implementation known that actually disassembles each network packet, inspects it, checks it
for validity, and then reassembles it before performing an action to the packet defined in the firewall's
rules. NetFilter on the other hand, does not disassemble the packet, nor does it check for it's validity. It
simply inspects the rules defined and performs whatever action is declared.

To better understand this distinction think of a firewall as a canal in which network traffic travels through.
NetFilter, acts as a lock for the canal. It either forwards the network packet through the channel to it's
destination, returns it back to the sender, or refuses to open and drops the packet all together. Where PF
acts as a port authority. It unloads the proverbial cargo of each packet, inspects all the contents of the
cargo, and the reloads the cargo back into the packet before performing the action defined in the firewall
rules.

The distinction and possible implementations of the two is arguably vast. There are those, like Linus
Torvalds, who believe that little distinguishes the two and use NetFilter because it is faster. Then there are
those who strongly disagree, as PF provides a network environment that possesses less errors, and a network
that is nearly impossible to spoof. Regardless, familiarity of the two is a skill every system administrator
should possess.

### NetFilter

Unlike PF, which primarily implements rules via a configuration file, NetFilter possesses several different
"interpretors" that interface with the kernel. The two most well known NetFilter interfaces are are iptables
and nftables. Both being widely implemented in different operating systems, are often implemented together as
they are not mutually exclusive, and both offer similar configurations.

#### iptables

Iptables is the most common interface to the kernel's netfilter module using the command line. As such, it is
important to be familiar with a few basic commands.

| command                                                                                      | description |
| -------------------------------------------------                                            | ----------- |
| `iptables-save -f /etc/iptables/iptables.rules`                                              |             |
| `iptables-restore /etc/iptables/iptables.rules`                                              |             |
| `iptables -A INPUT -i eth0 -p tcp --dport 902 -j REJECT --reject-with icmp-port-unreachable` |             |
| `iptables -L INPUT --line-numbers`                                                           |             |
| `iptables -D INPUT 2`                                                                                         |             |
|                                                                                              |             |
|                                                                                              |             |
|                                                                                              |             |
