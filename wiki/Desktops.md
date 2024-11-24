```text
#  ____            _    _                       _    _   _ ____
# |  _ \  ___  ___| | _| |_ ___  _ __  ___     / \  | \ | |  _ \
# | | | |/ _ \/ __| |/ / __/ _ \| '_ \/ __|   / _ \ |  \| | | | |
# | |_| |  __/\__ \   <| || (_) | |_) \__ \  / ___ \| |\  | |_| |
# |____/ \___||___/_|\_\\__\___/| .__/|___/ /_/   \_\_| \_|____/
#                               |_|
#
# __        ___           _
# \ \      / (_)_ __   __| | _____      __
#  \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / /
#   \ V  V / | | | | | (_| | (_) \ V  V /
#    \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/
#
#  __  __
# |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___
# | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/ __|
# | |  | | (_| | | | | (_| | (_| |  __/ |  \__ \
# |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|  |___/
#                           |___/
#
```

## Desktops and Window Managers for all ages and skillsets

Unix offers more variety and choice when it comes to Desktop environments than any other Operational platform.
This is due to Unix's age, and it's popular open source form of distribution. For new users, finally having
variety of choice in their life can lead to an existential crisis. Suddenly, they no longer know who they are,
and what it means to be "themselves". Eventually, they will migrate to being a nomad of desktop environments,
changing their environment once or twice a week for years. This form of migratory existence is quite
detrimental to the maturation of budding script kiddies. So it is for this reason we shall put forth a light
and incomprehensive list of Desktop Environments.

Before we begin our journey we must clarify something. For the purposes of this wiki entry we shall refer to
both desktop environments and window managers as desktop environments. In reality, there is a difference
between a desktop environment and a window manager, just as there is a difference between a central processing
unit and a computer. Window managers refer to software the manages rendering of windows/screens, where desktop
environments refer to homogenous working environment that window managers make up a part of. 

### Our Fucking Fantastic table of Desktop Environments

(Which will more than likely never fully reach anything close to resembling comprehensivity.)

For our fucking fantastic table of Desktop Environments we will:
* Define whether it is a Desktop Environment or a Window Manager.
* Whether it includes Sausages.
* Difficulty of setup.
* Skills needed for Setup.
* User Friendliness.
* Weight, referring to size and load.
* Graphics, referring to visual appeal
* Whether we reccommend or not.

| Name             | Sausages           | DE or WM   | Difficulty           | Skills Needed                    | Friendly             | Weight              | Graphics            | Reccommend                   |
| ------           | ----------         | ---------- | ------------         | ---------------                  | ----------           | --------            | ----------          | ------------                 |
| Gnome            | Too Many           | DE         | Easy                 | None                             | Very                 | Heavy               | Kuddos              | It's alright                 |
| KDE              | Abundant           | DE         | Harder than Gnome    | None                             | Very                 | Heavy               | It's got some       | Usable                       |
| XFCE             | Good Portioning    | DE         | Easy                 | None, besides it exists.         | Very                 | Moderately          | less than 2 above   | Sure.                        |
| lxqt             | Sparse             | DE         | Should be no problem | None                             | Easy going           | Reasonable          | less is more        | Yeah                         |
| Enlightenment    | Minimal            | DE         | Not really           | Little                           | Cool Beans           | Moderately          | Hell, Yeah. Shazam! | Definitely                   |
| [i3](i3)         | none               | WM         | Medium Rare          | Sh, and config files             | Just Right           | light               | Minimal             | We use it, so there.         |
| [bspwm](bspwm)   | Sausages exist?    | WM         | Hard                 | Sh & Bash                        | Not really           | Lighter than air    | With effort         | Promising                    |
| [xmonad](xmonad) | Does not compute   | WM         | Use at own risk!     | Ability to program Haskell well. | This WM hates you.   | lite, but not light | There are rumors    | Not unless your a masochist. |
| AwesomeWM        | Not a trace        | WM         | Medium - Hard        | Create the config file           | Done it, didn't cry. | Reasonably Light    | Minimal             | Could be fun for pros        |

#### FreeDesktop.org Spec Supported

Here is a list of desktop environments that are recognized as to following the freedesktop.org specification:

OnlyShowIn Value	Environment
COSMIC	COSMIC Desktop
GNOME	GNOME Desktop
GNOME-Classic	GNOME Classic Desktop
GNOME-Flashback	GNOME Flashback Desktop
KDE	KDE Desktop
LXDE	LXDE Desktop
LXQt	LXQt Desktop
MATE	MATÉ Desktop
Razor	Razor-qt Desktop
ROX	ROX Desktop
TDE	Trinity Desktop
Unity	Unity Shell
XFCE	XFCE Desktop
EDE	EDE Desktop
Cinnamon	Cinnamon Desktop
Pantheon	Pantheon Desktop
DDE	Deepin Desktop
Endless	Endless OS desktop
Old	Legacy menu systems

### Xsettings Daemon

Do not quote me on this, because I am no authority on the matter. After the occurrence of an issue with
getting GTK settings to apply to the menu bar of Sublime Text I learned about the role of the X settings
daemon. As it turns out, not all applications take their values directly from configuration files, some take
their values from an intermediary daemon. As anyone can guess, this intermediary daemon is referred to as the
"X Setting Daemon." Each of the major desktop environments possess their own flavor of the xsettings daemon,
but all serve the same purpose of reading configuration varables from various files and providing those
variables to the requesting program. It does need it's own configuration file available, `~/.xsettingsd`, but
what that configuration file is actually used for, is currently a mystery. As our local copy is completely
empty.

If you are like me, and do not run one of the big name desktop environments. The universal xsettings daemon is
"xsettingsd". Install it and create a blank configuration file, and your off to the races.
