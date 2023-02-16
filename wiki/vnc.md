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

### Using xinetd to setup tigerXvnc

Probably not the reccommended way to setup a vnc server, but with this method, one is allowed to run vnc on a
truly headless host.

*This method was abandoned as it only opened a empty gray screen.*

#### Xinetd Service

We will use Xinetd to manage starting the xnvcserver, and so we will need to configure that service for
xinetd.

```config
service xvncserver {
	disable = no
	protocol = tcp
	socket_type = stream
	wait = no
	user = root
	server = /usr/bin/Xtigervnc
	server_args = -inetd -query localhost -once -geometry 1024x768 -depth 24 -fp /usr/share/X11/fonts/misc -securitytypes=none
	}
```

#### Defining the service in `/etc/services`

In order for xinetd to know which service it is to start, you will need to add it to the `/etc/services` file.
Add it to the bottom of the file, where it notates `custom services`, or some reasonable facsimile thereof.

```config
xvncserver 	5950/tcp 	#for xvncserver
```

#### Configure xdm

Both gdm and lightdm can be used for this as well, but gdm tends to be rather heavy and lightdm appears to
require a head. So for this xdm was chosen.

* In the file `/etc/X11/xdm/Xaccess` uncomment the line `*             #any host can get a login window`, this
	will enable remote access
* In the file `/etc/X11/xdm/xdm-config` comment the line `!DisplayManager.requestPort:    0` with a `!`.
