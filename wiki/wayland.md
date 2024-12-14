```text
# __        __          _                 _
# \ \      / /_ _ _   _| | __ _ _ __   __| |
#  \ \ /\ / / _` | | | | |/ _` | '_ \ / _` |
#   \ V  V / (_| | |_| | | (_| | | | | (_| |
#    \_/\_/ \__,_|\__, |_|\__,_|_| |_|\__,_|
#                 |___/
#
```

## Wayland: The replacement of X.

For some reason or another, I always associate Wayland with some slick haired country music singer that smells
of wiskey, cigarettes, and cologne. Not dissing it, just saying...

### Sections

| [Sway](sway) | [Hyprland](hyprland) | [launchers](launchers) |

### WTF, is it?

Well, that is a good question. Supposedly it is the long awaited successor to the X windows system. So, it
replaces X, not compliments it. In the X windows system, X acts as a server that controls the display functions
of the system, and serves those capabilities to the client, which in most cases is the desktop environment. On
wayland, the server-client model is eliminated, and desktops environments directly control all display
capabilities. You would naturally assume, wayland to have a smaller footprint and possess a lighter load on
the system running it, but you would be wrong. Due to it's mature codebase and refinements over the years, X
possesses the lighter footprint and significantly lighter load.

#### How do I implement it?

Although, not necessarily a fun job to perform, it is very doable. Programs that are X specific will need to be replaced
with a Wayland equivalents. This means your Desktop Environment, display manager, terminal, and your vnc server, if you have one, 
will all need to be replaced with their wayland counterpart. Before you do, you need to have settled on which
wayland implementation you plan on using. This is to to ensure uniformity and avoid conflicts in design. Once
done, you will need to setup the desktop environment manager to start on system start, this in turn is what
will start wayland for you after logging in. 

The most crucial part is to ensure you have Xwayland installed and started by you wayland implementation after
login. The Xwayland program provides the necessary libraries and support to allow you to run programs designed
to run on X to be run on wayland. So, to put it simply, Xwayland acts as an adapter for your X programs.

### How do you get rid of it?

Removing wayland is no biggie either, but isn't necessarily fun either. You will need to reinstall whatever
X11 Desktop environment you desire to run as well as X-server if required. If you are going to use a display
manager, then you will need to enable it at some point. Before you do, discover how wayland is started on your
system. Often this involves the inclusion of a script in your user profile or shell rc file. Which ever is in
use, make sure to disable it. Only then should you use `systemctl enable $YOUR-DISPLAY-MANAGER`. Only begin
to uninstall wayland's components when you have successfully finished the transition back to X.

### References

Most of the references used for our local implementation of wayland and sway came from the archlinux wiki. 

- [Sway](https://wiki.archlinux.org/title/Sway)
- [Wayland](https://wiki.archlinux.org/title/Wayland)
