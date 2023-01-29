```text
#  _   _                 ____                  _
# | | | |___  ___ _ __  / ___|  ___ _ ____   _(_) ___ ___
# | | | / __|/ _ \ '__| \___ \ / _ \ '__\ \ / / |/ __/ _ \
# | |_| \__ \  __/ |     ___) |  __/ |   \ V /| | (_|  __/
#  \___/|___/\___|_|    |____/ \___|_|    \_/ |_|\___\___|
#
#  __  __
# |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___
# | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
# | |  | | (_| | | | | (_| | (_| |  __/ |  \__ \
# |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
#                           |___/
#
```

## User Level Service Managers

We are not talking about systemd, openrc, rc.d, or sysv. Those are system level service/daemon management
systems. Here we are talking about user level service managers, that is, services that are started and run by
a user of the system, or a service that does not interface well with a system service manager.

As far as user level service managers goes, there are two options one should keep in mind.

1. [supervisord](supervisord)
2. [pm2](pm2)
