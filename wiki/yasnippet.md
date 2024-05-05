```text
# __   __              _                  _
# \ \ / /_ _ ___ _ __ (_)_ __  _ __   ___| |_
#  \ V / _` / __| '_ \| | '_ \| '_ \ / _ \ __|
#   | | (_| \__ \ | | | | |_) | |_) |  __/ |_
#   |_|\__,_|___/_| |_|_| .__/| .__/ \___|\__|
#                       |_|   |_|
#
```

Yasnippets
==========

The Emacs snippet manager
--------------------------

Where there are many packages to manage snippets in emacs, yasnippets is by far the most complete and robust
solution. With robustness and completeness, unfortunately, also comes weight, and for this reason there are
many other snippet managers that one might prefer. Although, to our knowledge, none of these other snippet
managers come with the option to install quite a generous collection of premade snippets.

### Installation

As with all packages in our Emacs configuration, package installation is performed using `straight.el`
integrated with the famous `use-package.el` package configuration system. Using this, all one needs to do is
simply add the below block of code to your emacs configuration file.

```elisp
(use-package yasnippet)
```

and your done.

### Writing snippets

Yasnippets has it's own file format and mode for handling said format. Creation of snippets can be done by
executing the command `yas-new-snippet` or `C-c C-n` on the keyboard. If you go this route, when finished, all
one needs to do is hit `C-x C-s` and a dialogue will ask you what mode is the snippet for, and then will ask
for confirmation of the location to save the file. Snippets are generally stored in the `~/.emacs.d/snippets/`
and inside a folder with the same name as the mode for which the snippet is for. Once finished, simply press enter. 

If one does not desire to use the automated method of creating snippets, they can do so manually as long as
they follow the correct file format. All yasnippets start with the same header:

```elisp
# -*- mode: snippet -*-
# name: snippet_name
# key: some_key
# --

;; Here is where you write your snippet.

```

Once written, simply save the file in the propert location and tell yasnippet to reload all snippets.

#### Adding place holders to your snippets.

If a snippet contains a placeholder, then once the snippet is inserted into the file, the cursor will
automatically moved to the first placeholder, and the placeholder label will be highlighted. You can then
directly type in the replacement text for the placeholder label, and that text will overwrite the placeholder label.
To move to the next placeholder, simply use `Tab` and the cursor will jumpt to the next placeholder in the
order which the snippet was written.

Placeholders with labels can be added to your snippets by use of the format `${N:LABEL}`. Where `N` is the
number designating the order in which the labels should be replaced, and `LABEL` is the actually placeholder
label that will be replaced by the user. A basic example is provided below:

```elisp
# -*- mode: snippet -*-
# name: she_bang
# key: some_key
# --
#!/usr/bin/env ${1:Shell}
```

When you insert this snippet it the fifth hash mark will be read exactly as you intended it, and the cursor
will be moved automatically to the shell placeholder for you to designate your shell.

