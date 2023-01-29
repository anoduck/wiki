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

#### The Error

Made some major changes to my local network configuration. I swapped carriers and removed an old firewall
router that had seen the last of it's days, and I purchased a new domain for personal use. All of which meant
the computers connected to the network had to be reconfigured to accept all the above changes. No probliem,
right? Well that would be wrong.

My desktop manged to make the change like butter, but a remote box that I use did not like the
changes one bit. These are the changes I made:

1. Added `supersede dns-name-servers 127.0.2.1`, to prevent dhclient from overwriting my settings in
	 `resolv.conf` that allows the use of dnscrypt-proxy. Later removed, along with dnscrypt-proxy.
2. Changed hostname `/etc/hostname` to `myhost.newdomain.new`, then changed it to `myhost` to align with
	 documentation.
3. Then everywhere in my network configuration I changed `myhost.olddomain.old` to `myhost.newdomain.new`.

Then the error hit, `sudo:unable to resolve myhost`...

#### Resolution attempts

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
127.0.1.1    myhost.newdomain.new myhost

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

The file was altered, but the error persisted. Again the man page was consulted to ensure proper syntax, and it
stated that syntax should employ the ip, followed by the canonical name, and then finally an optional alias.
Which would look like this: `127.0.0.1 localhost ($ALIAS)` for localhost. Personally, I would and have
resisted the temptation to add an alias to the locahost declaration, and from all I have consulted, I would
reccommend you follow suit.

Returning to the problem at hand, the `/etc/hosts` file checked out good, and eventually discarded as a
possible option for causing the error. This left us with three other possible causes for the error. They are:

1. The `/etc/hostname` file.
2. The `resolv.conf` file.
3. The settings for dhclient.

If I were honest, a completely different avenue was explored that lead me to the three possible solutions
above, and it was employment of the systemd-resolved service. Systemd-resolved, incorporates a multicasting
hostname resolving dns server for the local network, so it does play a role in hostname resolution. It is this
odd attempt to resolve the issue that has made concluding this blog post difficult, because there is still
uncertainty concerning which of the three possible solutions was the one that needed correction. But, it was
this detour down the rabbit hole of setting up systemd-resolved, it was discovered three seperate services were
attempting to make changes to the system's `resolv.conf` file, they were anonsurf, dhclient, and systemd-resolved.

The modification that made the greatest experienced difference was adding `nohook resolv.conf` to
`/etc/dhcp/dhclient.conf`. This addition disabled dhclient from making changes to resolve.conf, and appears
for now to have resolved the problem. Afterwards though, it was learned systemd-resolved was unable to read
it's own configuration file, recieving a `permission denied`, so it was quickly removed from the system. Doing
this meant the only service that was tampering with `resolv.conf` was anonsurf. Which may have lead to the
resolution.

#### Resolv.conf

Regardless of the ambiguity of the solution. It is important to note what a proper `resolv.conf` file consists
of.

```conf
search your-domain-name.com # this being the domainname of your network
nameserver 127.0.0.1 # using 127.0.0.1 if you are running a resolver on localhost
```

#### hostname

An additional clarification that needs to be made is what a correct `/etc/hostname` should look like.
Historically, this file should only contain the hostname, and although modern services possess the ability to
parse this file even if it contains a FQDN. We are of the belief, it still should only contain a hostname.

```conf
yourhost
```

#### Conclusion

The lesson learned here is... Well, I am not sure, but there is one somewhere. This post is more of a do as I
say, not as I do posts.
