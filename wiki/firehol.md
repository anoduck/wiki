```text
#  _____ _          _           _
# |  ___(_)_ __ ___| |__   ___ | |
# | |_  | | '__/ _ \ '_ \ / _ \| |
# |  _| | | | |  __/ | | | (_) | |
# |_|   |_|_|  \___|_| |_|\___/|_|
#
```

## Firehol: Now, that's something different

THIS PAGE IS A WIP!

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

__IMPORTANT_NOTE:__ Firehol is way more complex than originally assumed when this tutorial was first written.
Although ample documentation is provided, it is rather lean in our honest opinion, and could use further
expansion to grant clarity.

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

### Firehol configuration: A deeper dive

Firehol is an entire suite of tools provided to work with modern linux systems. When we say "modern linux
systems", we are referring to the current effort of linux developers to embrace virtualization and virtualized
solutions. Although vague in definition, the result of this effort is linux's virtual namespaced networking
stack. Such tools created for and currently being adopted to implement are iproute2, iw, and numerous
virtualized networking protocol to name a few. 

To help manage this stack, Firehol provides the following tools: iprange, firehol, fireqos, update-ipsets, and
vnetbuild. Although the Firehol team does not maintain or develop the ipsets toolset it does implement many
features to work alongside ipsets. Ipsets, being self exlanative, is a tool to define sets of ip addresses
that can be used in network configurations and firewall configurations.

Firehol configuration files are an oddity as far as configuration files are concerned, because they allow the
user to define their own variables and do accept some basic forms of shell scripting language. How firehol is
able to distinguish between user defined variables and it's own syntax is not really known, but it works.

#### Configuration file structure

The structure of your firehol configuration is very important, as firehol will match rules and directives in a
first come first serve policy, it will also not parse a configuration file if it is not structured correctly.
Although not stated in the firehol configuration tutorial, firehol configuration files consist of the
following sections:

1. Versioning definition
2. Service Definitions
3. Shell Variables
4. Helper Directives
5. Interface Definitions
6. Router Definitions

We will take each of these one at a time and see if we can make sense of them.

##### Versioning definition

Firehol allows users to create versioning labeling for their configurations. See docs on how to do this.

##### Service Definitions

The firehol documentation states that you can create service definitions in one of two locations, you can
place them in the top of your configuration file (which did not work for us) or place them in their own file
within the `/etc/firehol/services` directory (which we did not care to try) with a `.conf` file extension.
Service definitions have a required labeling structure, that defines a) whether it is a client or server, b) the
name of the service, and c) followed by `_ports`. So for our attempt at adding definitions for the tinc vpn
service, our custom definitions looked like so.

```conf
server_tinc_ports="tcp/9933 udp/9933"
client_tinc_ports="tcp/9933 udp/9933"
```

The examples provided in the firehol documentation employ the use of the keywork "default", what actually that
is or what it does is not defined.

If you do decide to add your own service definitions to the `/etc/firehol/services` directory, it needs to be
noted that each file must begin with `#FHVER: 1:213`. More information about this can be found on the [firehol
service definition page](https://firehol.org/guides/adding-services/)

##### Shell variables

Shell variables should be self explanatory at this point. When incorporated into your configuration file, the
only difference is that the variables must be encased in a pair of curly brackets preceded by a `$` sign. So
for example, a variable defining you local lan network would look something like this `"${lan_net}`. 

```bash
LAN_NET="192.168.0.0/24"

interface eth0 lan src "${LAN_NET}" dst 192.168.0.211
    server http accept
    client all accept
```

##### Helper Directives

Helper directives are dependent on which of the many directives you try to use.

##### Interface Definitions

Interface definitions have nothing to do with anything else accept the actual interfaces on the firewall. They
exist to protect the firewall.

##### Router Definitions

At least three times in the firehol tutorial, it mentions that router definitions can get confusing, and no truer
words have been spoken before in technical literature. Confusing indeed. 

Router definitions define the routes packets travel through the host system of the firewall to their eventual
destination. You only need be concerned with requests, firehol will handle the replies automatically for you.

### References

- [Required reading: Intro to firehol](https://firehol.org/guides/firehol-welcome)
- [The only full example of firehol.conf provided in the repo](https://github.com/firehol/firehol/blob/master/examples/lan-gateway.conf)
- [A script to scrape adblock urls](https://github.com/firehol/firehol/blob/master/examples/adblock.sh)
- [An example of fireqos from the repo](https://github.com/firehol/firehol/blob/master/examples/fireqos.conf)
