```text
 _   _                        _ _
| | | |_ __  __ _ _ _ __ _ __| (_)_ _  __ _
| |_| | '_ \/ _` | '_/ _` / _` | | ' \/ _` |
 \___/| .__/\__, |_| \__,_\__,_|_|_||_\__, |
      |_|   |___/                     |___/
   _   _  _ ___
  /_\ | \| |   \
 / _ \| .` | |) |
/_/ \_\_|\_|___/
 ___                                   _ _
|   \ _____ __ ___ _  __ _ _ _ __ _ __| (_)_ _  __ _
| |) / _ \ V  V / ' \/ _` | '_/ _` / _` | | ' \/ _` |
|___/\___/\_/\_/|_||_\__, |_| \__,_\__,_|_|_||_\__, |
                     |___/                     |___/
```

# Upgrading and Downgrading OpenBSD

During the install process, the operating system is downloaded in several archives referred to as "Installation
Sets". These "sets" can be enabled and disabled to the user’s preferences, but the reccommended and default setting is
to have them all enabled. 

## InstallURL
Then once they are downloaded and extracted onto the root file system, the file
`/etc/installurl` is created in the root filesystem. If you open the file to view it’s contents, you will see a solitary
line containing the URL where the installation sets were downloaded from. 

> [!NOTE] The `/etc/installurl` does not contain a full path to the installation sets, it only contains the path to the
> OpenBSD mirror. Since, the remaining portion of the installation sets path is uniform across all OpenBSD mirrors, it
> does not need to be stored in this file.

The mirror URL is recorded to ensure system conformity and congruity. i.e. To prevent your system from pulling from a
mirror which is either out of date or contains a change which will break your system. 

### Setting up your InstallURL

The InstallURL file only contains one mirror URL by default, BUT accepts comments, and can be more than one line in length. So,
it is a good idea to add one or two additional URLs to the file, and comment them out. This way, if for some reason a
mirror becomes inaccessible, OR YOU RECIEVE A FUNKY ERROR, you can uncomment one url and then comment out the previous
url, pulling upgrades from a different mirror url that is reachable.

The url pattern for an installurl uses the https protocol, an OpenBSD mirror url address, and uses `/pub/OpenBSD` as the
path. OpenBSD mirrors can be found on the [OpenBSD FTP page](https://www.openbsd.org/ftp.html). An example of an
installurl would be: `https://mirror.ungleich.ch/pub/OpenBSD/`. So if we picked three installurls at random the file
would look something like the file below:

```bash
# InstallURLS
# ------------------------------------------
# Comment or UnComment as needed
# ------------------------------------------
# https://mirror.ungleich.ch/pub/OpenBSD/
# https://ftp.nluug.nl/pub/OpenBSD/
https://ftp.cc.uoc.gr/pub/OpenBSD/
```

By doing this, you will be ensuring your system will always have a mirror which is reachable.

### Setting Up Package Path in your Environment

Back in the day, you stored the URL to download packages from as the environment variable `pkg_path`. This next trick
merely expands upon this step, and sets the URL for you in your shell initialization file. So, everytime you login, the
environment variable is automatically exported to the environment, where OpenBSD’s package manager will pick up on it
from there. 

Rather than hard code the URL into your shell initialization file, with the use of a little AWK, you can have this URL
match whatever URL is stored in `/etc/installurl` and dynamically load it.

They key is adding the below two lines to `.bashrc` or `.zshrc`, whichever you use. If you are currently following the
"SNAPSHOT", then leave it as it is provided. If you are following one of the releases, replace "snapshots" with the
release number you are currently on.

```bash
INSTALL_URL=$(awk -v RS="\n" '!/^#/ {print $0}' "/etc/installurl")
export PKG_PATH="$INSTALL_URL/snapshots/packages/amd64"
```

