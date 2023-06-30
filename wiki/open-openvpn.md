```text
#   ___                __     ______  _   _
#  / _ \ _ __   ___ _ _\ \   / /  _ \| \ | |
# | | | | '_ \ / _ \ '_ \ \ / /| |_) |  \| |
# | |_| | |_) |  __/ | | \ V / |  __/| |\  |
#  \___/| .__/ \___|_| |_|\_/  |_|   |_| \_|
#       |_|
#   ___                   ____ ____  ____
#  / _ \ _ __   ___ _ __ | __ ) ___||  _ \
# | | | | '_ \ / _ \ '_ \|  _ \___ \| | | |
# | |_| | |_) |  __/ | | | |_) |__) | |_| |
#  \___/| .__/ \___|_| |_|____/____/|____/
#       |_|
#
```

## OpenBSD VPNs

There are numerous implementations of VPNs in OpenBSD. OpenVPN was once the defacto in many linux based
operating systems, but in OpenBSD, IKEv2 is the reccommended implementation. Wireguard is also
natively supported, and requires no external software to implement. Lastly, there is also tinc if one so
chooses, but this option is rarely supported by a VPN provider. 

For the following scenarios we will assume that you are using a VPN provider.

### IKEv2

Setting up IKEv2 can be rather confusing, due to the unfamiliar terminology used, but it is fairly straight
forward in the command line.

1. To set up IKEv2, the certificate needs to be downloaded from your provider. This option is usually listed
   available for macOS systems, and since BSD is akin to macOS, this is OK. 
2. Once downloaded, you will notice the certificate will come with a file extension `.der`. This file extension
   is always used with X.509 certificates, but to use it we will have to convert it to the `.pem`
   format.

```bash
openssl x509 -in "$YOUR_CERTIFICATE".der -inform DER -out "$YOUR_CERTIFICATE".pem
```

3. Next you will want to move this file to the configuration directory for IKEv2, but before you do, it is
   important that you decide upon a naming scheme for this file. See `man iked` for more info about the
   available name schemes and locations. For our file we have chosen the "UFQD", so we copy it to the
   `/etc/iked/pubkeys/ufqdn` folder.

```bash
sudo cp "$YOUR_CERTIFICATE".pem /etc/iked/pubkeys/ufqdn/"$USERNAME"@"$FQDN"
```

- [client ikev2](https://www.openbsd.org/faq/faq17.html#clientikev2)
- [macOS ikev2](https://protonvpn.com/support/macos-ikev2-vpn-setup/)

### Wireguard Configuration

Configuring OpenBSD's native Wireguard support is rather odd if your acustomed to running an OpenBSD system.
This because unlike Linux used to be, where configuration of interfaces took place with the `ifconfig` command
(now `ip addr set`), OpenBSD relies on a file based configuration (i.e. `hostname.em0`). EXCEPT, when it comes
to configuring Wireguard, OpenBSD allows the use of `ifconfig` to configure the interface. As not usual, see `man
ifconfig` for detailed information for executing the following command.

1. To set up a wireguard interface (`wg0`) with ifconfig, use the following command.

```bash
sudo ifconfig wg1 create wgkey "$YOUR_PRIVATE_KEY" wgport "$YOUR_DESIGNATED_PORT" wgpeer "$YOUR_PUBLIC_KEY" wgaip 0.0.0.0/0 wgendpoint "$ENDPOINT_IP" "$ENDPOINT_PORT" 
```



### Reference Links

- [OpenVPN Client](https://astro-gr.org/openbsd-openvpn-client/)
- [Clein OpenVPN](https://umgeher.org/posts/2022/09/openbsd-client-openvpn.html)
