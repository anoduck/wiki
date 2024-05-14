```text
# __     ______  _   _    ___  _   _    ___                   ____ ____  ____
# \ \   / /  _ \| \ | |  / _ \| \ | |  / _ \ _ __   ___ _ __ | __ ) ___||  _ \
#  \ \ / /| |_) |  \| | | | | |  \| | | | | | '_ \ / _ \ '_ \|  _ \___ \| | | |
#   \ V / |  __/| |\  | | |_| | |\  | | |_| | |_) |  __/ | | | |_) |__) | |_| |
#    \_/  |_|   |_| \_|  \___/|_| \_|  \___/| .__/ \___|_| |_|____/____/|____/
#                                           |_|
#
```

## OpenBSD VPNs

There are several available implementations of VPNs in OpenBSD. OpenVPN was once the defacto in many linux based
operating systems, but in OpenBSD, IKEv2 is the reccommended implementation. Wireguard is also
natively supported, and requires no external software to implement. Lastly, there is also tinc if one so
chooses, but this option is rarely supported by a VPN provider. 

For the following scenarios we will assume that you are using a VPN provider.

### OpenVPN

For implementing OpenVPN on OpenBSD with a VPN provider, one merely needs to download the appropriate OpenVPN
configuration from the provider and execute the openvpn command on the command line, followed by the
configuration file you downloaded. This will create a secure connection, and set up the appropriate
routes needed to redirect traffic through the vpn. 

The command to create a secure connection will look like:
```bash
sudo openvpn $YOUR_CLIENT_CONFIGURATION
```

There is a downside to this, and that is the OpenVPN connection is not daemonized, and dependent on the user
remaining logged in to the system. 

### IKEv2

__OpenBSD's implementation of the IKEv2 client was written specifically for compatibility with OpenBSD's implementation
of the IKEv2 server, and is not compatible with other IKEv2 servers.__

### Wireguard Configuration

Implementing a wireguard client VPN in OpenBSD is as simple as implementing an OpenVPN client. Visit your vpn
provider's download page, and download the configuration into `/etc/wireguard/wg0.conf`. Then from the
terminal execute the `wg-quick` command. The `wg-quick` command is the workhorse of the wireguard tool set. It
will configure the connection for you, bring up the interface, and handle all the routing for you. 

1. Bring up the connection

```bash
doas wg-quick up /etc/wireguard/wg0.conf
```

2. Save it for easier access

```bash
doas wg-quick save wg0
```

3. Bring it down when ready

```bash
doas wg-quick down wg0
```

4. bring it up again

```bash
doas wg-quick up wg0
```

### Reference Links

- [OpenVPN Client](https://astro-gr.org/openbsd-openvpn-client/)
- [Clein OpenVPN](https://umgeher.org/posts/2022/09/openbsd-client-openvpn.html)
- [OpenBSD Wireguard](https://marcocetica.com/posts/wireguard_openbsd/)
- [OpenBSD gateway using IKEV2](https://xw.is/wiki/OpenBSD_VPN_gateway_using_IPSec/IKEv2)
- [RoadWarrior styled vpn on OpenBSD with iked and openvpn](https://sukany.cz/blog/2022/04/roadwarrior-styled-vpn-on-openbsd-with-iked-and-openvpn/)
- [Iked / Configuring OpenIKED](https://wiki.ircnow.org/index.php?n=Iked.Configure?from=Openbsd.Iked)
- [Implementing IKE](https://www.semanticscholar.org/paper/Implementing-Internet-Key-Exchange-%28IKE%29-Hallqvist-Keromytis/3c89b7a845d4a5a63c84ac840b6851a260c21c40)
- [IKEv2 Interop testing](https://libreswan.org/wiki/IKEv2_Interop_testing_with_OpenBSD)
- [OpenBSD ike ipsec vpn](https://findelabs.com/post/openbsd-ike-ipsec-vpn/)
- [ipsec.conf man](https://man.openbsd.org/ipsec.conf.5)
