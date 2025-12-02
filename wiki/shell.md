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

### Require SuperUser Privileges

While performing some server configuration work, this convenient script was written to make copying the
configuration file over and restarting the server more convenient. It's importance is the simple conditional
that requires a user to have SuperUser Privileges in order to run. Appropriate slang included for variety.

```bash
#!/usr/bin/env bash

HTTPDIR="/etc/httpd.conf.d"
REPODIR="/local/location/of/files"

if [ "$EUID" -ne 0 ]; then
  echo "Yo! You gotta be root to run this shit! Fool!"
  echo "Try using sudo."
  exit
else
  echo "Nice, Playa! Word to your momma."
  sleep 1
fi

UFILE="$REPODIR/$1"
SFILE="$HTTPDIR/$1"

if ! [[ -f "$UFILE" ]]; then
  echo "Argument must be a configuration file located in $REPODIR"
  exit
fi

USUM=$(cat "$UFILE" | md5)
SSUM=$(cat "$SFILE" | md5)

if [[ "$USUM" == "$SSUM" ]]; then
  echo "Both files are the same."
  exit
else
  if [[ "$UFILE" -nt "$SFILE" ]]; then
    echo "Replacing httpd configuration file and reloading server"
    cp "$UFILE" "$SFILE"
    rcctl restart httpd
    echo "Done."
  else
    if [[ "$SFILE" -nt "$UFILE" ]]; then
      echo "Replacing file in repository."
      cp "$SFILE" "$UFILE"
      chown "$USER" "$UFILE"
      chmod 0755 "$UFILE"
      echo "Done"
    fi
  fi
fi
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
##### More Advanced Example of a case switch for bash

This example was directly taken from a deprecated script once used to launch a
remote desktop session using one of several methods.

```bash
while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do case "$1" in
	-a | --autossh )
		run_autossh
		;;
	-s | --ssh )
		RUN_HYPR=false
		run_ssh
		;;
	-r | --hypr )
		RUN_HYPR=true
		run_ssh
		;;
	-k | --kill )
		kill_all
		;;
	-v | --vnc )
		"$VNC_CMD"
		;;
	_)
		run_ssh
		;;
esac; shift; done
if [[ "$1" == '--' ]]; then shift; fi
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

#### Upgrade godns

This takes part of the snippet above and actually integrates it into a working example of upgrading godns. It
first checks to see if the current version and the current release are the same, if so nothing is done, if not
so it downloads and installs the newest release.

<script src="https://gist.github.com/anoduck/e550043126876f2c7db0df2fb8588fae.js"></script>

#### Recursively find and replace string

Quite easily actually.

```bash
find /some/path \(-type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i 's/some_phrase/some_replacement/g'
```

#### Use SSH to run a series of commands on a remote machine.

```bash
ssh otherhost << EOF
  ls some_folder; 
  ./someaction.sh 'some params'
  pwd
  ./some_other_action 'other params'
EOF
```

#### Use SFTP in a shell script to upload or download a file.

``` bash
HOST='your_sftp_server'
USER='your_username'
PASSWORD='your_password'
LOCAL_FILE='/path/to/local/file.txt'
REMOTE_DIR='/path/to/remote/directory/'

sftp $USER@$HOST <<EOF
put $LOCAL_FILE $REMOTE_DIR
bye
EOF
```

### Newly Discovered Commands

Recently a few new commands have been encountered, that have never been seen before, or I have seen and didn't care to
investigate. Either way, they listed below to help me remember them for later.

#### newgrp

Newgroup allows a user to initiate and finalize changes to group membership without having to log out and in again.
This feature becomes handy when the user does not need to lose any established environment variables.

#### Directory Stack

Both Bash and Zsh provide a virtual directory stack used to aid navigation through complex paths. The utilization of this stack
is performed with the `pushd` command, the removal of entries from this stack is performed with the `popd` command, and the viewing of this
stack is performed with the `dirs` command. Each are discussed more fully below.

##### Pushd and dirs

Pushd is a built in shell command that is known to come with both bash and zsh, Perl also has an implementation
for convenience. Pushd is designed to ease navigation of complex paths by adding those paths to an internal virtual stack.
Adding a path to the network stack places the path on top of the stack, meaning it will be positioned first, and first used
when pushd is used again. At anytime the user can view this stack by executing the `dirs -l -v` command. Which will provide
the user with a numbered list of paths which represents the virtual directory stack.

```bash
>~ dirs -l -v
0	/home/user
1	/
2	/home/user
3	/home/user/.emacs.d/init.d
4	/home/user/Projects
5	/home/user/Projects/clifm
6	/home/user/Downloads
7	/home/user/Projects/The_Duck
8	/home/user/Projects/vnc
9	/home/user/Projects/Scripts
10	/home/user/Projects/texstudio/build
11	/home/user/Projects/texstudio
12	/home/user/Projects/Wireguard
13	/home/user/Projects/GameBoy
14	/home/user/Projects/latex-work
15	/home/user/Documents/Risc-V/docs
```

Using `pushd ${SOME-DIRECTORY}` will change directory to `${SOME-DIRECTORY}` AND add that directory to the top of the virtual
directory stack. If you issue `pushd -n ${SOME-DIRECTORY}` pushd with the `-n` flag, the directory will only be "pushed" to
the top of the directory stack, and your current directory will remain the same.

As it's purpose would suggest, the user can fully utilize this virtual directory stack and navigate to any path in the stack by
issuing a `pushd +{SOME-NUMBER}` or `pushd -{SOME-NUMBER}`, where `{SOME-NUMBER}` is the "Nth" path in the stack. Using a "+" 
(plus or positive symbol) will count upward from the bottom of the stack to the "Nth" entry, and using a "-" (minus or negative
symbol) prefix will count downward from the top of the stack. Thus, referencing the example stack above, `pushd +3` will change
directory to `/home/user/.emacs.d/init.d`, and `pushd -3` will change directory to `/home/user/projects/GameBoy`.

##### Popd

Popd operates in much the same manner as pushd does, except rather than add paths to the directory stack, popd removes them. So,
similar to pushd, `popd ${SOME-DIRECTORY}` changes directory to `${SOME-DIRECTORY}`, and then removes that directory from the directory
stack. Use of the `-n` flag will only remove the directory from stack, and use of "+/-" will allow the user to remove the "Nth"
directory, and not change directory as well.

#### Compgen

Compgen can be used to list every command available within a shell. As expected, the output of this command can be manipulated with flags,
which is discussed below.

- `compgen -c` outputs all available commands.
- `compgen -a` outputs all available aliases.
- `compgen -b` outputs all available shell builtin commands.
- `compgen -k` will output all keywords.
- `compgen -A` for all functions.

#### Test

I have seen this command thousands of times, but never considered including it in my own scripts until now,
and it really is incredible. Test simplifies and reduces the complexity of scripts by handling the "if...then" clause for you.
So, instead of having to write the entire block to test an expression, you can simply run `test $EXPRESSION`
and if it is true it will return not return anything, but if it is false it will return "1". Examine the
example below.

```bash
# Long format
if [[ -e "/var/www/htdocs" ]]; then 
    echo "Geronimo!!!"
fi

# Now with test
test -e /var/www/htdocs
```
