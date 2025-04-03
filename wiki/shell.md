```text
#  ____  _          _ _
# / ___|| |__   ___| | |
# \___ \| '_ \ / _ \ | |
#  ___) | | | |  __/ | |
# |____/|_| |_|\___|_|_|
#
```

## The comforts of shell

Here is a nice introduction to shell. It explains what they are, what differentiates them from the command
line, and the different varieties of shell available.

* [Terminal Colors](https://github.com/termstandard/colors)

### Bash

Here is where I write a nice introduction about the Bourne again shell.

Here is my page to the wiki page for bash --> [bash](bash)

* [Basher](https://www.basher.it)
* [bash-it](https://github.com/Bash-it/bash-it)

### ZSH

Here is where I take a stab at explaining what ZSH is, and why zsh differs from bash.

Here is my page on zsh --> [zsh](zsh)

* [zi](https://github.com/z-shell/zi)

### Neat tricks

This section is to cover neat tricks that are too cool to be tucked away in a section of their own.

#### Using EOF to write a file in your shell

```bash
cat <<EOF> $FILE
> #!/usr/bin/env bash
> echo "Do something really cool!"
> EOF
```

#### Restart on configuration file change

This script is worth taking notice, because parts of it have been used numerous times in other scripts to aid in launching
applications, and ensuring those applications remain running. This particular script just comes with an
additional feature, which is to continuously check configuration files for changes.

```bash
#!/usr/bin/env bash

# Variables
CONFIG="$HOME/.config/hypr/waybar"
WAYCONFIG="$CONFIG/config"
WAYSTYLE="$CONFIG/style.css"

# start waybar if not started
if ! pgrep -x "waybar" > /dev/null; then
	hyprctl keyword exec waybar -b "bar" --config "$WAYCONFIG"
fi

# current checksums
current_checksum_config=$(md5sum "$WAYCONFIG")
current_checksum_style=$(md5sum "$WAYSTYLE")

# loop forever
while true; do
	# new checksums
	new_checksum_config=$(md5sum "$WAYCONFIG")
	new_checksum_style=$(md5sum "$WAYSTYLE")

	# if checksums are different
	if [ "$current_checksum_config" != "$new_checksum_config" ] || [ "$current_checksum_style" != "$new_checksum_style" ]; then
		# kill waybar
		killall waybar

		# start waybar
		waybar &

		# update checksums
		current_checksum_config=$new_checksum_config
		current_checksum_style=$new_checksum_style
	fi
done
```

#### Common case switch for bash

Just a basic example of using case in bash.

```bash
case "$1" in
  start | up)
    vagrant up
    ;;

  *)
    echo "Usage: $0 {start|stop|ssh}"
    ;;
esac

```

#### Download latest Github Release of a project

This is a snippet of a script that will download the latest release of an application.

```bash
#!/usr/bin/env bash

PROFILE=""
PROJECT=""
OUTFILE=""
ENDFILE=""
 
VERSION=$(curl -s "https://api.github.com/repos/$PROFILE/$PROJECT/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
 
curl -Lo "$OUTFILE" "https://github.com/$PROFILE/$PROJECT/releases/download/v${VERSION}/$PROJECT_${VERSION}_Linux_x86_64.tar.gz"
 
tar xf $OUTFILE $ENDFILE
 
sudo install $ENDFILE -D -t /usr/local/bin/
```

### New Commands

Recently a few new commands have been encountered, that have never been seen before. Unsure if they are new arrivals
or if they are older commands which were unknown of. Either way, they listed below.

#### newgrp

Newgroup allows a user to initiate and finalize changes to group membership without having to log out and in again.
This feature becomes handy when the user does not need to lose any established environment variables.

#### Pushd

Pushd comes from perl, and appears to be part of the standard perl package. The best way to describe the
functionality of pushd is to think of it as a temporary change directory command. As it allows the user to designate a
directory to change into, and when ready, executing the command again without any arguements then will return the
user back to the directory he started out in. 
