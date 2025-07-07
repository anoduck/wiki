```text
# __        ___           _
# \ \      / (_)_ __   __| | _____      _____
#  \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / __|
#   \ V  V / | | | | | (_| | (_) \ V  V /\__ \
#    \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ |___/
#
```

Microsoft Windows
=================

Admittedly, things were said, and mistakes were made. Not saying that is all behind us now, but you can't beat a dead horse.

CMD is not PowerShell
---------------------

Both are shell environments for windows, but the availability of commands differs between the two. Powershell was intended to be used
by experienced system administrators and other power users. This is because it has object oriented scripting
as one of it's primary features. Although this feature provides many benefits, it does change how the shell
handles arguments and executes commands. CMD is intended for your more rudimentary operations where the
advanced features of powershell are not required. Regardless, CMD is still the default "go-to" shell environment for windows,
and this is not likely to change.

CMD Snippets
-------------

Just a few snippets of commands for Windows terminal. 

### Download a file with Curl.

Windows 10 now comes with `curl.exe`, just keep in mind the flags are different.

To download a file with curl granting it a specific name, you would use:

```cmd
curl.exe -o $OUTPUT_FILE $URL
```

To download a file with curl allowing it to keep it's default name, you would use:

```cmd
curl -O $URL
```

### Extracting a zip

Extracting a zip archive in windows is surprisingly similar to extracting an archive in Unix. 

```cmd
tar -xf $ARCHIVE
```

References
----------

- [Windows Curl Cheatsheet](https://gist.github.com/jimmyFlash/0d96b9f6026507129ac9270a0587e1d0)
