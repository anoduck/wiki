```text
#  ____                              _
# / ___| _   _ _ __   ___ _ ____   _(_)___  ___  _ __
# \___ \| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \| '__|
#  ___) | |_| | |_) |  __/ |   \ V /| \__ \ (_) | |
# |____/ \__,_| .__/ \___|_|    \_/ |_|___/\___/|_|
#             |_|
#
```

## Supervisor

Supervisor is primarily a service that runs as a daemon, and manages other services who either do not natively
interface with the system service manager or are run on the user level and are not intended to be run as system
wide services. Setup is more involved than pm2, and is completely configuration file based. Supervisor is
dependent on it's daemon process `supervisord` being started by the system service manager. Thus needs to be
enabled and started.

### Configuration File Basics

The biggest catch to using supervisor is configuring the service in a supervisor configuration file. These
files are typically located at `/etc/supervisord.d/` and supervisor's main configuration file is located
`/etc/supervisord.conf`.

There are too many options to review for this page entry, so it is best to review the documentation provided
at [supervisord's github page](https://github.com/Supervisor/supervisor). Here is a very basic configuration
file example.

```conf
[example_service]
command=/path/to/cmd
user=someuser
autostart=true
directory=/some/dir ;This for a working dir
```
