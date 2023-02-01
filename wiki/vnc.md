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


### Setting up tigervnc-scraping

1. Create a password using `vncpassword` as the user you intend to login as.
2. Make sure the intended user is listed in the file `/etc/tigervnc/vncserver.users`.
3. create a config file for vnc by editing/creating `~/.vnc/config` with the following syntax.

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

### Using xinetd to setup tigerXvnc

To be continued later.
