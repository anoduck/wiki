```text
#  ____
# | __ )  _____  _____  ___
# |  _ \ / _ \ \/ / _ \/ __|
# | |_) | (_) >  <  __/\__ \
# |____/ \___/_/\_\___||___/
#
```

## Boxes - Draw ascii art borders in your terminal.

[Main site for Boxes](https://boxes.thomasjensen.com/)

### Intro 

Boxes is a command line tool that injects ascii art into a designated file or outputs it to the command line.
It can be integrated into several of the more popular text editors, comes with several predefined designs, and
even allows a method for users to add their own designs. 

### Config file

Like most configuration files these days, the user's copy is kept in `~/.config/boxes/config`, and it is in
this file where users may add their own ascii art designs toe the program. Below is a layout of the
configuration file.

__Box Design__

```boxes
BOX $(design_name)
    $(entries_and_blocks)
END $(design_name)
```
