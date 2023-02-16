```text
#  _____ _           _          _     _____
# |  ___(_)_  __    / \   _ __ | |_  | ____|_ __ _ __ ___  _ __ ___
# | |_  | \ \/ /   / _ \ | '_ \| __| |  _| | '__| '__/ _ \| '__/ __|
# |  _| | |>  <   / ___ \| |_) | |_  | |___| |  | | | (_) | |  \__ \
# |_|   |_/_/\_\ /_/   \_\ .__/ \__| |_____|_|  |_|  \___/|_|  |___/
#                        |_|
#
```

## Fix Apt Errors

It is a rare occurrence, but it is only a matter of time until you run into an error with apt. So here are
some errors and ways to fix them.

### dpkg: error processing archive ... (--unpack): trying to overwrite

Note that packages for apt are stored in `/var/cache/apt/archives/*`.

Use the following command replacing `$PACKAGE` with the full name of the package including version number that is having difficulty.

```bash
sudo dpkg -i --force-overwrite /var/cache/apt/archives/$PACKAGE.deb
```
