```text
#  ____             _        __   __                 ____  _     _ _   _
# |  _ \ ___  _   _| |_ ___  \ \ / /__  _   _ _ __  / ___|| |__ (_) |_| |
# | |_) / _ \| | | | __/ _ \  \ V / _ \| | | | '__| \___ \| '_ \| | __| |
# |  _ < (_) | |_| | ||  __/   | | (_) | |_| | |     ___) | | | | | |_|_|
# |_| \_\___/ \__,_|\__\___|   |_|\___/ \__,_|_|    |____/|_| |_|_|\__(_)
#
```

Route your shit!
================

A less than practical, most inadequate, barely unuseable, guide to network routes on OpenBSD.
----------------------------------------------------------------------------------------------

- Show your current routes.

```bash
sudo route show
```

- Delete that bitch:

```bash
sudo route delete -inet $NETWORK_IP4_ADDRESS -netmask $NETWORK_MASK
# example
sudo route delete -inet 192.168.0.0 -netmask 255.255.255.0
```

- Add default gateway

```bash
sudo route add default $DEFAULT_GATEWAY
```

- Add route to a network

```bash
sudo route add -net -ifp $INTERFACE -inet $NETWORK_IP4_ADDRESS -netmask $NETWORK_MASK
```

- https://www.cyberciti.biz/faq/openbsd-ip-routing-configuration/
- https://www.cyberciti.biz/faq/howto-setup-static-routes-on-openbsd-unix-networking/
