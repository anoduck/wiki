```text
#  ____  _____ ____  _        _      _
# |  _ \|  ___/ ___|| |_ __ _| |_ __| |
# | |_) | |_  \___ \| __/ _` | __/ _` |
# |  __/|  _|  ___) | || (_| | || (_| |
# |_|   |_|   |____/ \__\__,_|\__\__,_|
#
```

The Packet Filter Statistics Daemon
===================================

PF is the packet filtering system for OpenBSD and some NetBSD systems, in other words it is the firewall for
those systems. PF differs from other firewalls, except NPF (a brother from a different mother), because it
disassembles every packet sent to the host, inspects the packet, scrubs it of corruption, reassembles the
packet, and only then desides to reject, drop, or accept it. This is vastly different from other types of
firewall systems who for the most part simply perform a reject/accept operation. This means that pf firewalls
are more difficult to circumvent and can be an abundant source of information for any network administrator.

The statistics daemon
---------------------

Pfstatd is a small/tiny statistics processing daemon that collects analytical information from the pf daemon,
via the pseudo-device pf, and generates statistical graphs to represent the collected data. This data can then
be used to improve one's pf configuration or discover problems in one's networking framework. The entry is
primarily concerned with setting up the daemon securely and to run on first boot. 

### Configuration

Pfstatd comes with an example configuration, prepared and ready for use. All that is needed is for the example
interface used in the configuration file to be replaced with the primary network interface that is active on
one's system. The file is located in `/etc/pfstat.conf`, you an either modify this file by hand or do it in
one go with sed, the terminal stream editor, like so.

```sh
sed -i 's/em0/fxp0/g' /etc/pfstat.conf
```

### Prepare for starting

By default pfstatd listens on all network interfaces on port 9999. This port will not be accessible to the
external network unless we allow connections to it in our pf configuration, for now this is acceptable. So, to
enable pfstatd to run on startup we simply need to enable it and start it. We do so by executing the following
commands.

```bash
doas rcctl enable pfstatd
doas rcctl start pfstatd
```
