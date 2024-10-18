```text
#   ____                           _   _____
#  / ___| ___ _ __   ___ _ __ __ _| | | ____|_ __ ___   __ _  ___ ___
# | |  _ / _ \ '_ \ / _ \ '__/ _` | | |  _| | '_ ` _ \ / _` |/ __/ __|
# | |_| |  __/ | | |  __/ | | (_| | | | |___| | | | | | (_| | (__\__ \
#  \____|\___|_| |_|\___|_|  \__,_|_| |_____|_| |_| |_|\__,_|\___|___/
#
#  ___        __
# |_ _|_ __  / _| ___
#  | || '_ \| |_ / _ \
#  | || | | |  _| (_) |
# |___|_| |_|_|  \___/
#
```

# General Emacs Knowledge

Here is where we will discuss knowledge pertaining to emacs use in general.

## Tweaking Emacs' Performance Environment

The two variables most responsible for performance are `max-lisp-eval-depth` and `max-specpdl-size`.
Max-lisp-eval-depth is somewhat self explanatory, it controls the depth of which lisp functions are evaluated.
Max-specpdl-size is less obvious, and controls the size of the stack. Both can be increased to some degree to
a relatively high amount, but if this setting is too high the user will recieve a `stack overflow` error.

```elisp
(setq max-lisp-eval-depth 8000)
(setq max-specpdl-size 8000)

```

Just FYI: In my experience it is best if these two settings are left alone to allow packages to define them
dynamically, rather than assign them permanently at a single value. (Yes, even with lsp-mode installed)

### Inserting Symbols

A word or two on keymap markup. Emacs shortcodes often take place in the form of pairs, these pairs are
referred to as "key chords". The two most common of which are `C-x` and `C-c`, which represent `Ctrl+x` and
`Ctrl-c`. Notice the difference in notation there? In these key sequences, "Control" is represented simply as
a capital "c", where a capital "c" would be represented as `S-c` for `Shift+c`, which is what you would press
to get a capitalized "c". The "Meta" key, more commonly known as "Alt", is represented as `M`, for meta.
Spaces in Emacs keymap notation are to be interpreted as breaks in the sequence, naturally. So, a
sequence of `C-x C-s`, represents a chord of `C-x` followed by the second chord of `C-s`. Which is used to
save the current buffer to file.

It really is not rocket science, and something any user would probably pickup on with time and experience.
Just be aware, keychords can get quite complex and cumbersome. One particular key chord has jovially been
referred to as the klingon death grip.

#### Inserting the section symbol

To insert a section symbol in Emacs: `C-x 8 S-s`

### Taming Frames and Windows

The important thing to keep in mind, is that contrary to what most users are used to, these two labels are
reversed in Emacs. That is, what users normally refer to as windows are referred to as frames in emacs, and
what users normally refer to as frames are referred to as windows in Emacs.

Confused yet? Nope, good.

A common behavior of emacs is to open new popup frames for temporary buffers, this can be really annoying for
users of certain window managers like ion and bspwm.  One way to avoid this is implementing one's own
[OneOnOneEmacs](https://www.emacswiki.org/emacs/OneOnOneEmacs). Although, implementation of this is rather
involved, so for some of us a simple enabling of popup windows will suffice. Below is the code to insert into
your configuration file.

```elisp
(setq pop-up-frames t)
```

### Ending the tyrrany of horizontally split temporary windows.

This is a little biased, but for me anyway, the creation of windows that are split horizontally for temporary
windows is disruptive to my workflow. The only time this is desired is when working on two files, so one can
sit beside the other. To achieve this add the following line to your configuration file.

```elisp
(setq split-width-threshold 9999)
```

To do the exact opposite, and have Emacs split natively vertically you would set the opposite value.

```elisp
(setq split-height-threshold 9999)
```

-----
