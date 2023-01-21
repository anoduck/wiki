```text
# __     ___   _  ____
# \ \   / / \ | |/ ___|
#  \ \ / /|  \| | |
#   \ V / | |\  | |___
#    \_/  |_| \_|\____|
#
```

## Setting up an VNC Server overview

At one time or another almost every system admin has had to setup a VNC server. Here is a brief and haphazard
means to accomplish this. For this example we will setup a vncserver that initiated by systemd on a debian
derivitive using tigervnc.

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
