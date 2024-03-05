```text
#  ____            _                   ____                  _
# / ___| _   _ ___| |_ ___ _ __ ___   / ___|  ___ _ ____   _(_) ___ ___
# \___ \| | | / __| __/ _ \ '_ ` _ \  \___ \ / _ \ '__\ \ / / |/ __/ _ \
#  ___) | |_| \__ \ ||  __/ | | | | |  ___) |  __/ |   \ V /| | (_|  __/
# |____/ \__, |___/\__\___|_| |_| |_| |____/ \___|_|    \_/ |_|\___\___|
#        |___/
#  __  __
# |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___
# | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
# | |  | | (_| | | | | (_| | (_| |  __/ |  \__ \
# |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
#                           |___/
#
```

## System Service Managers

A system service manager, often referred to as a system service daemon, is a daemon that manages other service
providing daemons that run on the system level. System services start on boot and end on shutdown or reboot,
and provide services like web servers, virtual machines, databases, desktop environments, audio servers, etc,
etc...They are a key component of the modern operating system, and being such they come in various forms. The
limiting factor as to which service managers are available is kernel dependent. Furthermore, there can only
one primary/default service manager. 

In most unix systems the service manager has remained the same throughout time, rc.d. Closed source operating
systems, such as windows and macintosh, have their own service manager, and those service managers are usually 
hardcoded. Meaning, it might be possible to change them, but the outcome will more than likely be extremely
undesirable, and come at a great expense. Linux has much more flexibility over selection of preferred default
service managers than the rest, although the default service manager is usually distro specific.

### Linux Service Managers

Not too long ago, Sys-V was the most commonly used service manager amongst linux operating environments, but
with the passing of time the popularity of Sys-V has faded, and SystemD is now overwhelmingly the most commonly
servicce manager for linux. Although, popularity does not include superiority, as there are a number of linux
enthusiasts who believe SystemD has become too bloated and heavy. There is even a popular version of debian
with SystemD replaced by Sys-V called Devian. 

"Outlying" distrobutions such as Alpine and Gentoo, prefer the linux native version of rc.d, called OpenRC.
OpenRC is also found in many versions of embedded linux due to its small size and speed. Then there are the
distrobutions who have to be different from everyone else, which is the case of Void Linux, who uses runit. 

#### SystemD

##### User Level Services

An interesting feature of SystemD is that it allows users level services. This is a rather convenient feature,
as it allows services to be managed on a per user basis, allowing services to run without requiring
superuser permissions, which in turn makes these services more secure.

Enabling this feature is quite easy, as the user just needs to execute `systemctl` with the `--user` flag, and
if the service needs to be run immediately, the `--now` flag can be added.

```bash
systemctl --user --now enable pipewire
```

##### Masking Services

Additionally allows "masking" services. To mask a service, means to link the service process to `/dev/null`.
Here is a quick example:

```bash
systemctl --user mask pipewire.service
```
