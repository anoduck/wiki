```text
# __        ______ _____
# \ \      / /  _ \___ /
#  \ \ /\ / /| |_) ||_ \
#   \ V  V / |  __/___) |
#    \_/\_/  |_|  |____/
#
```

## WifiPumpkin3: A more definitive guide

Wifipumpkin is a wireless attack framework, that creates an rogue access point for enticing the target to connect
to. This access point is then used to launch attacks from. It's the defacto program of choice to perform attacks of 
this type.

Although it does offer good documentation, this documentation is not nearly as explanative as one would hope, leaving 
many critical topics and characteristics untouched. For instance, the documentation does not mention whether
to treat this application as a turn-key solution, or whether it should be used to create a customized
offensive framework. Even the creator admitted ninety nine percent of users are unable to get the
application's internal dhcp server to work. It is in respects to this lack of definitey, WifiPumpkin3 is a
solution for a problem with an unknown number of parts, arranged in an unknown configuration. 

The only way to provide definition to this enigma is to review the source code and break it down into it's
individual parts.


### Source Code Structure

<details>

<summary> Repository Layout </summary> 

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
</details>

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

#### A better tutorial

Finally, I was able to discover a tutorial that went beyond the basics. The link to it is below. 

- [WifiPumpkin3 Dangerous Access Point](https://www.kalilinux.in/2020/12/wifi-pumpkin-3-dengerous-access-point.html)

The tutorial goes over installing an additional captiveflask for use as a captive portal. Unfortunately, after
this the tutorial is nearly identitical to the other tutorials, the end result being a failure of WifiPumpkin3
to issue addresses to clients via it's built in dhcp server.

### Current Status: Not Working

In our attempted implementation of WifiPumpkin3 we encountered an issue with it's internal DHCP server, where
the DHCP server never issued clients an IP address, and the client eventually gave up and closed it's
connection. This process was monitored via wireshark, and absolutely zero packets were transmitted from
WifiPumpkin3 during this process. All traffic was generated by the client to the WP3 instance. This leads one
to the conclusion that WP3 is not aware of the client being present. The developer was contacted and related 
that this error was the result of a bad configuration, but was unsure of exactly what was causing the incident.

Later on, an attempt to build the Docker image was tried, and failed with a `/bin/sh - permission denied`
error.