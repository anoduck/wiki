```
#  _____                          _           _
# |__  /___  _ __   ___ _ __ ___ (_)_ __   __| | ___ _ __
#   / // _ \| '_ \ / _ \ '_ ` _ \| | '_ \ / _` |/ _ \ '__|
#  / /| (_) | | | |  __/ | | | | | | | | | (_| |  __/ |
# /____\___/|_| |_|\___|_| |_| |_|_|_| |_|\__,_|\___|_|
#
```

## Zoneminder

Zoneminder is a well developed mature Open Source latest video survelliance system, that
connects to ip cameras and forwards the streaming video from those cameras to a central conctrol center.
Where video can be managed, analyzed, compressed, and saved to storage. Zoneminder has been in production for
at least as long as ip cameras have been available on the market, and has grown the with the rise in
popularity and affordability of these monitoring systems.

Once solely distributed in a customized operating system, zoneminder now facilitates more of traditional
software role in the operating system. This allows users more freedom in configuration and portability of the
video monitoring solution.

### Compatible IP Cameras

Sometimes open source software does not interface with every known hardware device, zoneminder is one of those
situations. So BEFORE we go willy-nilly and begin purchasing ip cameras left and right, we need to plan what
to buy to ensure it is compatible.

When it comes to zoneminder, the important anagram to keep in mind is "ONVIF". Which I am sure stands for
something super fantastic. What this means is that the camera adheres to certain open source industry standards in
regards to communications, commands and features. It is this standardization that allows zoneminder to be
compatible with the device regardless of the manufacturer. The downside, if there is one, is ONVIF is a
"standard" and not a "specification". It is this little game with labeling that allows device manufacturers to
charge more for a device that meets ONVIF standards due to standardization implying certain quality requirements
were met during manufacturing. Saying this, many manufacturers have already circumvented the entire idea of
ONVIF being a standard, and will use terms like "ONVIF compatible".

Another super fricking fantastic anagram is "RTSP", which stands for something as well. RTSP is a
communication protocol used to communicate with the device and zoneminder. It is a different from ONVIF, in
that it is a communication protocol and not a industry standard of development. The important bit to remember regarding
RTSP is not all RTSP compatible devices are compatible with zoneminder as well.

If the device you plan on purchasing is not explicitly and clearly labeled as supporting either of the two standards
above, then chances are it is not compatible with zoneminder.

Just as an honorable mention, at the time of writing this wiki page, both SV3C and WYZE appear to make reasonably priced
products, and a few of these products might be compatible with zoneminder. In surveying the marketplace and
prices for devices, these two have stuck out as being good options for the broke and downtrodden individual.

### A trifecta of complications: Power, connectivity and storage decisions

This section has purely come to fruition the hard and painful way. Regardless of what type of device it is, it
will require three things to function; power, connectivity and storage.

#### Power

Power to these devices can come in three different forms; solar, power cord, and POE (power of ethernet). If
you desire to have a truly "wire free" setup for your device, then you will more than likely want to use a
solar powered device. If your device is not purchased with solar a power component, they often can be purchased as
an accessory for your device.

If you want to use a power cord to provide a plug-in wired power source, you will need to find a way to get power to
your camera. Either a nearby power socket, an extension cord, or an extended power supply cable will be required.
This will require some planning out beforehand. Just keep in mind, that voltage drop does exist, and is a bitch.

Lastly, for those anal retentive bastards, who want everything in a tidy organized package, there is POE. The
benefit of POE is that both power and connectivity are delivered over the same cable. The drawback is that
stating the device is POE compatible is not puritanistic dogma, but rather a sprititualistic system of belief. In other
words, it is rather a state of mind than cold hard reality. A device may claim to be POE, but in reality will
require an additional inconvenient component to split power supply input from ethernet data connectivity, this
device is rather unoriginally referred to as a "splitter". IMHOP, this somewhat defeats the purpose of using
POE to begine with.

#### Connectivity

Now, this section is in no way or shape comprehensive, and is completely written from exposure gained from
dabbling in what little one has dabbled in. How one connects to a camera device can come in many different
shapes and forms, but of these forms there are four popular options; wifi, ethernet, POE, and old-school
analog. Also for ancient devices, at one time, coaxil was an option.

With a growing popularity, wifi is by far the most common form of connectivity available for camera
survelliance cameras. Obviously, it requires no additional wiring, provides numerous flexible means for
device configuration and data transfer. The no wires required feature is very appealing to many consumers, and
allows such devices to go completely wirefree if paired with a solar power supply. The drawback to such
devices is obviously anyone with an antenna and sufficient technical knowledge can access these devices too,
and several devices on the market do not even provide the most basic means to prevent unwanted connections.

Oddly, ethernet and POE are not nearly as popular as the other listed connectivity options. Probably due to
the requirement of additional wiring and devices that can be confusing to those unfamiliar with them. As
mentioned above, POE is quite appealing as it provides connectivity and power to be travel along the same
wire, but this functionality can be quite expensive as the wire itself is not cheap. Something learned in our
experience by painful means is that NVRs (Network Video Recorders) for POE systems provide the POE injection
builtin. Which means an additional POE injector or switch is not needed.

Lastly, analog devices are surprisingly popular and probably rank second most popular connectivity option on
the list. They have been around forever, so simple a retarded monkey could setup, and the analog wire has a
very low voltage drop over long distances. Unless being powered via solar, these devices will need two
hookups, one for the analog wire and a second for the power supply.

#### Storage

How and where video is stored on your system needs research before purchasing anything as well. There are many
pitfalls where storage of video data is concerned, so it is super critical for one to do their research and
discover exactly what options are out there. Some survelliance systems require a monthly subscription for cloud
storage, which we are not favorable toward in the least, and is something every consumer should lookout for. The
pricing of this cloud subscription varies. Many systems allow for a micro sd card to be inserted in the device for
storage, and or for use when the default storage device is unaccessible, which is a nice feature.

If you plan on running zoneminder, and setup everything carefully before hand, then zoneminder is your video
storage device.

WARNING: Many systems are designed to where you have to use their NVR for your system. NVRs are not terribly
expensive, and might seriously be a solution one looks into. An NVR can be purchased for a little more than a
single device and provide several terabytes of storage space, and can be setup and running in a matter of
minutes. The important thing to keep in mind is the compatilibility of such systems. As it is very frustrating
to purchase a camera(s) that isn't compatible with your NVR solution, and vice versa.

### Installation Options

Zoneminder can be installed in one of numerous ways.

* A bare-bones installation on a dedicated box.
* As a dedicated Virtual Machine.
* As a containerized virtual service, i.e. Docker Image.
* As a cloud based service.
* On [single board computer](https://wiki.zoneminder.com/Single_Board_Computers), such as raspberry pi.
* On a single board microcontroller, such as [arduino](https://wiki.zoneminder.com/Arduino).

#### Dockerized Zoneminder

For the moment, let's plan to install our zoneminder system using docker. This will allow us to also use the
server running docker for other services. For this you will need:

- A computer running docker.
- A configured dockerized mysql instance.

From the instructions on the docker page it shows that to use the docker image of zone minder, the
command to run is as follows:

```bash
docker run -d -t -p 1080:443 \
    -e TZ='America/Los_Angeles' \
    -e ZM_DB_USER='zmuser' \
    -e ZM_DB_PASS='zmpassword' \
    -e ZM_DB_NAME='zoneminder_database' \
    -e ZM_DB_HOST='my_central_db_server' \
    -v /disk/zoneminder/events:/var/cache/zoneminder/events \
    -v /disk/zoneminder/logs:/var/log/zm \
    --shm-size="512m" \
    --name zoneminder \
    zoneminderhq/zoneminder:latest-ubuntu18.04
```

Personally I would grant the image more ram memory, which would mean `--shm-size=1024m`, but this is just me.
Also it is important to recognize this image requires the access of the server to use https.

### Documentation

More information concerning zoneminder can be found in the following links.

- [The zoneminder manual](https://zoneminder.readthedocs.io/en/latest/)
- [Zoneminder third party utilities](https://wiki.zoneminder.com/Utilities)
