```text
#  _____        ______
# |_ _\ \      / /  _ \
#  | | \ \ /\ / /| | | |
#  | |  \ V  V / | |_| |
# |___|  \_/\_/  |____/
#
```

## iwd - The internet wireless daemon

_*Not to be confused with [iw](iw).*_

The internet wireless daemon (iwd) is meant to be a comprehensive connectivity solution for the linux
operating system. The primary goal was to create a solution optimized toward efficient resource usage. 

### Usage

Iwd runs as a system daemon, so to use it one must either start it with su privileges or start it with systemd,
sysv, openrc, or etc... Once this is accomplished the user must be added to the `netdev` group. ex. `sudo
usermod -a -G netdev user`. Afterwards, the iwctl command will drop the user into the iwd ctrl shell. 

#### Configuration

The `/etc/iwd/main.conf` configuration file configures general settings for iwd. 

Individual interfaces are configured through independent configuration files found in `/var/lib/iwd`, and have
a unique extension naming convention. The extension used is dependent on the security protocol that will be 
implemented. There are:

1. `.open` for open networks with no encryption.
2. `.psk` for networks using psk based encryption. This would include wpa and wep.
3. `.8021x` for networks using the 8021x encryption standard.

Each interface configuration file contains:

1. `[Settings]` section where general configuration settings can be set.
2. `[Security]` section where security settings can be set. But this is only relavent for `.psk` and `.8021x`.
3. `[Network]` secion contains general network settings.
4. `[IPv4]` section for ipv4 relevent settings.
5. `[IPv6]` section for ipv6 relevent settings.

Example for `$DEVICE.open`

```conf
[Settings]
AutoConnect=false
Hidden=false
AlwaysRandomizeAddress=true
```

Example for `main.conf`

```
[General]
AddressRandomization=network
AddressRandomizationRange=full
```


### References
More information on how to configure iwd can be found in [the kernel wiki](https://iwd.wiki.kernel.org/start).
