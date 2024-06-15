```text
#  ____       _     _       _
# | __ ) _ __(_) __| | __ _(_)_ __   __ _
# |  _ \| '__| |/ _` |/ _` | | '_ \ / _` |
# | |_) | |  | | (_| | (_| | | | | | (_| |
# |____/|_|  |_|\__,_|\__, |_|_| |_|\__, |
#                     |___/         |___/
#
```

Working with network bridges
=============================

### Adding a Bridge

There are numerous ways to go about doing this now. At one time using brctl was the defacto method 
of creating and modifying bridges, but this is no longer the case. Currently, using the ip command 
is how bridges are currently managed and created.

1. Create the bridge interface

```bash
ip link add name br0 type bridge
ip link set dev br0 up
```

2. Take note of the network configuration as it is.

```bash
ip addr show eth0
ip route show dev eth0
```

3. Initial Bridge Setup

```bash
ip addr add 192.168.1.2/24 dev br0
ip route append default via 192.168.1.1 dev br0
```

4. Create a script file, with the following contents ( or create a script file and put everything in it.)

```bash
#!/usr/bin/env bash
ip link set eth0 master br0
ip address del $ADDR dev eth0
```



