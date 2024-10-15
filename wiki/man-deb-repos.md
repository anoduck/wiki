```text
#  __  __                         _               ____       _
# |  \/  | __ _ _ __   __ _  __ _(_)_ __   __ _  |  _ \  ___| |__
# | |\/| |/ _` | '_ \ / _` |/ _` | | '_ \ / _` | | | | |/ _ \ '_ \
# | |  | | (_| | | | | (_| | (_| | | | | | (_| | | |_| |  __/ |_) |
# |_|  |_|\__,_|_| |_|\__,_|\__, |_|_| |_|\__, | |____/ \___|_.__/
#                           |___/         |___/
#  ____                      _ _             _
# |  _ \ ___ _ __   ___  ___(_) |_ ___  _ __(_) ___  ___
# | |_) / _ \ '_ \ / _ \/ __| | __/ _ \| '__| |/ _ \/ __|
# |  _ <  __/ |_) | (_) \__ \ | || (_) | |  | |  __/\__ \
# |_| \_\___| .__/ \___/|___/_|\__\___/|_|  |_|\___||___/
#           |_|
```

Managing Deb/Ubuntu Repos
-------------------------

To our understanding the use of `sudo apt-key add` is not deprecated in Ubuntu, but for Debian and it's derivates,
it is no longer a valid method to add repositories to your package manager's source list. So, because discovering
the proper way to do it can take more time than one would like, we are going to cover how to do this here.

### Determining your release alias

By saying "release alias", what we are referring to is the debian equivocal release of your operating system. If you are actually
running debian, then congrats, you can move on to the next step. If you are running a derivative of debian, then you will need to know
what is the debian equivalent of the release of your system. For Kali Linux this is rather easy, Kali is based off of "sid", in other words
debian unstable. Many third party repositories will only support stable releases of Debian, so you might have to go to [the debian
website](https://www.debian.org/releases/) and find out what the newest stable release is. At the time of writing this, this would
be bookworm.

### Acquire the GPG key

Gpg keys for repositories are now stored in `/etc/apt/trusted.gpg.d/`, and you will need to dearmor the gpg key before putting it there.

```bash
wget -qO- https://download.example.com/example-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/example.gpg > /dev/null
```

### Constructing the repository's list file contents

Apt uses "list" files to reference what repositories it should look into to discover software packages and updates. "Back in the day",
this was composed entirely of one file `/etc/apt/sources.list`, but as it became more and more common to use third party repositories, they went with a multi-file
approach. So now each repository has it's own individual file located within `/etc/apt/sources.list.d/`.

Most third party repositories will follow the format of the example below, but there are exceptions. The place where you will see the most
variation is in the URL path. As mentioned, most of them will use the distrobution, debian, but some will use the release, and others will
use a combination of the two. Some will designate their repository as being a "main" repository, and others will declare it as a "contrib"
repository, this matters little. Finally, some repos will not use the codename for the release, but will refer to the stability of the release.
This is extremely convenient, as it allows one to leave the repository configuration untouched while upgrading to a newer release.

Lastly, remember the obvious, just because an application has a repository listed as an installation method, doesn't mean the repository is maintained or even available.

```bash
echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/example.gpg] https://download.example.com/example/debian bookworm main' >> sudo tee -a /etc/apt/sources.list.d/example.list
```
