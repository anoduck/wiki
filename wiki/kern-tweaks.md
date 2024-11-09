```txt
#  _  __                    _   _____                    _
# | |/ /___ _ __ _ __   ___| | |_   _|_      _____  __ _| | _____
# | ' // _ \ '__| '_ \ / _ \ |   | | \ \ /\ / / _ \/ _` | |/ / __|
# | . \  __/ |  | | | |  __/ |   | |  \ V  V /  __/ (_| |   <\__ \
# |_|\_\___|_|  |_| |_|\___|_|   |_|   \_/\_/ \___|\__,_|_|\_\___/
#
```

Kernel Tweaking
---------------

Making changes to the kernel runtime in OpenBSD is for the most part exactly the same as in linux. Changes
that are to be made in real time can be done so by using the `sysctl` command, and more permanent changes can
be so by modifying the `/etc/sysctl.conf` file. The configuration values might be a little different, but if
one is familiar with modifying the kernel runtime in linux, this should not matter much. Just as one doesn't
go all willy-nilly, things should work out. Below we will discuss making changes to the kernel runtime to
improve the performance of the TCP stack for high speed connections.

### OpenBSD runtime tweaks for TCP

```conf
### Kernel Tweaks - from source #1
ddb.panic=0                     # do not enter ddb consol on kernel panic, reboot if possible
net.inet.ip.forwarding=1        # Permit forwarding (routing) of packets
net.inet.ip.ifq.maxlen=512      # Maximum allowed input queue length (256*number of interfaces)
net.inet.icmp.errppslimit=1000  # Maximum number of outgoing ICMP error messages per second
net.inet.ip.ttl=254             # the TTL should match what we have for "min-ttl" in scrub rule in pf.conf
net.inet.tcp.ackonpush=1        # acks for packets with the push bit set should not be delayed
net.inet.tcp.ecn=1              # Explicit Congestion Notification enabled
net.inet.tcp.mssdflt=1452       # maximum segment size (1452 from scrub pf.conf)
net.inet.tcp.rfc1323=1          # RFC1323 TCP window scaling
net.inet.tcp.recvspace=262144   # Increase TCP "receive" windows size to increase performance
net.inet.tcp.sendspace=262144   # Increase TCP "send" windows size to increase performance
net.inet.tcp.sack=1             # enable TCP Selective ACK (SACK) Packet Recovery
net.inet.udp.recvspace=262144   # Increase UDP "receive" windows size to increase performance
net.inet.udp.sendspace=262144   # Increase UDP "send" windows size to increase performance
kern.maxclusters=128000         # Cluster allocation limit
vm.swapencrypt.enable=1         # encrypt pages that go to swap

### From source #2
ddb.panic=0                    # do not enter ddb console on kernel panic, reboot if possible
kern.bufcachepercent=90        # Allow the kernel to use up to 90% of the RAM for cache (default 10%)
machdep.allowaperture=2        # Access the X Window System (if you use X on the system)
net.inet.ip.forwarding=1       # Permit forwarding (routing) of packets through the firewall
net.inet.ip.ifq.maxlen=512     # Maximum allowed output queue length (256*number of physical interfaces)
net.inet.ip.mtudisc=0          # TCP MTU (Maximum Transmission Unit) discovery off since our mss is small enough
net.inet.tcp.rfc3390=1         # Enable RFC3390 TCP window increasing so larger CWND can take affect
net.inet.tcp.mssdflt=1440      # maximum segment size (1440 from scrub pf.conf match statement)
#net.inet.udp.recvspace=131072 # Increase UDP "receive" buffer size. Good for 200Mbit without packet drop.
#net.inet.udp.sendspace=131072 # Increase UDP "send" buffer size. Good for 200Mbit without packet drop.
```


