```text
#  _____     _ _          _   _
# |  ___|_ _(_) | ___  __| | | |_ ___     ___  _ __   ___ _ __
# | |_ / _` | | |/ _ \/ _` | | __/ _ \   / _ \| '_ \ / _ \ '_ \
# |  _| (_| | | |  __/ (_| | | || (_) | | (_) | |_) |  __/ | | |
# |_|  \__,_|_|_|\___|\__,_|  \__\___/   \___/| .__/ \___|_| |_|
#                                             |_|
#     __  _             __  _      _    __                  _
#    / /_| | _____   __/ /_| |_ __(_)  / / __ ___ _ __   __| | ___ _ __
#   / / _` |/ _ \ \ / / / _` | '__| | / / '__/ _ \ '_ \ / _` |/ _ \ '__|
#  / / (_| |  __/\ V / / (_| | |  | |/ /| | |  __/ | | | (_| |  __/ |
# /_/ \__,_|\___| \_/_/ \__,_|_|  |_/_/ |_|  \___|_| |_|\__,_|\___|_|
#
```

Failed to open /dev/dr/renderD128
----------------------------------

This error is only known to occur on linux systems, thus placing it in the linux section of the wiki, and only
occurs when performing computational work that needs to use the graphics driver. So, saying it is not commonly
encountered is sufficient.

### The Error

This error was encountered while using the python library OpenCV2 to perform some image processing and the
error message was as following:

```bash
failed to open /dev/dri/renderD128: Permission denied
failed to open /dev/dri/renderD128: Permission denied
failed to open /dev/dri/renderD128: Permission denied
failed to open /dev/dri/renderD128: Permission denied
failed to open /dev/dri/renderD128: Permission denied
failed to open /dev/dri/renderD128: Permission denied
```

#### The solution

While one could simple change the permissions of the file descriptor to `sudo chmod 666 /dev/dr/renderD128`,
it is likely such change would simply be overwritten during the next reboot, and is completely unnecessary.
The proper solution is to simply add the user to the group "render" with `sudo adduser $USER render`. Once
this is done, the answer should no longer occur.

For prosperity and redundancy, I will write the solution again.

```bash
sudo adduser $USER render
```
