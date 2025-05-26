```text
#  ____  _____
# |  _ \|  ___|
# | |_) | |_
# |  __/|  _|
# |_|   |_|
#
```

PF: Packet Filter
==================

Forward
--------

A word of warning. Understanding the nuances of your operating system is critical in the proper configuration
of PF. Although PF grew out of the OpenBSD project, it is implemented in nearly, if not all, of the BSD's. I
imagine it could be implemented in OpenIndiana as well, and might be mistaken, but vaguely remember seeing a
blip that referenced it's use on Haiku. Funny as it is, the beg three are some of the few operating systems
which are not capable of running PF, due to their kernel limitations.

What might work in a FreeBSD implementation, might not work in the OpenBSD implementation, so please take this
into consideration.

The purpose of this wiki entry is to clarify the meaning of keywords in configuration of PF, and provide a
"only slightly better than average" pf implementation. So without further ado, here is pf.

### Section tasks

- [ ] Break down the configuration over multiple sections.
- [ ] Provide service based snippets.
- [ ] Elaborate on hardening strategies.
- [ ] Include a list of provided variables.

### Keywords

| keyword   | type         | meaning                                                  | example |
| -------   | ----         | -------                                                  | ------- |
| pass      | Action       | pass the packet to the kernel for processing             |         |
| block     | Action       | Either drops or returns the packet                       |         |
| drop      | block policy | Drops the packets immediately / ignores it               |         |
| return    | block policy | Returns the packet to the source.                        |         |
| in        | Direction    |                                                          |         |
| out       | Direction    |                                                          |         |
| log       | Parameter    | Initiates state dependent logging of packet              |         |
| quick     | Parameter    | perform action and do not attempt to match further rules |         |
| interface | device       | Preceeded by "on" keyword.                               |         |
| egress    | device       | Group of interfaces that possess a the default route     |         |

### An Example of a Basic Configuration

```conf
ext_if="vio0"

allowed_tcp="{ 53, 2222, ssh, smtp, submission, smtps, imap, imaps, pop3, pop3s, www, https, 11335 }"
icmp_types = "{ echoreq, unreach, timex }"
# RFC 4890: Recommendations for Filtering ICMPv6 Messages in Firewalls
icmp6_types = "{ echoreq, unreach, timex, toobig, paramprob, neighbrsol }"

table <whitelist> persist file "/var/pf/whitelist.txt"
table <pfbadhost> persist file "/var/pf/badhost.txt"
table <sshguard> persist

set ruleset-optimization basic
set optimization normal
set limit { states 200000, frags 200000, src-nodes 100000, table-entries 350000 }

set reassemble yes

set block-policy drop

set loginterface $ext_if

set skip on lo

match in all scrub (no-df random-id)

antispoof for $ext_if

block in quick proto tcp from <sshguard>
block drop in log quick on $ext_if from <pfbadhost>
block return in log all

pass quick inet proto icmp icmp-type $icmp_types max-pkt-rate 100/10
pass quick proto ipv6-icmp from any to any max-pkt-rate 100/10

# Whitelist
pass quick from <whitelist> to any flags any keep state

# allow SSH, SMTP, POP3, IMAP etc from allowed_tcp ports list
pass in quick on $ext_if proto tcp from any to ($ext_if) port $allowed_tcp
pass out quick on $ext_if proto udp from ($ext_if) to any port { ntp, domain }

pass out quick on $ext_if proto tcp from ($ext_if) to any port { smtp, www, https }

# Rspamd needs this
pass out quick on $ext_if proto tcp from ($ext_if) to any port { www, https }
```

### An Example of A Working Configuration

Until this moment, we have never shared any of our pf configurations with another living soul. This was due
partly to concerns of maintaining security, and partly out of fear of being criticised for possessing a
pathetic pf configuration. 

#### Macros

First set up your macros. Jargon is important in computer science, so be sure to refer to these as "macros" and not variables.

```conf
# REMEMBER LAST MATCH WINS!
# =================================================================================
## Local Macros
# ---------------------------------------------------------------------------------
int_if = "lo0"
ext_if = "msk0"
tinc_if = "tun0"
wg_if = "wg0"

intnet = $int_if:network
extnet = $ext_if:network
tincnet = $tinc_if:network
wgnet = $wg_if:network

icmp_types = "{ echoreq, unreach }"
table <bruteforce> persist
table <rfc6890> { 0.0.0.0/8 10.0.0.0/8 100.64.0.0/10 127.0.0.0/8 169.254.0.0/16 \
                  172.16.0.0/12 192.0.0.0/24 192.0.0.0/29 192.0.2.0/24 192.88.99.0/24 \
		  192.168.0.0/16 198.18.0.0/15 198.51.100.0/24 203.0.113.0/24 \
		  240.0.0.0/4 255.255.255.255/32 }

dns_server = "{ 127.0.0.1 }"

martians = "{ 127.0.0.0/8, 192.168.0.0/16, 172.16.0.0/12, \
             10.0.0.0/8, 169.254.0.0/16, 0.0.0.0/8, \
	     255.255.255.255/32, 240.0.0.0/4 }"

lan_net = "{ 192.168.1.0/24 }"
```

#### Default Rules

Here is where you want to establish your "default" policy, because everything that follows, will override
it.

```conf
# ---------------------------------------------------------------------------------
# General Settings
# ---------------------------------------------------------------------------------

# increase default state limit from 10'000 states on busy systems
set limit states 500000

# Drop hanging connections aggressively
set optimization aggressive

set block-policy drop

set loginterface egress

# ----------------------------------------------------------------------------------
# Opening rulesets
# ----------------------------------------------------------------------------------

# Table containing all IP addresses assigned to this host.
table <firewall> const { self }

set skip on lo0

## Turning on scrubbing to help with fragmentation
match in all scrub (no-df max-mss 1440)

## The yin-yang statement:
## Blocks packets that lack a state, and establishes the initial state of packets.
block return	# block stateless traffic
pass		# establish keep-state <--- ??? What does this do?

## Bloack IPV6
block quick inet6

## Block all incoming to ext_if
# block return log on ext_if all # <-- This did not work.
block all # <-- This did.
## =================================================================================
# Kill off zombie packets
## =================================================================================

# This is not the same as antispoofing.
# urpf = Unicast Reverse Path Forwarding
# These are packets originating from a network that holds the route back.
# block in quick from urpf-failed to any	# use with care... but why?

# Establish Antispoofing measures
# Rules created by the antispoof directive interfere with packets
# sent over loopback interfaces to local addresses.
# One should pass these explicitly.
# Meaning not with the antispoof directive.
antispoof for ext_if inet
antispoof for wg_if inet
antispoof for int_if

# Anything not possessing a back link to block
block in from no-route to any

# Block noise that could be created by a cable modem.
block in quick on $ext_if from any to 255.255.255.255

block in log quick on $ext_if from $martians to any

## =================================================================================
# Block unroutable
## =================================================================================
# Whether the following rules work, is suspect.
# block in quick on egress from <rfc6890>
# block return out quick on egress to <rfc6890>
## =================================================================================
# Introductionary rules
## =================================================================================

## Handle ICMP Packets
pass on $ext_if inet proto icmp all icmp-type 8 code 0

## sshguard
table <sshguard> persist
block in proto tcp from <sshguard>
```

#### Base level Ruleset

```conf
# -----------------------------------------------------------------------------------
# Beginning Regular Rules
# -----------------------------------------------------------------------------------
# Rule  0 (msk0)
block in log quick on $ext_if inet from self to any label "RULE 0 -- DROP "  

# Rule  1 (lo) -- rule generation on anything internal is a bad idea
# pass quick on lo0 inet from any to any label "RULE 1 -- ACCEPT "  

# Rule  2 (global)
# SSH Access to the host; useful ICMP
pass in quick inet proto tcp from any to self port 22 flags any label "RULE 2 -- ACCEPT ssh"  
#pass in on egress proto tcp to port {22} keep state (max-src-conn 15, max-src-conn-rate 3/1, overload <bruteforce> flush global)

# Rule  3.5 (global) -- Pass everything out 
# liberator:Policy:3: warning: Changing rule direction due to self reference
pass out quick inet from self to any label "RULE 3 -- ACCEPT "  

# Rule  4 (global)
block log quick inet from any to any label "RULE 4 -- DROP "  
# 
# Rule  fallback rule
#    fallback rule 
block quick inet from any to any no state label "RULE 10000 -- DROP "  

# ----------------------------------------------------------------------------------
# Rules for Virtualization
# ----------------------------------------------------------------------------------

# Moving up rule for virtualization in case it is blocked from anything below.
# match out on egress inet from vport0:network to any nat-to (egress)
# pass in proto { udp tcp } from vport0:network to any port domain rdr-to $dns_server port domain

# rules for vmd(8) - NAT and DNS forwarding for VMs (100.64.0.0/10 default)
# pass out on egress from 100.64.0.0/10 to any nat-to (egress)
# pass in proto udp from 100.64.0.0/10 to any port domain \
#    rdr-to $dns_server port domain

## I2P
# pass quick inet proto tcp from any to any port 4955 label "RULE 225 -- i2pd-any"
# pass quick inet proto udp from any to any port 4955 label "RULE 226 -- i2pd-any"

## Tinc
# pass quick on egress inet proto tcp to 192.168.1.99 port 9317 label "RULE 233 -- tinc-any"

## allowing traceroute
pass out quick on egress inet proto udp to port 33433:33626

#### Commentary

Include a commentary in your `pf.conf`, that way when you are exhausted and running on less than four hours of
sleep, you won't have to remember anything to modify your pf file.

# ==============================================================================
# Port Macros
# -----------
# What was defined:
# ----------------- 
# 1. Unknown Webports = nntp, auth, 5232, 655, 631, 1194, 5222, 6920, 6956, 1410, 22000, 21027
# 2. udp services = 1194, 631, 655, 1410, 6956, 21027, 41494, 64164
# -------------------------
# By Service:
# -------------------------
# Cups = 631 UDP
# Tinc = 9317 TCP
# OpenVPN = 1194
# Unknown = 46662, 6920, 6922, 6956. 41494, 64164
# PulseAudio = 1410
# Syncthing = 22000 TCP & 21027 UDP
# Bittorrent = 6881 through 6889 BOTH
# RealAudio = 7008 & 7012
# Unknown + Blocked due to vulenerability: 5232
# XMPP = 5222 BOTH
# Pulse = 4713
# Wireguard via ProtonVPN = 24021
# ==============================================================================

########################
# Variable Definitions #
########################
# Need to define each of these with a variable, so they can be disabled and enabled.
```

#### Setup services

It is easiest if you setup your services as macros, and bundle them together. So, you only have to write one
rule to manage numerous services.

```conf
## ===============================================================================
webserver = "{ 127.0.0.1 }"
router = "{ 192.168.1.1 }"
webports = "{ http, https }"
nameservers = "{ 127.0.0.1, 192.168.1.1 }"
wg_out = "{ 24021 }"
client_out = "{ domain, http, https, 8080, ntp }"
## Apparently there is no rule for client_in so commented out.
client_in = "{ 9317 }"
udp_services = "{ domain, ntp }"
p2p_services_tcp = "{ 6881:6889 }"
# p2p_services_udp = "{ 18292 }"

####################################################
# Magical Mystery Configuration for Local Services #
# I was not stoned writing this, just bored and    #
# really really tired.                             #
####################################################

pass quick proto { tcp, udp } from $intnet to port $udp_services
pass quick log inet proto icmp all icmp-type $icmp_types
pass quick proto tcp from $intnet to port $client_out
pass quick proto { tcp, udp } from $extnet to port $client_in
## Not running any webserver
# pass quick proto { tcp, udp } to $nameservers port domain
# pass proto tcp to $webserver port $webports

## Enable and Allow p2p networking...I think
pass quick proto tcp to port $p2p_services_tcp
# pass quick proto udp to port $p2p_services_udp

## -----------------------------------------------------------
# Explicitly block windows smtp packets
## -----------------------------------------------------------
block in on $ext_if proto tcp from any \
    os { "Windows 95", "Windows 98" } to any port smtp
```

#### Service specific rules.

```conf
## ---------------------------------------------------------------
# Tinc Rules
## ---------------------------------------------------------------
pass out on egress inet from $tincnet nat-to $ext_if

## ---------------------------------------------------------------
# Wireguard Rules
## ---------------------------------------------------------------

# Allow all on WireGuard interface
pass out on egress inet from $wgnet nat-to $ext_if
```

#### Close the gap

Cut off services and daemons that can use the network, but REALLY shouldn't.

```conf
# ===========================================================
# This goes last
# -----------------------------------------------------------

# By default, do not permit remote connections to X11
block return in on ! lo0 proto tcp to port 6000:6010

# Port build user does not need network
block return out log proto {tcp udp} user _pbuild
```

### SpamD Snippet for SMTP

Prerequisites for the following configuration would be the file `/etc/mail/nospamd`, which is a text file
containing a list of hosts who require bypassing the spamd altogether.

```conf
table <spamd-white> persist
table <nospamd> persist file "/etc/mail/nospamd"
pass in on egress proto tcp to any port smtp divert-to 127.0.0.1 port spamd
pass in on egress proto tcp from <nospamd> to any port smtp
pass in log on egress proto tcp from <spamd-white> to any port smtp
pass out log on egress proto tcp to any port smtp
```

### Mail server specific configuration rules

An example of rules used in a pf configuration file in order to allow traffice from mail servers.

```conf
# Create a marco for the mail services
mail_in = {smtp, submission, smtps, imap, imaps, pop3, pop3s}

# Establish Log interface, missing from above.
set loginterface $ext_if

# Establish persistent tables
table <spamd> persist
table <spamd-allow> persist

# Pass spamd allow list
pass quick log on $ext_if inet proto tcp from <spamd-allow> to $ext_if port smtp -> 127.0.0.1 port 25

# Pass webmail servers
rdr pass quick log on $ext_if inet proto tcp from <gmail> to $ext_if port smtp -> 127.0.0.1 port 25

# pass submission messages.
pass quick log on $ext_if inet proto tcp from any to $ext_if port submission modulate state

# Pass unknown mail to spamd
rdr pass log on $ext_if inet proto tcp from {!<spamd-allow> <spamd>} to $ext_if port smtp -> 127.0.0.1 port 8025

# Open up imap
pass in quick on $ext_if proto tcp from any to ($ext_if) port $mail_in
```

### Mail Server Configuration with SpamD integration

Now here is an example of combining the two previous examples together.

> [!info] Outbound rule
> Do not forget, no outbound rules are needed, because your server should already be configured to allow
> outbound traffic.

```conf
# Define macros
main_in_sec = {smtps, imaps}
mail_in = {smtp, submission, smtps, imap, imaps}

# Define Tables
table <spamd-scan> persist
table <spamd-noscan> persist file "/etc/mail/nospamd"

# Divert to spamd is only needed for smtps, since we do not plan on offering smtp.
pass in on egress proto tcp to any port smtps divert-to 127.0.0.1 port spamd

# Allow noscan to directly talk to mail server
pass in on egress proto tcp from <spamd-noscan> to any port smtps

# Pass diverted traffic back to smtp
pass in log on egress proto tcp from <spam-scan> to any port smtps

# Pass that shit back out
pass out log on egress proto tcp to any port smtp
```

-----

### Reference Material

- [Calomel pf configuration guide](https://calomel.org/pf_config.html)
- [A Dummy's Sample pf.conf](https://gist.github.com/nathwill/9703175)
- [Sample PF Configuration for OpenBSD Release](https://docs.ircnow.org/openbsd/pfstable/)
- [IRCNow PF Guide](https://docs.ircnow.org/openbsd/pf/)
- [tightening pf conf even further for my mail server](https://forums.freebsd.org/threads/tightening-pf-conf-even-further-for-my-mail-server.89515/)
- [Setting up your own mail server on FreeBSD](https://cloudfrik.com/blog/server/setting-up-your-mail-server-on-freebsd/)
- [Dan's PF Page](https://www.benzedrine.ch/pf.html)
