```txt
#  ____  __  __ ____
# |  _ \|  \/  |___ \
# | |_) | |\/| | __) |
# |  __/| |  | |/ __/
# |_|   |_|  |_|_____|
#
```

## PM2: Perhaps the most underrated service manager in existence.

I have been a fan of pm2 for sometime, and frankly don't know why everyone else isn't absolutely crazy about
using it. It practically needs zero configuration, installs in seconds, and is ready to run whatever the hell
you want with a simple command.

Just for reference, the official website is [pm2.keymetrics.io](https://pm2.keymetrics.io) It is nice, you
should visit it.

### Install

To install pm2, you need to have already installed nodejs and npm on your system, afterwards simply execute `sudo
npm install -g pm2`, and you are ready to rock with the best of them.

### Starting a service

To start whatever the hell you want as a service you only need to: `pm2 start whatever-the-hell`

### Starting a service that requires flags

To start a service that requires a flag, or a service that has mandatory options. Encase the command and
options in double quotations. Like so:

`pm2 start "whatever-the-hell --option arg1 --option arg2" --name whatever-the-hell -- other args for command`

Doing so prevents word splitting and contains the service command with options together for pm2 to run as a whole
command. Notice the additional flag outside the double quotes, it is directed at pm2, and not the command
pm2 is running. Using `--name` gives your service a clean service name, where normally the flag would include
the flags used as well.

### Bash Completion

To configure bash completeion: `pm2 completion >> ~/.bashrc`

### configuring pm2 to start on system boot

Only slightly more involved than the above.

1. run: `pm2 startup`
2. The above will output a command that needs to be run to set up start on boot.
3. In our case this is: `sudo env PATH=$PATH:/home/user/.nvm/versions/node/v16.4.0/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup systemd -u user --hp /home/user`
4. Start the service with systemd. `sudo systemctl start pm2`
5. Start the app/service you want to run on startup `pm2 start whatever-the-hell`
6. Then freeze (save) pm2's list of services. `pm2 save`
7. Done.

If you need to, or desire to, remove it at a later point in time. Just run `pm2 unstartup`.

### Other Miscellaneous commands

| monit       | Spawns a monitoring dashboard in the terminal |
| list/status | Lists services being managed                  |
| ping        | Checks to see if service is running           |

### Benefitial flags

| `--name`               | Ascribe a name to the command.         |
| `--log $LOG_FILE`      | Log output to file.                    |
| `--`                   | Pass extra arguments to the script (?) |
| `--time`               | Add time to log file.                  |
| `--watch`              | Restart when files change              |
| `--restart-delay`      | Delay between auto restart             |
| `--no-autorestart`     | Do not restart                         |
| `--cron $cron_pattern` | Specify cron for forced restrart       |
