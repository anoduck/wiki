```text
#  ____  _                     _
# |  _ \(_)_ __   _____      _(_)_ __ ___
# | |_) | | '_ \ / _ \ \ /\ / / | '__/ _ \
# |  __/| | |_) |  __/\ V  V /| | | |  __/
# |_|   |_| .__/ \___| \_/\_/ |_|_|  \___|
#         |_|
#
```

## Pipewire Audio Server

Pipewire is a new and robust audio server written with the intent to make both pulseaudio, and the 
Jack audio server. obsolete and a thing of the past, and so far it has almost accomplished this. 
There is only one catch to Pipewire, it has not developed the native ability to stream audio over
the network. So, to overcome this limitation, Pipewire implements its own version of pulseaudio.
Which you have to admit is pretty damn ironic.

### Streaming PulseAudio over RTP

Below are the command line arguements to stream a client over rtp to a server.

```bash
pacmd load-module module-null-sink sink_name=RTP
pacmd update-sink-proplist RTP device.description=RTP
pacmd load-module module-rtp-send \
  source=RTP.monitor \
  destination_ip=224.0.0.56 \
  port=46416
```

__References__

- [Archwiki pulse examples](https://wiki.archlinux.org/title/PulseAudio/Examples)
- [Archwiki pipewire page](https://wiki.archlinux.org/title/PipeWire)
