```text
#   ___                   ____ ____  ____
#  / _ \ _ __   ___ _ __ | __ ) ___||  _ \
# | | | | '_ \ / _ \ '_ \|  _ \___ \| | | |
# | |_| | |_) |  __/ | | | |_) |__) | |_| |
#  \___/| .__/ \___|_| |_|____/____/|____/
#       |_|
#  _   _      _                      _
# | \ | | ___| |___      _____  _ __| | __
# |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
# | |\  |  __/ |_ \ V  V / (_) | |  |   <
# |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
#
```

## Networking on OpenBSD

You live, you love, you learn, and you make mistakes. It is all part of the mystical journey of life. If you
are a member of the school of hard knocks, mistakes is how you learn. The more mistakes you make, the more you
learn. Here are a few pointers about networking with OpenBSD that I have learned the hard way by making
mistakes.

- As usual, any word/phrase that is capitalized and preceded with a '$' represents a variable. 
- All information is for ipv4. 

### Static IP Configuration

Standard ip configuration for OpenBSD is kept in a `/etc/hostname.$IFACE` file. If you were to
configure the interface via dhcp, then you would simply place `inet autoconf` in the file, ensure that
dhcpleased is running, and be done with it. Static configuration is only slightly more involved, but does
differ from the linux equivolent. 

#### Example hostname.if

Below is an example of a static ip configuration for OpenBSD

```conf
inet 192.168.0.1 255.255.255.0 192.168.0.255
dest 192.168.0.0
up
```

What this does is designate the following:

* _Line 1_

- "inet" = designates IPv4, where "inet6" designates IPv6.
- "192.168.0.1" = The static IP address of the computer you are configuring.
- "255.255.255.0" = Is of course, the network subnet.
- "192.168.0.255" = Broadcast

* _Line 2_

- "dest" = Is a special keyword indicating what follows specifies the next network hop. __It does not set the default gateway.__
- "192.168.0.0" = Is the address of the next network hop.

* _Line 3_

- "up" = Simply brings the interface up. Without it, the interface would remain down.

#### Remaining Configuration for Static IP Setup

1. If you thought you would be done after editing the hostname.if file, then you would be terribly wrong to your
detriment. You still have to establish the default route for the network. This is done in the `/etc/mygate`
file. This file is solely comprised of one value, and that is your default gateway. If desired, you may change
this in one shot from the command line `echo 192.168.0.0 > /etc/mygate`, or you can be fancy about it and open
up an editor. 

2. Next you need to define the default domain of your network. Just like with the default route, this is also
contained in a file, the `/etc/defaultdomain` file, and is the only thing in that file. So, 
`echo mydomain.local > /etc/defaultdomain` should do it. 

3. Next, the same for the hostname, which is kept in `/etc/myname`. Unlike, linux, which uses `/etc/hosname`.
Also, unlike linux, this file contains a FQDN. Note, the domain name must match the domain used above.
Again, `echo myhost.mydomain.local > /etc/myname` will set it.

#### Setting up a resolv.conf

4. Lastly, you need to configure `/etc/resolv.conf`, so queries to domains are answered. In most personal
networks, this is often the same as your gateway, but I don't particularly like this. I don't like using
google for this either, so I usually add a few publicly available nameservers. 

```conf
nameserver 9.9.9.9
search mydomain.local.
```

That extra dot at the end of your domain is important. Don't mistakenly remove it.
