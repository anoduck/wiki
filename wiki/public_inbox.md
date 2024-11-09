```text
#  ____        _     _ _        ___       _
# |  _ \ _   _| |__ | (_) ___  |_ _|_ __ | |__   _____  __
# | |_) | | | | '_ \| | |/ __|  | || '_ \| '_ \ / _ \ \/ /
# |  __/| |_| | |_) | | | (__   | || | | | |_) | (_) >  <
# |_|    \__,_|_.__/|_|_|\___| |___|_| |_|_.__/ \___/_/\_\
#
```

Public Inbox
------------

Public Inbox is a mailing list manager that takes a "archives first" approach to management. It is a project
we have developed considerable interested in for sometime now.

### Installation

Installing in any debian based system is as easy as pie.

The software source code repository can be fetched over tor.
`torsocks git clone http://7fh6tueqddpjyxjmgtdiueylzoqt6pt7hec3pukyptlmohoowvhde4yd.onion/public-inbox.git`

Dependencies and optional dependencies can be installed with:
`sudo apt install git perl libdbd-sqlite3-perl liburi-perl postfix spamassassin libsearch-xapian-perl
libinline-c-perl libemail-address-xs-perl libparse-recdescent-perl libmail-imapclient-perl
libbsd-resource-perl libplack-perl libtimedate-perl libplack-middleware-reverseparoxy-perl libhighlight-perl
xapian-tools curl liblinux-inotify2-perl libnet-server-perl`

Once these are installed, you will need the MakeMaker perl library to perform the make process. Which can be
installed with cpanm.
`cpanm install ExtUtils::MakeMaker`

Then you are ready to build.
```bash
perl Makefile.PL
make
make test # Always optional, usually skipped
sudo make install
```

If you desire to run the service on the user level, you can use the symlink-install tool, which is located in
the repository as well. NOTE: running this tool will generate symlinks in `$HOME/bin`.

```bash
perl Makefile.PL
make symlink-install prefix=$HOME
```

Once you reach this point, you are ready to read the rest of [the documentation here](https://public-inbox.org).

### Reference Links

- [Github Repository for the project](https://github.com/nojb/public-inbox)
- [Official Project Site](https://public-inbox.org)
