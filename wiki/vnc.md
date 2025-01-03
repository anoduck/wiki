```text
# __     ___   _  ____
# \ \   / / \ | |/ ___|
#  \ \ / /|  \| | |
#   \ V / | |\  | |___
#    \_/  |_| \_|\____|
#
```

*ALA, Kali Linux*

## Setting up an VNC Server overview

At one time or another almost every system admin has had to setup a VNC server. Here is a brief and haphazard
means to accomplish this. For this example we will setup a vncserver that initiated by systemd on a debian
derivitive using tigervnc.

For information on how to setup the X-dummy driver for truly headless desktops, please see
[vnc-xdummy](vnc-xdummy).

### Setting up tigervnc-scraping

1. Create a password using `vncpassword` as the user you intend to login as.
2. Make sure the intended user is listed in the file `/etc/tigervnc/vncserver.users`.
3. create a config file for vnc by editing/creating `~/.vnc/config` with the following syntax.

*This was the eventually resolution chosen for setup. As it worked effortlessly, and allowed for good screen
resolution and performance.*

```conf
session=i3
geometry=1920x1080
localhost
alwaysshared
```

4. Configure X to load libvnc, by adding the following to `/etc/X11/xorg.conf.d/10-vnc.conf`:

```conf
Section "Module"
Load "vnc"
EndSection

Section "Screen"
Identifier "Screen0"
Option "UserPasswdVerifier" "VncAuth"
Option "PasswordFile" "/root/.vnc/passwd"
EndSection
```

### Setting up lightdm to accept and act as a vnc server.

1. Install the tigervnc-standalone package
2. Install lightdm and the lightdm-autologin-greeter package.
3. Open the lightdm configuration file at `/etc/lightdm/lightdm.conf`
4. At the bottom of the configuration file you will find the settings for lightdm to run as a vnc server.
5. Simply uncomment each applicable setting, close the file, and restart the server.

#### Handling the `Failed to create IPV6 VNC socket` error

The full error output is: `WARNING: Failed to create IPv6 VNC socket: Error binding to address 127.0.0.1:5900: Invalid argument`

Right now, fuck if I know. For some reason lightdm is insisting on launching Xvnc on ipv6, which should not be
a problem, but appears to be.
