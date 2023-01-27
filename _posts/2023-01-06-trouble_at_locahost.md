```txt

#  _____                _     _              _
# |_   _| __ ___  _   _| |__ | | ___    __ _| |_
#   | || '__/ _ \| | | | '_ \| |/ _ \  / _` | __|
#   | || | | (_) | |_| | |_) | |  __/ | (_| | |_
#   |_||_|  \___/ \__,_|_.__/|_|\___|  \__,_|\__|
#
#  _                    _ _               _
# | |    ___   ___ __ _| | |__   ___  ___| |_
# | |   / _ \ / __/ _` | | '_ \ / _ \/ __| __|
# | |__| (_) | (_| (_| | | | | | (_) \__ \ |_
# |_____\___/ \___\__,_|_|_| |_|\___/|___/\__|
#
```

## Trouble at Localhost

My efforts and troubles attempting to resolve an issue a 1st grader could handle.

### Sudo Error: `sudo:unable to resolve host myhost: name or service not known`

Made some major changes to my local network configuration. I swapped carriers and removed an old firewall
router that had seen the last of it's days, and I purchased a new domain for personal use. All of which meant
the computers connected to the network had to be reconfigured to accept all the above changes. No probliem,
right? Well that would be wrong.

My desktop manged to make the change like butter, but a remote box that I use did not like the
changes one bit. These are the changes I made:

1. Added `supersede dns-name-servers 127.0.2.1`, to prevent dhclient from overwriting my settings in
	 `resolv.conf` that allows the use of dnscrypt-proxy.
2. Changed hostname `/etc/hostname` to `myhost.newdomain.new`, then changed it to `myhost` to align with
	 documentation.
3. Then everywhere in my network configuration I changed `myhost.olddomain.old` to `myhost.newdomain.new`.

Then the error hit, `sudo:unable to resolve myhost`...

### Resolution attempts

The most probable cause of this error is a misconfigured `/etc/hosts` file, but it appeared to be fine.

```conf
127.0.0.1    localhost
127.0.1.1    myhost

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

The man page was consulted to ensure this was correct, and it suggested that hosts should look like:

```conf
# For localhost entry
127.0.0.1    localhost

# For canonical host name paired with localhost (Whatever the hell that means.)
127.0.1.2    myhost.newdomain.new myhost

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
I have read forum and blog entries that suggest to use `127.0.0.1 myhost` or `127.0.0.1 myhost.newdomain.new
myhost`, but upon later review, I believe these suggestions are erroneous.
