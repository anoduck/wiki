```text
#   ____ ____  ____  ____
#  / ___|  _ \/ ___||  _ \
# | |  _| |_) \___ \| | | |
# | |_| |  __/ ___) | |_| |
#  \____|_|   |____/|____/
#
```

## GPSD: The gps daemon

GPSd is the gps monitoring daemon for linux, unix, and most open source operating systems. It is a daemon that
runs in the background and communicates between the gps device, drivers and gps clients. The installation of
which is fairly straight forward for most operating systems, merely requiring the added definition of the
location to the connected gps device for running. 

### Troubleshooting gpsd

Below are a few commands used to troubleshoot gpsd. 

1. Stop all gpsd processes. `sudo killall gpsd`
2. Ensure all created sockets are removed. `sudo rm /run/gpsd.sock`
3. Run gpsmon to test if device is working. `sudo gpsmon /dev/ttyUSB0`
4. If using a Garmin Device, test it is identified. `sudo GPSDEV=/dev/ttyUSB0 gpstrans -i`
5. Run GPSd in debug mode for output. `sudo gpsd -N -D3 -F /run/gpsd.sock /dev/ttyUSB0`

Read further for the resolution to a potential issue.

### Cannot create listening socket

On the most recent update of gpsd, the daemon refused to run altogether. The output error was `Failed to
create listening socket ([::1]:2947)`. As one can easily discern, this is an ipv6 address. The real question
was why is a failure to establish a socket on an ipv6 port causing GPSd to fail on a machine where all ipv6 is
disabled at the kernel level?

The simple answer was some maintainer decided to require gpsd to only run on ipv6 network ports. Which
since all of ipv6 was disabled at the kernel level, this was not going to happen. So we needed to change this
in the systemd `gpsd.socket` configuration file. 

To edit the file we executed `sudo systemctl edit --full gpsd.socket`, which opened an editor in the
configuration file for `gpsd.socket`. Below are it's contents, where you can clearly see the issue.

```conf
[Unit]
Description=GPS (Global Positioning System) Daemon Sockets

[Socket]
ListenStream=/run/gpsd.sock
ListenStream=[::1]:2947 ## <--- Comment out this.
ListenStream=127.0.0.1:2947 <--- Leave this alone.
# To allow gpsd remote access, start gpsd with the -G option and
# uncomment the next two lines:
# ListenStream=[::]:2947
# ListenStream=0.0.0.0:2947
SocketMode=0600
BindIPv6Only=yes ## <--- Change this to "no"

[Install]
WantedBy=sockets.target
```

After making the needed changes as indicated in the comments, all that was needed was to restart gpsd. Which
worked, as it should.

### Building GPSD from src

Something every system administrator should be able to do is build applications from source code. For an
encountered issue launching GPSD, we are having to build GPSD from source for testing. All the
required dependencies are in the repository `build.adoc` file. For our particular build, the dependecy
missing from our system is asciidoctor.
The main repository for GPSD is at: `https://gitlab.com/gpsd/gpsd.git`. 
If you are a user of github, you should be able to login to gitlab with your github credentials.

#### Building

After reviewing the build documentation and installing all the required dependencies, you are ready to build.
If you have not already cloned the repository, do so now with `git clone ...`.

1. This project uses `scons` rather than the popular `make` command. So ensure you have that installed.
2. Run `scons -c && scons && scons check && sudo scons install`

