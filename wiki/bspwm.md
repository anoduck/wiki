```text
#  ____ ____  ______        ____  __
# | __ ) ___||  _ \ \      / /  \/  |
# |  _ \___ \| |_) \ \ /\ / /| |\/| |
# | |_) |__) |  __/ \ V  V / | |  | |
# |____/____/|_|     \_/\_/  |_|  |_|
#
```

## BSPWM: A window manager implemented completely in shell scripts

Sounds promising? Yes, it most definitely does, but only if you are at home with writing
shell scripts, and you understand you will have to manually configure everything for this 
window manager. Just as a point of information, catching erros can be a real bitch on remote 
platforms, and it is required that you configure first before running anything.

### Configuration

It was introduced as a WM completely implemented in sh, but don't let that fool you. BSPWM definitely
has a configuration syntax of it's own that has to be followed in order to successfully set it up. Also,
and rather disappointingly, BSPWM does not handle any keybinds. Keybinds are handled by BSPWM's sister program
`sxhd`, and it has it's own configuration syntax that cannot be implemented in shell, and is completely
different than BSPWM's. If you plan on using BSPWM on a remote computer, understand that if you fuck up your configuration, then you
will be served a black screen with a mouse pointer. There will be no menus, no terminal, nor windows, it will
be a proverbial empty shell of a window manager.

Saying all of that, configuration can be pretty convenient due to it being in sh, and BSPWM is incredibly
flexible, customizable, and lighter than a binary feather.
