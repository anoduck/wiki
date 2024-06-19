```text
#  _   _      _   _____ _ _ _
# | \ | | ___| |_|  ___(_) | |_ ___ _ __
# |  \| |/ _ \ __| |_  | | | __/ _ \ '__|
# | |\  |  __/ |_|  _| | | | ||  __/ |
# |_| \_|\___|\__|_|   |_|_|\__\___|_|
#
```

Netfilter
=========

### NetFilter

Unlike PF, which primarily implements rules via a configuration file, NetFilter possesses several different
"interpretors" that interface with the kernel. The two most well known NetFilter interfaces are are iptables
and nftables. Both being widely implemented in different operating systems, are often implemented together as
they are not mutually exclusive, and both offer similar configurations. 

#### iptables

Iptables is the most common interface to the kernel's netfilter module using the command line. As such, it is
important to be familiar with a few basic commands.

##### Flags

- w = (wait) Wait for iptables to possess a lock.
- P = (Policy) Set the policy for the chain. Only two choices, ACCEPT and DROP.
- A = (Append) Appends the rule to the bottom of the chain.
- t = (table) which table the command should apply to. There are five: filter, nat, mangle, raw, and security
- i = (in-interface) Designates the inward interface the rule should apply to.
- o = (out-interface) Designates the outward interface the rule should apply to.
- j = (jump) Designates the target of the rule.
- m = (match) Condition used to match packet for a rule. 

##### Commands

| command                                                                                                  | description                                         |
| --------------------------------------------------------------------------------------------             | --------------------------------------------------- |
| `iptables-save -f /etc/iptables/iptables.rules`                                                          |                                                     |
| `iptables-restore /etc/iptables/iptables.rules`                                                          |                                                     |
| `iptables -A INPUT -i eth0 -p tcp --dport 902 -j REJECT --reject-with icmp-port-unreachable`             |                                                     |
| `iptables -L INPUT --line-numbers`                                                                       |                                                     |
| `iptables -D INPUT 2`                                                                                    |                                                     |
| `-w -P FORWARD ACCEPT`                                                                                   | Accept forwards                                     |
| `w -t nat -A POSTROUTING --out-interface $inet -j MASQUERADE`                                            | nat masquerade as inet                              |
| `-w -A FORWARD -i $inet --out-interface $wlan -j ACCEPT -m state --state RELATED,ESTABLISHED`            | forward inet out to wlan if related or established  |
| `-w -A FORWARD -i $wlan --out-interface $inet -j ACCEPT`                                                 | forward wlan out to inet.                           |
| `-w -A OUTPUT --out-interface $inet -j ACCEPT`                                                           | accept out traffic                                  |
| `-w -A INPUT --in-interface $wlan -j ACCEPT`                                                             | accept in traffic                                   |
| `iptables -A INPUT -p tcp -s 203.0.113.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT` | Allow ssh from specific address                     |
| `iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT`                      | Allow outgoing ssh (only if OUTPUT != ACCEPT)       |


