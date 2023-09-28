```text
#  _____        __
# |_ _\ \      / /
#  | | \ \ /\ / /
#  | |  \ V  V /
# |___|  \_/\_/
#
```

## IW - Wireless network CLI

The iw command is the new CLI interface to Linux kernel wireless drivers. It was written with the intent to
eventually replace `iwconfig`, and as so should be adopted soon. There are only two documents describing it's
features, the man page, [the kernel wiki page](https://wireless.wiki.kernel.org/en/users/documentation/iw),
and [the cheatsheet for moving from iwconfig to it](https://wireless.wiki.kernel.org/en/users/documentation/iw/replace-iwconfig).
Just as the linux kernel will perpetually be in a process of development, so will the iw command. Features for
this command will be created on a as needed basis. Documentation for these features will arise much
afterwards. 

### Cheatsheet

Below is a cheatsheet providing commonly used commands for iw.

1. Set up a new monitor mode -- `iw dev $DEVICE interface add $MON_DEVICE type monitor flags $FLAGS`
2. Set regulatory domain -- `iw dev $DEVICE reg set XX`
3. Delete Interface -- `iw dev wlan0mon del`
4. Power save -- `iw dev $DEVICE set power_save on`
5. Set TX power -- `iw dev $DEVICE set txpower <auto|fixed|limit> [<tx power in mBm>]`
6. Station statistics -- `iw dev $DEVICE station dump`
7. Stats against peer -- `iw dev $DEVICE station get $PEER`
8. Link status -- `iw dev $DEVICE link`
9. Set Channel -- ???

#### Monitor flags

The following are flags you can specify:

    none
    fcsfail
    plcpfail
    control
    otherbss
    cook
    active

