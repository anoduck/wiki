```text
#   ____                           _
#  / ___| ___ _ __   ___ _ __ __ _| |
# | |  _ / _ \ '_ \ / _ \ '__/ _` | |
# | |_| |  __/ | | |  __/ | | (_| | |
#  \____|\___|_| |_|\___|_|  \__,_|_|
#
```

## General: Sane keymapping syntax

* [General](https://github.com/noctuid/general.el)

If you came to the page hoping to find a 'general overview' of emacs, then you are sadly mistaken. This entry
is for `general.el`, which is a package that allows the user to define his own keymapping in a manner that
should in theory, be easier to perform, but unfortunately is difficult to understand.

### Usage

From glancing over the documentation, implementing the package is much more involved then originally assumed.
Regardless, below is an example that exemplifies most of the basic functionality.

#### Syntax Example
```elisp

;; * Global Keybindings
;; `general-define-key' acts like `global-set-key' when :keymaps is not
;; specified (because ":keymaps 'global" is the default)
;; kbd is not necessary and arbitrary amount of key def pairs are allowed
(general-define-key
 "M-x" 'amx                             ; or 'smex
 "C-s" 'counsel-grep-or-swiper)

;; * Mode Keybindings
;; `general-define-key' is comparable to `define-key' when :keymaps is specified
(general-define-key
 ;; NOTE: keymaps specified with :keymaps must be quoted
 :keymaps 'org-mode-map
 "C-c C-q" 'counsel-org-tag
 ;; ...
 )
;; `general-def' can be used instead for `define-key'-like syntax
(general-def org-mode-map
  "C-c C-q" 'counsel-org-tag
  ;; ...
  )

;; * Prefix Keybindings
;; :prefix can be used to prevent redundant specification of prefix keys
(general-define-key
 :prefix "C-c"
 ;; bind "C-c a" to 'org-agenda
 "a" 'org-agenda
 "b" 'counsel-bookmark
 "c" 'org-capture)

;; for frequently used prefix keys, the user can create a custom definer with a
;; default :prefix
;; using a variable is not necessary, but it may be useful if you want to
;; experiment with different prefix keys and aren't using `general-create-definer'
(defconst my-leader "C-c")

(general-create-definer my-leader-def
  ;; :prefix my-leader
  ;; or without a variable
  :prefix "C-c")

;; ** Global Keybindings
(my-leader-def
  "a" 'org-agenda
  "b" 'counsel-bookmark
  "c" 'org-capture)

;; ** Mode Keybindings
(my-leader-def
  :keymaps 'clojure-mode-map
  ;; bind "C-c C-l"
  "C-l" 'cider-load-file
  "C-z" 'cider-switch-to-repl-buffer)
;; `general-create-definer' creates wrappers around `general-def', so
;; `define-key'-like syntax is also supported
(my-leader-def clojure-mode-map
  "C-l" 'cider-load-file
  "C-z" 'cider-switch-to-repl-buffer)

;; * Settings
;; change `auto-revert-interval' after autorevert has been loaded (`setq' will
;; not work)
(general-setq auto-revert-interval 10)

```

#### Package Integration

General.el integrates with many of the popular packages for Emacs. A few notable one's are:

* Which-Key
* Use-Package
