```text
#   ____ ___  ____      _    _
#  / ___/ _ \|  _ \    / \  | |
# | |  | | | | |_) |  / _ \ | |
# | |__| |_| |  _ <  / ___ \| |___
#  \____\___/|_| \_\/_/   \_\_____|
#
```

## Getting freaky with Google [Coral](https://www.coral.ai)

### Intro

Last year Google released the Coral platform, an initiative to aid in development of ai without the need of a cloud. That's
right, coral is offline, and doesn't need a cloud. Which means it is secure, doesn't involve the additional
cost of needed connectivity or access to cloud storage. The platform facilitates an on-board Edge TPU
processor that is capable of performing 4 trillion operations per second, while only consuming 1watt of power.
It is trult state of the art technology, and surprisingly affordable.

### Devices

The platform is available in numerous different devices that can be ran as a standalone server, a mini pci-express card to extend
an already existent system, and to a usb accelerator drive. Two of these devices were particularly eye catching, the [standalone
development board](https://pi3g.com/products/machine-learning/google-coral/coral-dev-board-4gb/) and the [usb accelerator](https://www.coral.ai/products/accelerator/)
. Both being priced quite reasonably.

### Development framework

Coral facilitates the tensorflow lite framework, which many of us are already familiar with using for ML
development. There is an API for both C++ and for python available.

-----
