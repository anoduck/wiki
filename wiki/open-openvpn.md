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

Configuring OpenBSD's native Wireguard support is rather odd, because it can be performed in any number of
different ways, and all would be correct. It can be configured from the command line using the `ifconfig`
command, in a `hostname.if` file as other interfaces are configured, on the command line using the `wg`
command, and finally with a configuration file using the `wg-quick` command. 

#### Ifconfig

If you are curious about setting it up using ifconfig, then please see the man page for ifconfig for more
instructions on how to do this.

1. To set up a wireguard interface (`wg0`) with ifconfig, use the following command.

```bash
sudo ifconfig wg1 create wgkey "$YOUR_PRIVATE_KEY" wgport "$YOUR_DESIGNATED_PORT" wgpeer "$YOUR_PUBLIC_KEY" wgaip 0.0.0.0/0 wgendpoint "$ENDPOINT_IP" "$ENDPOINT_PORT" 
```

#### hostname.if 

You can break the above command down and create a hostname.if file like so. 

```conf
inet "$YOUR_CLIENT_IP" "$CLIENT_IP_SUBMASK" NONE
wgkey "$YOUR_PRIVATE_KEY" \
  wgport "$YOUR_DESIGNATED_PORT" 

wgpeer "$YOUR_PUBLIC_KEY" \
  wgaip 0.0.0.0/0 \
  wgendpoint "$ENDPOINT_IP" "$ENDPOINT_PORT" 

!route "$ROUTE rules here"
```

But there are far better ways to configure the interface.

#### Hybrid configuration

The best strategy is to perform a hybrid configuration, where a `hostname.if` file is created, and the `wg`
command used to configure the interface.

```bash
[#] ifconfig wg0 create description wg-quick: wg0 
[#] wg setconf wg0 /dev/fd/63 
[#] ifconfig wg0 inet "$CLIENT_IP"/32 alias 
[#] ifconfig wg0 mtu 1420 
[#] ifconfig wg0 up 
[+] resolvd is not running, DNS will not be configured 
[#] route -q -n add -inet 0.0.0.0/1 -iface "$CLIENT_IP" 
[#] route -q -n add -inet 128.0.0.0/1 -iface "$CLIENT_IP" 
[#] route -q -n delete -inet "$ENDPOINT_IP" 
[#] route -q -n add -inet "$ENDPOINT_IP" -gateway "$LOCAL_EXT_IP"
```

```bash
inet "$CLIENT_IP" 255.255.255.255 alias
mtu 1420
up
!wg setconf wg0 /etc/wireguard/wg0.conf
!route -q -n add -inet 0.0.0.0/1 -iface "$CLIENT_IP" 
!route -q -n add -inet 128.0.0.0/1 -iface "$CLIENT_IP" 
!route -q -n delete -inet "$ENDPOINT_IP" 
!route -q -n add -inet "$ENDPOINT_IP" -gateway "$LOCAL_EXT_IP"
```

### Reference Links

- [OpenVPN Client](https://astro-gr.org/openbsd-openvpn-client/)
- [Clein OpenVPN](https://umgeher.org/posts/2022/09/openbsd-client-openvpn.html)
- [OpenBSD Wireguard](https://marcocetica.com/posts/wireguard_openbsd/)
