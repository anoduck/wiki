```text
#  ____            _
# / ___| _   _ ___| |_ ___ _ __ ___
# \___ \| | | / __| __/ _ \ '_ ` _ \
#  ___) | |_| \__ \ ||  __/ | | | | |
# |____/ \__, |___/\__\___|_| |_| |_|
#        |___/
#  ___        __                            _   _
# |_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __
#  | || '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \
#  | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |
# |___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
#
```

Acquiring System Information
----------------------------

It is not always a convenience to shutdown a system, walk over to the server closet, pull the server from the
rack, disconnect all the cables, and open up the casing to discover the specifications of a particular part.
Often, you just want to type in a command and move on with your life. 

So this wiki page covers how to discover hardware information from your terminal. 

### dmidecode

There are several commands that can give you specifics of system information, but dmidecode can do most of it,
and provides more detailed information. So, it is the best command to do this with. 

The `-t` flag is used to denote what topic the users is requesting information on. If the `-t` flag is used
without any further arguments, then dmidecode will display a list of all available topics the user can then
use to discover what he is looking for. 

- `dmidecode -t memory`: Shows ram info
- `dmidecode -t bios`: Shows bios info
- `dmidecode -t system`: Provides a system overview.

```sh
dmidecode | grep -A3 '^System Information'
```

### Other Options

In the customary manner, we will provide some other options, in table form. 

| command | context | Description                                                   |
| ------- | ------- | -----------                                                   |
| lscpu   | cpu     | Provides fairly indepth information on a systems CPUs         |
| lspci   | pci     | Provides information on devices connected to the PCI buses    |
| lsusb   | usb     | Provides information on usb devices connected to the system   |
| mount   | drives  | Without any flags, mount will display what drives are mounted |
| df      | disks   | Displays amount of free space on drives                       |
| lsblk   | blocks  | Shows an overview of available block devices                  |
| free | ram | shows amount of free ram available |
| fdisk | disks | When used with only the `-l` flag will list available drives |
