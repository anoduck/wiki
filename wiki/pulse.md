```text
#  ____        _               _             _ _
# |  _ \ _   _| |___  ___     / \  _   _  __| (_) ___
# | |_) | | | | / __|/ _ \   / _ \| | | |/ _` | |/ _ \
# |  __/| |_| | \__ \  __/  / ___ \ |_| | (_| | | (_) |
# |_|    \__,_|_|___/\___| /_/   \_\__,_|\__,_|_|\___/
#
```

# Pulse Audio Server

PulseAudio is a general purpose sound server intended to run as a middleware between your applications and
your hardware devices, either using Alsa or Oss (but probably alsa). Designed to easy audio
configuration on computer systems, but due to the highly customizable nature of the server, allows advanced
users to create a configuration that best suits their needs. 

It is easy to confuse Alsa and PulseAudio, and the two appear intertangled in our minds as well. It is
best to come to an understanding that pulse does what pulse does, and alsa does what alsa does. (Whatever than means..)

## SunSetting Pulse

Pipewire Audio Server was specifically written to replace both PulseAudio and Jack (another audio server). It
is stable, and quickly has become the new default. As a result, this unfinished disgrace for a wiki page will
be merged at some point in the future, or deleted altogether. So, it is advised you visit the
[Pipewire](pipewire) page instead.


(It should be interesting what this horizontal line becomes below.)

# --------------------------------------------------------------------------------------------------------

## Configuring Pulse as a network sound server.

This wiki page covers using PulseAudio as a network sound server to allow a remote and headless system
to stream audio to a user's computer. 

[PulseAudio Network Setup](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/)

### Remote configuration

First we begin by configuring the server on the remote host.

#### Configuration files

__If you plan to run pulseaudio as a regular user,__ It is advised to not make changes to the system's 
configuration files at first, but to copy the configuration files from `/etc/pulse/*` to the user's configuration 
directory `~/.config/pulse`, and make needed changes there first.

```bash
sudo cp -r /etc/pulse/* ~/.config/pulse/
```

__For our purposes of running pulseaudio as a system service, we will ignore this advice.__ 

All values of the configuration file are at their default settings and commented out.

##### daemon.conf

File to edit: `/etc/pulse/daemon.conf`

__The required values for configuarion are below.__

```conf
daemonize = yes
resample-method = speex-float-2
```

##### Load the appropriate modules

If you plan on running pulse audio as a normal user, you edit: `~/.config/pulse/default.pa`

If you plan on running pulse audio as a system service, you edit: `/etc/pulse/system.pa`

Which ever file you edit, add the following line to the bottom of the configuration.

```conf
load-module module-native-protocol-tcp auth-anonymous=1
```

If you plan on using avahi, then you will need to add:

```conf
# On the Server: 
load-module module-zeroconf-publish

# On the Client:
load-module module-zeroconf-discover
```

##### Establishing the Server in vnc

To startup vnc, we use a simple script that establishes an ssh tunnel with the remote client, and then opens
the vnc viewer. To establish the server to connect to, we will simply add it as an environmental variable to
this file.

```bash
export PULSE_SERVER=$YOUR_SERVER_IP_OR_NAME
```

