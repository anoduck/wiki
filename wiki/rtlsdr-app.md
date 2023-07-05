```text
#  ____ _____ _         ____  ____  ____       _                  _     _ _
# |  _ \_   _| |       / ___||  _ \|  _ \     / \   _ __  _ __   | |   (_) |__
# | |_) || | | |   ____\___ \| | | | |_) |   / _ \ | '_ \| '_ \  | |   | | '_ \
# |  _ < | | | |__|_____|__) | |_| |  _ <   / ___ \| |_) | |_) | | |___| | |_) |
# |_| \_\|_| |_____|   |____/|____/|_| \_\ /_/   \_\ .__/| .__/  |_____|_|_.__/
#                                                  |_|   |_|
#
```

## The RTL-SDR Application 

Not only is RTL-SDR the name of a technology and a SDR Doggle, but it is the name of a library that provides
applications for use with the RTL-SDR doggle. Not really that confusing, just apparently a very popular name.

This application library is written for and intended to be used with the RTL-SDR-Blog SDR doggle, although the
library can be used with other sdr platforms as well. It provides:

- rtl-tcp: A sdr server that allows network connectivity to the sdr platform.
- rtl-fm: A basic frequency monitoring application.
- rtl-power: A wave spectrum scanner logging the power of present signals
- rtl-bias: a means to activate the rtl-sdr doggle's built in biased t.
- rtl-eeprom: An eeprom programmer (Don't touch this.)
- rtl-adsb: A simple adsb decoder.
