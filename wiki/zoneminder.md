```
#  _____                          _           _
# |__  /___  _ __   ___ _ __ ___ (_)_ __   __| | ___ _ __
#   / // _ \| '_ \ / _ \ '_ ` _ \| | '_ \ / _` |/ _ \ '__|
#  / /| (_) | | | |  __/ | | | | | | | | | (_| |  __/ |
# /____\___/|_| |_|\___|_| |_| |_|_|_| |_|\__,_|\___|_|
#
```

## Zoneminder

Zoneminder is a well developed, and mature Open Source state-of-the-art video survelliance system, that
connects to ip cameras and forwards the streaming video from those cameras to a central conctrol center.
Where video can be managed, analyzed, compressed, and saved to storage. Zoneminder has been in production for
at least as long as ip cameras have been available on the market, and has grown the with the rise in
popularity and affordability of these monitoring systems.

Once solely distributed in a customized operating system, zoneminder now facilitates more of traditional
software role in the operating system. This allows users more freedom in configuration and portability of the
video monitoring solution.

### Implementation

The primary purpose of creating this wiki page is to prepare for our own implementation of the software. As
such this is what this entry will mostly cover.

#### Compatible IP Cameras

Sometimes open source software does not interface with every known hardware device, zoneminder is one of those
situations. So BEFORE we go willy-nilly and begin purchasing ip cameras left and right, we need to plan what
to buy to ensure it is compatible.

For beginners (that is unquestionably us), there are two brands zoneminder reccommends.

- [Axis](https://wiki.zoneminder.com/Axis) = Good, but fucking expensive.
- [Hikvision](https://wiki.zoneminder.com/Hikvision) = Cheap and decent.(No longer true.)

I am going to include two other brands in this mix, because they were listed as what was available in our
miniscule price range.

- [Anpiz](https://wiki.zoneminder.com/Anpviz) = Only one model is supported, the [IPC-D250G-S](https://www.amazon.com/Anpviz-Weatherproof-Compliant-Compatible-IPC-D250G/dp/B07N3Y4HS6).
- [EZVIZ](https://wiki.zoneminder.com/EZVIZ) = A rebranding of Hikvision, one model supported, the [c3w](https://www.amazon.com/EZVIZ-Waterproof-Customizable-Alerts%EF%BC%8CAI-Compression/dp/B09M3R3CMX/?th=1)

The wiki states that of these two brands, Hikvision is the cheapest, and since we are frankly broke, this is
what we will plan on.

##### Hikvision Models

With some research translating old models into current models, we were able to find a few cameras that appear
to be compatible with zoneminder and were still in reach of our price range. Not the price range we wanted,
but doable if we reduce the number of cameras purchased.

- [DS-2cd2143G0-I](https://www.amazon.com/dp/B07B16DFMB/?th=1) = $103
- [DS-2cd2632F-I](https://www.amazon.com/HIKVISION-DS-2CD2632F-I-Varifocal-Camera-White/dp/B00GFFPFEU) = $123
- [DS-2cd2043GO-I](https://www.amazon.com/HIKVISION-US-VERSION-DS-2CD2043G0-I-Communication/dp/B07VC8VR8K/) =
	$115

#### Installation Options

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
