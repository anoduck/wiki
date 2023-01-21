```text
#                        __ _ _
# __  ___ __  _ __ ___  / _(_) | ___
# \ \/ / '_ \| '__/ _ \| |_| | |/ _ \
#  >  <| |_) | | | (_) |  _| | |  __/
# /_/\_\ .__/|_|  \___/|_| |_|_|\___|
#      |_|
#
```

### It is like a `~/.profile`, but for `xorg`

Learned of a new configuration file today. It is just being implemented in _some_ linuxes. To be honest,
there is nothing revolutionary, mandatory, or required about its implementation. To be honest, it is just
a safeguard to prevent those who tinker with their `xsession` and `xinit` files from buggering up their
X11 setup. Without a doubt, it is a good implementation to follow for better system management.

#### How to play along.

*Fer Linux* Place the following snippet in both `~/.xsession` AND `/etc/X11/Xsession`.
*Fer OpenBSD* Place the following snippet in `~/.xsession` AND `/etc/X11/xenodm/Xsession`.

```shell
#!/bin/sh

# Make sure this is before the 'exec' command or it won't be sourced.
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

```

Then afterwords, add programs that you would like to start BEFORE your window manager begins.
