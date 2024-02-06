```text
#  _       _ _         _
# (_)_ __ (_) |_   ___| |
# | | '_ \| | __| / _ \ |
# | | | | | | |_ |  __/ |
# |_|_| |_|_|\__(_)___|_|
#
```

## Welcome to the rest of your life.

One does not simply install Emacs. Creating an Emacs configuration file is a process that will take the rest
of your remaining life, and you still will have not completed it. Instead of set and done, think of it as a
process of continual maintenance.

Busey ipsum dolor sit amet. Go with the feeling of the nature. Take it easy. Know why you're here. And remember
to balance your internal energy with the environment.You ever roasted doughnuts?Have you urinated? Have you 
drained your bladder? Are you free? Because if you haven't it will only come out later. I'm giving you some
information that your bodily fluids may penetrate your clothing fibre's without warning.

You ever roasted doughnuts?It's good to yell at people and tell people that you're from Tennesee, so that way 
you'll be safe.I wrestled a bear once. A 750lbs black bear.Have you urinated? Have you drained your bladder?
Are you free? Because if you haven't it will only come out later. I'm giving you some information that your 
bodily fluids may penetrate your clothing fibre's without warning.

The best way to communicate is compatible. Compatible communication is listening with open ears and an open mind,
and not being fearful or judgemental about what you're hearing.Listen to the silence. And when the silence is 
deafening, you're in the center of your own universe.

### Good place to start

Below are two links from the emacswiki. Both include snippets or oneliners that are convenient, commonly
used, and encouraged to include in your init file.

* [DotEmacsChallenge](https://www.emacswiki.org/emacs/DotEmacsChallenge)
* [EmacsCrashCode](https://www.emacswiki.org/emacs/EmacsCrashCode)

### The most important snippet of code in your entire new life

Don't ask me where I found this, probably from the [emacswiki](https://emacswiki.org), but it's value cannot
be quantified by modern man, and it will save you days of painstaking labor. Add it to you init for instance
relief, and calmness will flow through your body.

```elisp
(setq
   backup-by-copying t      ; don't clobber symlinks
   backup-directory-alist
    '(("." . "~/.saves"))    ; don't litter my fs tree
   delete-old-versions t
   kept-new-versions 6
   kept-old-versions 2
   version-control t)
```

Now, you are ready to tackle the world being a better man because of it.

### Use-Package

Use-package is a package for emacs, that allows you to easily load and configure other packages for your Emacs session. For
lack of a better explanation, it is sort of like "nix config" for emacs, except not at all.

The documentation for it is fairly extensive, and best if left to the author to maintain. So, here is a direct
link to the readme. [Use-Package Readme](https://github.com/jwiegley/use-package/blob/master/README.md)

#### Most Commonly used Keywords.

| Keyword        | Definition                                                       | Load Time | example                              |
| -----------    | ----------------------------------------------------------       | ------    | -------                              |
| `:requires`    | Declares dependencies both required and optional.                | Before    | `:require org`                       |
| `:after`       | Ensures a package loads AFTER another package.                   | After     | `:after which-key`                   |
| `:defer`       | Defers loading of package a) until needed or b) after N seconds. | Lazy Load | `:defer t`                           |
| `:init`        | Declares code that needs execution before loading package.       | Before    | `:init (setq variable (definition))` |
| `:config`      | Defines package configuration options.                           | After     | `:config (setq variable thing)`      |
| `:custom`      | Declares custom variables for variables found within the package | After     | Rarely needed                        |
| ~`:bind`~      | ~Declares key binds for package.~                                |           | N/A                                  |
| `:general`     | We use `general.el` for keymap definitions.                      |           | <a href="#General">General</a>       |
| `:hook`        | Defines hooks for loading of package   *Implies Deferred*        | Lazy Load |                                      |
| `:mode`        | sets auto-mode-alist binding        *Implies Deferred*           | Lazy Load |                                      |
| `:interpreter` | sets interpreter-mode-alist binding   *Implies Deferred*         | Lazy Load |                                      |
| `:command`     | Triggers the loading of a package when used.  *Implies Deferred* | Lazy Load |                                      |
| `:magic`       | lower priority file association  *Implies Deferred*              | Lazy Load |                                      |
| `:ensure`      | Ensures that package is loaded.                                  | During    |                                      |
| `:if`          | Conditional loading keyword.                                     | Lazy Load |                                      |

##### Examples

###### General

General uses two methods for setting keymaps. 
1. Global
2. Per Mode

```elisp
;; Global
:general
("C-x f" 'find-file)

;; Keymap by mode
:general
(:keymap org-mode-map
  ("C-c a" org-agenda))
```


##### syntactical format

In the following example, `$package` will be used to represent a desired package.

```elisp
(use-package $package
   :requires $another-package
	 :defer t
	 )
```

### Giving Emacs a boost

After reading an article on [emacswiki](https://emacswiki.com) I learned it is recommended to bump your
single file memory limit to 1GB. Therefore, I added.

```elisp
(setq most-positive-fixnum 1073741824)
```
