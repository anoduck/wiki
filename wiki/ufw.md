```text
#  _   _ _______        __
# | | | |  ___\ \      / /
# | | | | |_   \ \ /\ / /
# | |_| |  _|   \ V  V /
#  \___/|_|      \_/\_/
#
```

Uncomplicated Firewall
======================

The uncomplicated firewall framework is first and foremost just a wrapper around iptables, and it's purpose is
exactly what it's name suggests, to allow configuration of firewalls without complication. Do not
misunderstand, working with iptables directly is in itself not that difficult, but in general the more stupid
simple you make the application, the better in the long run. 

Before diving into our primary tutorial for this page, let's look at some basic example commands.

### Basics

UFW can be easily and quickly installed on any linux machine through the package manager, if you are using a
debian derivative that would simply be `sudo apt install ufw -y`. Then you are ready to rock and roll.

1. Let's enable the firewall = `sudo ufw enable`
2. Don't forget to allow ssh = `sudo ufw allow ssh`
3. Now, open up the firewall for a webserver = `sudo ufw allow http https`
4. What if you want to delete a rule = `sudo status numbered` then with rule number `sudo ufw delete <$RULE_NUMBER>`
5. How about a more fine tuned example = `sudo ufw allow proto tcp from 192.168.1.1 to any port 4444`

You get the picture, it really just super easy.

### Setting up NAT

Setting up UFW to perform Network Area Translation (nat) is a little more complicated than the above, and
requires editing UFW configuration files. Just follow the instructions below. 

In the file /etc/default/ufw change the parameter DEFAULT_FORWARD_POLICY

```
DEFAULT_FORWARD_POLICY="ACCEPT"
```

Also configure /etc/ufw/sysctl.conf to allow ipv4 forwarding (the parameters is commented out by default). Uncomment for ipv6 if you want.

```
net.ipv4.ip_forward=1
#net/ipv6/conf/default/forwarding=1
#net/ipv6/conf/all/forwarding=1
```


The final step is to add NAT to ufw’s configuration. Add the following to /etc/ufw/before.rules just before the filter rules.

```
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]

# Forward traffic through eth0 - Change to match you out-interface
-A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these nat table rules won't
# be processed
COMMIT
```


Now enable the changes by restarting ufw.

```
$ sudo ufw disable && sudo ufw enable
```


### FORWARDING

For port forwardind just do something like this.

```
# NAT table rules
*nat
:PREROUTING ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]

# Port Forwardings
-A PREROUTING -i eth0 -p tcp --dport 22 -j DNAT --to-destination 192.168.1.10

# Forward traffic through eth0 - Change to match you out-interface
-A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these nat table rules won't
# be processed
COMMIT
```

### References

- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu
- [Referenced from Gist](https://gist.github.com/kimus/9315140)
- https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands
