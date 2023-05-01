```text
# __     ___   _  ____  __  __   _
# \ \   / / \ | |/ ___| \ \/ /__| |_   _ _ __ ___  _ __ ___  _   _
#  \ \ / /|  \| | |      \  // _` | | | | '_ ` _ \| '_ ` _ \| | | |
#   \ V / | |\  | |___   /  \ (_| | |_| | | | | | | | | | | | |_| |
#    \_/  |_| \_|\____| /_/\_\__,_|\__,_|_| |_| |_|_| |_| |_|\__, |
#                                                            |___/
#
```

## VNC and XDummy

### XDummy

`xserver-xorg-video-dummy` provides a dummy driver that allows headless systems to run X. It was originally
created to provide a means for developers to run tests on xserver, then later on found use in providing a
means to provide X a driver so it can run on systems that do not have a physical monitor. Note, that using the
dummy driver is only needed in special cases where a definitive geometry of the display is required.

### VNC

VNC has now circumvented the need of the "dummy" driver, by creating it's own module for X that provides a
monitor-free screen from which X can run on. This circumvension works fine, but not always. Some applications
and libraries require a measurable display and are not satisfied with vnc's screen. It is for these occasions
that one has to implement use of the dummy video driver.

### Combining the two

The biggest complication of combining the two is that XDummy remains undocumented, and relatively rarely heard
of. It is installed along side the xserver dummy driver, but is not mentioned in the packages description.
Implementing the dummy driver alongside TigerVNC's Xvnc Xorg module within a standard xorg.conf file is very doable, but
this results in a monitor that is limited in size to a mere 1024x800 resolution. Which is much too small for
modern monitors. An implementation of X11VNC appears to be better suited for the pairing with the dummy driver
because of X11vnc's approach to forwarding the monitor. But, how exactly to work out the best pairing of
X11vnc with XDummy is yet to be discovered.

#### TigerVNC Xvnc with Dummy Driver

Below is an example of combining Xvnc with Xorg's dummy driver. The end result will unfortunately be that tiny
1024x800 display as mentioned above. This small display appears to be a built in limitation in the driver
itself, in order to provide minimal strain on the system's resources during testing. As, it was originally
designed to do.

```conf
Section "Screen"
  Identifier	"Dummy_Screen"
  Device	"Dummy_Card"
  Monitor	"Dummy_Monitor"
  DefaultDepth	24
  SubSection	"Display"
    Depth	24
  EndSubSection
EndSection

Section "Device"
  Identifier	"Dummy_Card"
  Driver 	"dummy"
  OPTION	"DPMS"
EndSection

Section "Monitor"
  Identifier	"Monitor0"
  HorizSync 	30.0-83.0
  VertRefresh 	56.0-76.0
  # https://arachnoid.com/modelines/
  # 1920x1080 @ 60.00 Hz (GTF) hsync: 67.08 kHz; pclk: 172.80 MHz
  Modeline "1920x1080_60.00" 172.80 1920 2040 2248 2576 1080 1081 1084 1118 -HSync +Vsync
  Option	"DPMS"
EndSection
```

As also previously mentioned, using X11vnc promises to provide a better chance of surpassing the resolution
limitation, since it provides a `scale` configuration variable, but unlike Xvnc, X11vnc does not provide a
module for Xorg to use. So, XDummy would need to be started and configured by hand first before calling on
X11vnc to forward it to any host.


### References

- [Our Friendship is over](https://mriksman.blogspot.com/2013/07/our-friendship-is-over-xdummy-replaces.html)
- [ArchWiki X11VNC](https://wiki.archlinux.org/title/X11vnc)
- [Xpra on XDummy](https://github.com/Xpra-org/xpra/blob/master/docs/Usage/Xdummy.md)
- [XDummy Man](https://manpages.ubuntu.com/manpages/focal/man8/Xdummy.8.html)

-----
