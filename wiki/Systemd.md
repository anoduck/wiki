```text
#  ____            _                 ____
# / ___| _   _ ___| |_ ___ _ __ ___ |  _ \
# \___ \| | | / __| __/ _ \ '_ ` _ \| | | |
#  ___) | |_| \__ \ ||  __/ | | | | | |_| |
# |____/ \__, |___/\__\___|_| |_| |_|____/
#        |___/
#
```

# SystemD: The most common service manager for Linux Systems

SystemD is the service manager for linux systems that replaces the more traditional SysV init style systems
used in the past. Although most commonly implemented, systemd is not universally adopted, and several Linux
distrobutions still avoid foregoing it's implementation. One of the things that separates systemd from it's
predecessor is it's implementation of built-in services, which traditionally were provided by external third
party programs.

## Writing SystemD Unit Files

Systemd breaks services down into what it refers to as units. Each service and the dependencies of that
service making up a single unit. The accomodates for service dependency resolution, and streamlines the
service management process.

It is particularly important to know how to write your own service unit files for systemd in linux system management,
because of the fast paced development environment surrounding Linux software. So below we will break down the
various parts.

### Overview

A minimal service configuration will appear like so:

```systemd
[Unit]
Description=A Service Description

[Service]
ExecStart=/usr/sbin/foobar

[Install]
WantedBy=Multi-user.target
```

Notice the three different sections of the systemd service file: Unit, Service, and Install. Each of these
will be discussed further below.

For a full list of available attributes please refer to the man pages `man systemd.unit` and `man systemd.service`,
information on `systemd.install` is contained within the `man systemd.unit` man page.

#### Dependency Management

Systemd defines dependencies on two seperate priority association levels, "Require" and "Want". "Require" is
used to denote dependencies with the highest degree of association. Meaning, that if one of the required
dependency fails, then so does the service unit that required it. "Want" is used to denote a lesser degree of
association, where if the dependency fails it will have not impact on the unit wanting it.

### Unit

As the name indicates, the unit section provides attributes that defines the service unit. Below we list a few
of the most common attributes in customary table format.

| Attribute     | Description                                        |
| :------------ | :------------------------------------------------- |
| Description   | A Description of the unit                          |
| Documentation | A location identifier to documentation on the unit |
| Before        | Start before listed dependency                     |
| After         | Start after listed dependency                      |
| Requires      | High Degree Association Dependencies               |
| Wants         | Lower Degree Association Dependencies              |
| Conflicts     | Handles conflicting services to stop if started    |

### Service

The service section provides attributes that define and control the particular service the unit is
controlling.

| Attribute       | Description                                                     |
| :-------------- | :-------------------------------------------------------------- |
| Type            | One of: simple, forking, oneshot, dbus, notify, idle; see below |
| ExecStart       | Command with arguements to start the service.                   |
| ExecStop        | Commands to stop the service                                    |
| ExecReload      | Commands to trigger a configuration reload.                     |
| Restart         | Restarts the service in the advent of failure.                  |
| RemainAfterExit | Boolean. Service remains active even if exited.                 |

#### Service Types

Below are a list of definitions which describe the available service types which can be used in the `Type`
definition of the service file.

* simple - Starts the service immediately
* forking - Service start succeeds upon process forking.
* oneshot - Requires the process to exit for success.
* dbus - Succeeds when dbus name is acquired.
* notify - Succeeds on reception of signal.
* idle - Execution succeeds only after system is idle.

### Install

The install section provides attributes the deal with the enabling and disabling of the service.

| Attribute  | Description                                           |
| :--------- | :---------------------------------------------------- |
| Alias      | Space separated list of additional names              |
| RequiredBy | Heavy associated Reverse Dependencies                 |
| WantedBy   | Lower Associated Reverse Dependencies                 |
| Also       | List of units to enable/disable along with this unit. |


## References

* [SystemD Service File Examples](https://www.shellhacks.com/systemd-service-file-example/)
