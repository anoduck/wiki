```text
#  _     _                  __ _
# | | __| | ___ ___  _ __  / _(_) __ _
# | |/ _` |/ __/ _ \| '_ \| |_| |/ _` |
# | | (_| | (_| (_) | | | |  _| | (_| |
# |_|\__,_|\___\___/|_| |_|_| |_|\__, |
#                                |___/
#
```

## Fixing ldconfig libraries.

After a catastrophic experience, I have since avoided tinkering with `ldconfig`, and in general it should
remain left alone, and for the system to manage. For those who did not heed this warning, below is how to
return ldconfig back to a state of normality.

### With regard to ldconfig:

*I do not follow the recommended convention of using `doas` , mainly because doas came after my use of OpenBSD, the  installation of sudo on my system, and after I had already disabled login for root. Also, it is bloody tedious having to type `doas` for every single command.*

1. `sudo cat /etc/rc.conf.local` ensure that you do not see a line that begins with `shlib_dirs`. If you do, delete it. The default installation does not have one.
2. run `sudo ldconfig -U` and see if this fixes it.
3. If the above does not fix it, then you are going to need to be brave. Run `sudo rm /var/run/ld.so.hints` , then run `sudo ldconfig -R` and this should regenerate your `/var/run/ld.so.hints` file. If it outputs an error that `/var/run/ld.so.hints` cannot be found, then run the command without the `-R` flag. So, just `sudo ldconfig`. This should clear up everything.
4. Check to see if the hints file exists. `sudo ldconfig -r`.
5. Reboot your system.
