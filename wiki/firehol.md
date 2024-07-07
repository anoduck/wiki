```text
#  _____ _          _           _
# |  ___(_)_ __ ___| |__   ___ | |
# | |_  | | '__/ _ \ '_ \ / _ \| |
# |  _| | | | |  __/ | | | (_) | |
# |_|   |_|_|  \___|_| |_|\___/|_|
#
```

## Firehol: Now, that's something different

If you have ever taken a survey of firewall technologies for linux, you will find a great abundance of
software intended to make configuration and setup of firewalls easier. Not being the biggest fan of iptables,
we can understand this. It is not that configuring iptables is complicated or difficult, but it is that
configuration of the linux firewall, netfilter, is tedious, timeconsuming, and cumbersome. It is also quite
easy to loose one's place while in process of doing so. This is due to the highly reptitive, but long, syntax
required to do so. This difficult smattering of flags and variables is required for each rule, every policy,
and to modify all the tables. So, it is no wonder why many have strived to discover another way of doing it.

Firehol is a suprisingly unique way of doing this, it includes features that we liked in other firewall
configuration technologies, and adds severl more well thought out capabilities. It should be no surprise to
the user that this is another creation from [Costa Tsaousis](https://github.com/ktsaou), who is the founder of
netdata. It shares many of the same "no hassle" magical traits that you find in the netdata technology. It
also takes on a different approach to building firewalls that one might dare to say is more reflective of the
real structure of networking firewalls. 

Firehol is also only one part of the firehol technology, as it is accompanied by fireqos, which is a traffic
shaping system.

Being pressed for time, we shall only provide a tiny dabble into how to use firehol.

### Configuration

Assuming you have firehol installed on a debian derivative system, the first thing you will need to do is open
up the file located at `/etc/default/firehol.conf` and uncomment line number 13 to enable firehol to run.

```conf
# FireHOL application default file
# sourced by the initscript `/etc/init.d/firehol'.
#

# START_FIREHOL(=NO|AUTO|YES) init script variable:
# - to disable firehol at startup set START_FIREHOL=NO (default)
#START_FIREHOL=NO
# - to handle firehol with a third-party machinery (like ifupdown)
# set START_FIREHOL=AUTO . This scheme empties the WAIT_FOR_IFACE
# list (see below)
#START_FIREHOL=AUTO
# - to effectively start firehol at startup set START_FIREHOL=YES
START_FIREHOL=YES # <-- Uncomment this line to enable firehol.


#
# See firehol-variables(5) manual page or FireHOL Manual
# for the full list of exportable variables that control the
# behaviour of FireHOL and their respective description.
#

# If you want to have firehol wait for an iface to be up add it here
WAIT_FOR_IFACE=""
# This list is set to the empty list in the START_FIREHOL=AUTO scheme.

# Disallow pre-established traffic to continue whilst the firewall is activated
FIREHOL_ESTABLISHED_ACTIVATION_ACCEPT=0
```

With that done, you are now ready fore firehol to generate a "beginner friendly" configuration file for you.
We say that is it "beginner friendly", because it comes with it's own pair of training wheels, and will not
lock you out unless you configure it to do so. 

#### Editing the configuration

The configuration file you just created will be unquestionably highly commented, and will provide a thorough
explanation of why what was generated where for what. It will identify the parts that you will need to change,
and other alterations you may or may not want to make. When you are satisfied, save the file as
`/etc/firehol/firehol.conf`, and issue the `sudo firehol try` command to have firehol review the file and test
out the rules you provided. If you have made an error, it will tell you where and how to change it. Once you
have a working configuration file, it will then prompt you to load the rules and enable the firewall by
pressing the enter key.

Then your done.
