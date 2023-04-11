```text
#     _    __  __ ____   ____ ____  _   _   _  __     _ _
#    / \  |  \/  |  _ \ / ___|  _ \| | | | | |/ /__ _| (_)
#   / _ \ | |\/| | | | | |  _| |_) | | | | | ' // _` | | |
#  / ___ \| |  | | |_| | |_| |  __/| |_| | | . \ (_| | | |
# /_/   \_\_|  |_|____/ \____|_|    \___/  |_|\_\__,_|_|_|
#
```

## Installing AMDGPU drivers on Kali

Less complicated than you might think.

1. Download the most recent driver release, regardless of distro, from amd. [here](https://www.amd.com/en/support/linux-drivers)
2. It will be a `.deb` file. Then install it. `sudo dpkg -i --force-overwrite ./amdgpu-install_X.X.XXXXX-X_all.deb`.
3. Then run `apt update`, and continue if it all checks out.
4. Edit the bash script, for us, we are using micro. `sudo micro /usr/bin/amdgpu-install`
5. Once open in your editor, add kali to the list of debian based distros.
6. Then run the installer.
