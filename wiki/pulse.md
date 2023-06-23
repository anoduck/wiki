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


## Configuring Pulse as a network sound server.

This entire wiki page is written to document the method of using PulseAudio as a network sound server to
allow a remote and headless system to stream audio to a user's computer. 

### Remote configuration

First we begin by configuring the server on the remote host.

#### Configuration files

It is recommended to not make changes to the system's configuration files at first, but to copy the
configuration files from `/etc/pulse/*` to the user's configuration directory `~/.config/pulse`, and make
needed changes there first.

```bash
sudo cp -r /etc/pulse/* ~/.config/pulse/
```

By default, all values of the configuration file have been commented out, and a preset of configuration
variables were established during compilation. So to make changes to the file either the option can be
uncommented and/or changed, or the configuration variable can simply be added to the bottom of the file. The
former is preferred as it ensure's values are loaded in the intended order, and it helps to maintain
configuration file structure. Although this is user preference.

##### daemon.conf

File to be edited: `~/.config/pulse/daemon.conf`

__The required values for configuarion are below.__

```conf
daemonize = yes
allow-module-loading = no
resample-method = speex-float-2
```

##### default.pa 

```conf
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;192.168.1.0/24
```
##### Establishing the Server in vnc

To startup vnc, we use a simple script that establishes an ssh tunnel with the remote client, and then opens
the vnc viewer. To establish the server to connect to, we will simply add it as an environmental variable to
this file.

```bash
export PULSE_SERVER=$YOUR_SERVER_IP_OR_NAME
```

