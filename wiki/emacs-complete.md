```text
#  _____
# | ____|_ __ ___   __ _  ___ ___
# |  _| | '_ ` _ \ / _` |/ __/ __|
# | |___| | | | | | (_| | (__\__ \
# |_____|_| |_| |_|\__,_|\___|___/
#
#   ____                      _      _   _
#  / ___|___  _ __ ___  _ __ | | ___| |_(_) ___  _ __
# | |   / _ \| '_ ` _ \| '_ \| |/ _ \ __| |/ _ \| '_ \
# | |__| (_) | | | | | | |_) | |  __/ |_| | (_) | | | |
#  \____\___/|_| |_| |_| .__/|_|\___|\__|_|\___/|_| |_|
#                      |_|
#
```

## Completion in Emacs

There is a lot more to configuring emacs completion than one might thing, and there are even greater ways to
customize completion than one might desire. The distinction to make is where you want the completion
performed, how you want it performed, how to perform it, and what do you want included in it's performance.

### Completion overview.

* Where is completion performed?

Emacs generally provides two most common places to perform completion:

1. In the minibuffer
2. In the main buffer.

* How is completion performed?

Customization of Emac's completion system is completely customizable and dependent on the completion engine in
use.

* What completion engines are available for completion?

1. Native completion - Emacs actually comes with it's own completion system.
2. Company Mode - is by far the most popular completion engine available for emacs. It is also probably the
   	 most customizable, and deeply developed.
3. Auto-Complete - is another extremely popular completion engine for emacs.
4. Corfu - Corfu is a new arrival on the completion scene, and is perhaps the most flexible option. It plays
	 well with company-mode, and can use many of company's libraries for completion.


### Links

* https://github.com/radian-software/prescient.el
* https://github.com/minad/corfu
