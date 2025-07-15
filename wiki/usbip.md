```text
#  _   _ ____  ____ ___ ____
# | | | / ___|| __ )_ _|  _ \
# | | | \___ \|  _ \| || |_) |
# | |_| |___) | |_) | ||  __/
#  \___/|____/|____/___|_|
```

The Wonderful World of USBIP
============================

> [!note] What is usbip?
> USBIP is a system service that allows user to share USB devices with remote systems over the network.

Intro
-----

All cliche statements aside, it was not too long ago when the ability to share USB devices across the network was
not a reality, and it was viewed as unobtainable. The technology simply was not there to do it. It was during
this time one would see things such as 30Ft USB extension cables. Eventually, the technology evolved enough to
allow proprietary USB hubs that would allow the sharing of several USB devices over the network with a special
proprietary USB driver. Fortunately, the technology has evolved and now become common place.

The feat of sharing USB devices over the network is done by the use of a special generic driver which
encapsulates "USB I/O messages" in TCP payloads and transmits them across the network to remote systems. 

Usage
-----

Creating USB/IP connections that persist after rebooting the system is out of the scope of this page. One can
find more information on that subject on the [ArchLinux USB/IP page](https://wiki.archlinux.org/title/USB/IP).
If you have questions not covered in this page, it would be best to check out there as well, or check out the
[official USB/IP project page](https://usbip.sourceforge.net/).

Using the service is incredibly easy, and involves simply running the `usbip` service command in the user's
terminal. The command uses the following arguments to manage the sharing of USB devices; `list`, `port`, `attach`,
`detach`, `bind`, and `unbind.`

### Network considerations

The services requires the TCP port 3240 is open in order to form connections, and each device is assigned it's
own port to communicate on.

### Command Arguments

| Args   | What it does                                          | Flags      |
| ------ | --------------                                        | -------    |
| list   | Lists devices available on the server.                | `-r`       |
| port   | Lists devices attached to the system.                 | N/A        |
| attach | Attaches devices to the system                        | `-r`, `-b` |
| detach | Detaches a device from the system                     | `-p`       |
| bind   | Bind the device to the server for sharing             | `-b`       |
| unbind | Unbind the device from the server and stop sharing it | `-b`       |

### Example Commands

- list locally available devices - `usbip list -l`
- list remotely available devices - `usbip list -r`
- bind device on busid `$BUSID` - `usbip bind -b $BUSID`
- unbind the same device - `usbip unbind -b $BUSID`
- list attached devices - `usbip port`
- detach a device - `usbip detach -p $PORT_NUMBER`
- attach a remote device - `usbip attach -r $SERVER_IP -b $BUSID`

For a more indepth review of how to use these commands please consult `man usbip`
