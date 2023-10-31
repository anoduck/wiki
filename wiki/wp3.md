```text
# __        ______ _____
# \ \      / /  _ \___ /
#  \ \ /\ / /| |_) ||_ \
#   \ V  V / |  __/___) |
#    \_/\_/  |_|  |____/
#
```

## WifiPumpkin3: A more definitive guide

To prove to you how little information is available regarding the configuration and deployment of Wifipumpkin,
this unfinished and derelict wiki page ranks 4th in the duckduckgo search results. It isn't even finished, and
was planned to be scraped entirely. Yet it made the top 5 search results. 

### Intro

Wifipumpkin is a wireless attack framework, that creates an rogue access point for enticing the target to connect
to. This access point is then used to launch attacks from. It's the defacto program of choice to perform attacks of 
this type.

#### Documentation is left wanting...

Although it does offer good documentation, this documentation is not nearly as explanative as one would hope, leaving 
many critical topics and characteristics untouched. For instance, the documentation does not mention whether
to treat this application as a turn-key solution, or whether it should be used to create a customized
offensive framework. Even the creator admitted ninety nine percent of users are unable to get the
application's internal dhcp server to work. It is in respects to this lack of definitey, WifiPumpkin3 is a
solution for a problem with an unknown number of parts, arranged in an unknown configuration. Not to mention
the documentation does not fully embrace the gift of good grammar, and many sentences are broken. 

The way to provide definition to this enigma is to review the source code and break it down into it's
individual parts.


### Source Code Structure

Below is a tree of the contents of the WifiPumpkin3 src directory.

```text
├── __init__.py
├── __main__.py
├── _author.py
├── _version.py
├── core
│   ├── __init__.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── console.py
│   │   ├── platforms.py
│   │   ├── terminal.py
│   │   ├── threads.py
│   │   └── uimodel.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── globalimport
│   │   │   └── __init__.py
│   │   └── setup.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── defaultcontroller.py
│   │   ├── dhcpcontroller.py
│   │   ├── dnscontroller.py
│   │   ├── extensioncontroller.py
│   │   ├── mitmcontroller.py
│   │   ├── proxycontroller.py
│   │   ├── uicontroller.py
│   │   └── wirelessmodecontroller.py
│   ├── lib
│   │   ├── __init__.py
│   │   └── mac_vendor_lookup.py
│   ├── packets
│   │   ├── __init__.py
│   │   ├── dhcpserver.py
│   │   ├── dnsserver.py
│   │   ├── dnsspoofNF.py
│   │   ├── listener.py
│   │   ├── network.py
│   │   └── wireless.py
│   ├── servers
│   │   ├── __init__.py
│   │   ├── dhcp
│   │   │   ├── __init__.py
│   │   │   ├── dhcp.py
│   │   │   ├── dhcpdServer.py
│   │   │   └── pyDHCP.py
│   │   ├── dns
│   │   │   ├── __init__.py
│   │   │   ├── DNSBase.py
│   │   │   └── pyDNSServer.py
│   │   ├── mitm
│   │   │   ├── __init__.py
│   │   │   ├── mitmmode.py
│   │   │   ├── responder.py
│   │   │   └── sniffkin3.py
│   │   ├── proxy
│   │   │   ├── __init__.py
│   │   │   ├── captiveflask.py
│   │   │   ├── no_proxy.py
│   │   │   ├── proxymode.py
│   │   │   └── pumpkin_proxy.py
│   │   └── rest
│   │       ├── __init__.py
│   │       ├── application.py
│   │       ├── blueprints
│   │       │   ├── __init__.py
│   │       │   └── restapi
│   │       │       ├── __init__.py
│   │       │       ├── accesspoint.py
│   │       │       ├── authenticate.py
│   │       │       ├── commands.py
│   │       │       ├── logger.py
│   │       │       ├── plugins.py
│   │       │       └── proxies.py
│   │       └── ext
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── configuration.py
│   │           └── exceptions.py
│   ├── ui
│   │   ├── __init__.py
│   │   ├── dhcpConfig.py
│   │   ├── plugins.py
│   │   └── uimode.py
│   ├── utility
│   │   ├── __init__.py
│   │   ├── banners.py
│   │   ├── collection.py
│   │   ├── component.py
│   │   ├── constants.py
│   │   └── printer.py
│   ├── widgets
│   │   ├── __init__.py
│   │   ├── default
│   │   │   ├── __init__.py
│   │   │   ├── logger_manager.py
│   │   │   ├── plugins.py
│   │   │   └── session_config.py
│   │   └── docks
│   │       ├── __init__.py
│   │       └── dock.py
│   └── wirelessmode
│       ├── __init__.py
│       ├── docker.py
│       ├── karma.py
│       ├── restapi.py
│       ├── static.py
│       └── wirelessmode.py
├── data
│   ├── exceptions
│   │   ├── ap_mode_support_error.txt
│   │   ├── dhcp_server_dhcpd_not_found.txt
│   │   ├── dhcp_server_settings_error.txt
│   │   ├── dhcp_test_message.txt
│   │   ├── hostapd_message_error.txt
│   │   ├── interface_buzy_error.txt
│   │   └── iptables_path_not_found.txt
│   └── helps
│       ├── help_dhcpconf_command.txt
│       ├── help_extra_captiveflask.txt
│       ├── help_hostapd_config_command.txt
│       ├── help_info_command.txt
│       ├── help_install_customcaptiveflask.txt
│       ├── help_kill_command.txt
│       ├── help_mode_command.txt
│       ├── help_plugins_command.txt
│       ├── help_proxies_command.txt
│       ├── help_proxy_plugin_command.txt
│       ├── help_security_command.txt
│       ├── help_set_command.txt
│       ├── help_unset_command.txt
│       ├── help_wifideauth_add_command.txt
│       └── help_wifideauth_rm_command.txt
├── exceptions
│   ├── __init__.py
│   ├── base.py
│   └── errors
│       ├── __init__.py
│       ├── dhcpException.py
│       ├── hostapdException.py
│       ├── iptablesException.py
│       └── networkException.py
├── extensions
│   ├── __init__.py
│   ├── ap.py
│   ├── banner.py
│   ├── clients.py
│   ├── dhcpconf.py
│   ├── dhcpmode.py
│   ├── dump.py
│   ├── info.py
│   ├── kill.py
│   ├── plugins.py
│   └── proxies.py
├── modules
│   ├── __init__.py
│   ├── misc
│   │   ├── __init__.py
│   │   ├── custom_captiveflask.py
│   │   └── extra_captiveflask.py
│   ├── spoof
│   │   ├── __init__.py
│   │   ├── arp_spoof.py
│   │   └── dns_spoof.py
│   └── wifi
│       ├── __init__.py
│       ├── wifideauth.py
│       └── wifiscan.py
├── plugins
│   ├── __init__.py
│   ├── bin
│   │   ├── __init__.py
│   │   ├── captiveflask.py
│   │   └── sslstrip3.py
│   ├── captiveflask
│   │   ├── __init__.py
│   │   ├── DarkLogin.py
│   │   ├── flask_demo.py
│   │   ├── login_v4.py
│   │   ├── loginPage.py
│   │   └── plugin.py
│   ├── external
│   │   ├── __init__.py
│   │   └── sslstrip
│   │       ├── __init__.py
│   │       ├── ClientRequest.py
│   │       ├── CookieCleaner.py
│   │       ├── DnsCache.py
│   │       ├── DummyResponseTamperer.py
│   │       ├── PluginsManager.py
│   │       ├── ResponseTampererFactory.py
│   │       ├── ServerConnection.py
│   │       ├── ServerConnectionFactory.py
│   │       ├── SSLServerConnection.py
│   │       ├── StrippingProxy.py
│   │       └── URLMonitor.py
│   ├── pumpkinproxy
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── beef.py
│   │   ├── downloadspoof.py
│   │   ├── html_inject.py
│   │   ├── js_inject.py
│   │   └── no_chache.py
│   └── sniffkin3
│       ├── __init__.py
│       ├── default.py
│       ├── emails.py
│       ├── ftp.py
│       ├── hexdump.py
│       ├── httpCap.py
│       ├── image.py
│       ├── kerberos.py
│       └── summary.py
└── tree.txt
```

__Call Graphs__

These are two call graphs listing the flow of functions in the program. One with a depth of
three levels, and the other with four levels.

- [Callgraph 3 levels](../assets/img/out-lvl3.png)
- [Callgraph 4 levels](../assets/img/out-lvl4.png)

### The inefficient tutorial

Every tutorial includes the same basic example on how to run WifiPumpkin3. It is the introduction to
running pulp files, and running pulp commands from the terminal. It is boring, barely informative, and
makes the same mistake regarding pulp files. This tutorial shows the use of comments in pulp files, where
although not critical, these comments are echoed back into the terminal upon execution, and an error is
registered in the standard output.

```text
# Set interface
set interface wlan2
# set name of AP
set ssid Shifty_Susan
# Set noproxy plugin
set proxy noproxy
# Ignore pydns log
ignore pydns_server
# Start that shit (Admittedly, I added 'that shit')
start
```

After trying to run this, you will see that all comments are echoed back into the terminal, and an error
message is generated for them. So, it would be best to avoid using comments in pulp files all together.

Since writing this, a few more pulp files have appeared in the repository, which can act in their own was a
tutorials for new users.

### A tutorial of much improvement

As we all know, everything from India is really cool. Raj Chandel wrote the best tutorial I have seen to date.
It can be found [here](https://www.hackingarticles.in/wireless-penetration-testing-wifipumpkin3/).

Admittedly after reading Raj's tutorial myself, I am somewhat disappointed with WifiPumpkin3. I guess that I
expected it to be more of a one-stop solution for performing a rogue AP attack. 

Here is another tutorial page from [kalitutorials.com](https://kalilinuxtutorials.com/wifipumpkin3/), but not
nearly as good as the previous one.

### My configuration

For our purposes facilitating a captive portial would not be wise, as they tend to raise red flags for technologically savy individuals.
So our method of implementation must be as cladestine as possible. For this we shall primarily be relying upon
wifipumpkin's pumpkinproxy. 

#### Dealing with the disconnect

Immediately, we must deal with the issue of connectivity loss before preceding any further with wifipumpkin.
Because we are running wifipumpkin on a remote host, starting it instantly disconnects us from the remote host
and prohibits us from regaining connection. 

In wp3's configuration file `~/.config/wifipumpkin/config/app/config.ini` there are several configuration
settings that dictating how iptables is setup in order to correctly forward packets to and from the exterior interface and
the wireless network interface. Within these settings there are two varables, `inet` and `wlan`. These
variables are derived from the configuration settings, `interface` and `interface_net`, `interface` being the
interface used for the wireless network and `interface_net` being the device used for wireless communications. Ensure 
they are appropriately set. If desired, you may go ahead and replace the variables `inet` and `wlan` in the
iptable settings with their equivocal values. Doing this should correct the disconnection issue.

If you need some help correcting these iptable rules, please see [firewall](firewall).

#### Dhcp not working

For our configuration, using the builtin 'pydhcp_server' was never successful. The dhcp server never provided clients
with a ip address and would cause the client to time out and disconnect from the network. To resolve this two
things were done, the option to use the standardized isc-dhcp-server was enabled, and the network offered to
clients was reconfigured. 

Reconfiguring wp3 to offer a different network to clients than `10.0.0.0` was done brutally with two quick sed
commands, `sed -i 's/10.0.0/192.168.0/g' config.ini` and `sed -i 's/255.0.0/255.255.255/g' config.ini`. This changed all network 
configuration settings from `10.0.0.0` to `192.168.0.0` and all subnet settings from `255.0.0.0` to
`255.255.255.0`. This was primarily done because there is no need to establish a network that can accomodate 
16,777,214 clients, and there is not a moment in recollection where one can remember such a network being
offered.

Enabling wifipumpkin to use the isc-dhcp-server and disabling the 'pydhcp_server' is rather straightforward. The
setting to do this is in the configuration file, and is listed under `[accesspoint]`. Simply change the
setting `dhcpd_server=false` to `dhcpd_server=true` and `pydhcp_server=true` to `pydhcp_server=false`, and
your done.

#### No internet connection

First off, there might be several reasons why this occurs in your instance of wifipumpkin, but in our case
this was caused by a conflict in DNS server resolution. Our external interface was configured with a set of
dns servers that differed from wifipumpkin's dns resolution configuration. This meant clients were not able to
contact any dns servers, and as a result were not able to resolve any domain names. The resulting error was a
'no internet access available' message. 

Further research discovered the nameserver used to resolve domain names is google's `8.8.8.8` and `8.8.4.4`.
Which is problematic since this does conflict with local dns settings. Some thought will need to be invested
in order to mitigate this issue.
