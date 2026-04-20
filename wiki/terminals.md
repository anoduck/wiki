```txt
#  _____ _____ ____  __  __ ___ _   _    _    _
# |_   _| ____|  _ \|  \/  |_ _| \ | |  / \  | |
#   | | |  _| | |_) | |\/| || ||  \| | / _ \ | |
#   | | | |___|  _ <| |  | || || |\  |/ ___ \| |___
#   |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_____|
#
#  _____ __  __ _   _ _        _  _____ ___  ____  ____
# | ____|  \/  | | | | |      / \|_   _/ _ \|  _ \/ ___|
# |  _| | |\/| | | | | |     / _ \ | || | | | |_) \___ \
# | |___| |  | | |_| | |___ / ___ \| || |_| |  _ < ___) |
# |_____|_|  |_|\___/|_____/_/   \_\_| \___/|_| \_\____/
```

    Phazers on kill, photon torpedo.

# Terminal Emulators

As the name would suggest a terminal emulator is a program that emulates a terminal. No, big surprise there,
but what exactly is a terminal? Now, that question gets a little more complicated, because terminals are often
referred to by different names that all mean the same thing. In Windon't the terminal is often referred to as
a "command line", which is, a line in which the user types commands into. "Consoles" and "Terminals" are
almost synonymous with each other, and even the wikipedia page redirects console to terminal, although the
origin of their use differs historically. Back in the early days of computing, a terminal was an actual
piece of hardware which would provide the user with a means of inputting data and outputting feedback from the
system in use. The term "terminal" infers an activity of transportation and/or communication, while the term
"console" infers a physical device performing the activity of input. 

Circumventing a lot of irrelevant history, explanations, and bring the introduction to a close. Today, modern
terminals are the primary means by which interaction between the user and the computer take place. There are a
lot of different types out there, with a cornicopea of different features. While some are particularly more
featureful than others, it all comes down to how one wants to use it, the trade off between features and
footprint, and what one is comfortable with.

A nice list can be found [Here](https://wiki.archlinux.org/title/List_of_applications/Utilities#Terminal_emulators).

## Kitty

Kitty is the terminal emulator I use most. I like kitty a lot.

## Zutty

Zutty is supposed to be an abbreviation for a "zero cost tty". It is quite similar to other barebone
minimalistic terminal emulators, such as the classic XTerm, URxvt, Sakura, and ST. Although, it claims to be
much faster and better at rendering fonts. 

Just as with Xterm and URxvt, configuration for zutty is performed in the `~/.Xresources` file.

```Xresources
Zutty.title:    The Big Zutty
Zutty.geometry: 120x45
Zutty.border:   5
Zutty.font:     Iosevka Term Nerd Font Complete Mono
Zutty.fontsize: 10
Zutty.fg:       00ff80
Zutty.bg:       203040
Zutty.color0:   #1c1b19
Zutty.color1:   #ef2f27
Zutty.color2:   #519f50
Zutty.color3:   #fbb829
Zutty.color4:   #2c78bf
Zutty.color5:   #e02c6d
Zutty.color6:   #0aaeb3
Zutty.color7:   #d0bfa1
Zutty.color8:   #918175
Zutty.color9:   #f75341
Zutty.color10:  #98bc37
Zutty.color11:  #fed06e
Zutty.color12:  #68a8e4
Zutty.color13:  #ff5c8f
Zutty.color14:  #53fde9
Zutty.color15:  #fce8c3
```
