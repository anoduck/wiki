```text
  ___             __  __         _
 / _ \ _ _ __ _  |  \/  |___  __| |___
| (_) | '_/ _` | | |\/| / _ \/ _` / -_)
 \___/|_| \__, | |_|  |_\___/\__,_\___|
          |___/
```

## What is org mode?

    I’m sure I’ll be tweaking it forever though, it’s almost as satisfying as actually using it.
    ~8ninjani8 on /r/emacs.

    I honestly don’t know how I ever lived without org-mode
    ~Luke Gaudreau on Twitter.

    I’m having the same feeling for org-mode that I did when I first learned to really program and use emacs.
    ~Jeffery Travis on Twitter.

    Org-mode is one of those tools that change the way you work and think forever.
    ~Kaluza Twitter


### Org Mode

It was only a matter of time until this wiki ventured into the realm of org. Org Mode is something that is unlike anything else, and is
truly unique to the EMACS text editor. It begin it's existence primarily focused on lists of tasks, but has now expanded to anything
that can be derived from a list. It has taken over a decade of development, and is still being expanded into further forms of
application.

In a nut-shell, Org Mode is basically an outline of items, where items are referred to as nodes. Where each node falls in the outline
effects the prioritization and/or chronology of the node. Nodes also have properties that further describe them and are reflected upon
them, changing how they are handled and treated. Nodes also possess attributes, that are particularly catered towards task managment.
If this sounds complex and confusing, perhaps the best thing is to just look at a normal Org Mode file, and you will see there is not
much to it at all.

```org
#+TITLE: Example Task File
#+CATEGORY: Examples
# -------------------
* Depending on your preference, any heading on any level can be used as a heading or category indicator.
* Tasks
** TODO Example task

```

### Why you should not be like me

A long rambling paragraph was planned for this section, but instead just a few simple words of advice. Yeah,
org comes with a whole shit load of really cool addon or "extra" packages that enable additional
functionality, but avoid the temptation to install a bunch of packages you may only use maybe once or twice a
month. Stick with the basics, and it will make org flow more smoothly.

#### Links

* [Sync Org with Unison](https://orgmode.org/worg/org-tutorials/unison-sync.html)
* [Docs for Org Commands, Hooks, and Options](https://orgmode.org/worg/doc.html)
* [Org Mode Hacks](https://orgmode.org/worg/org-hacks.html)

### Org-Export

#### Disable converting nodes to headers, keep outline layout.

This particular configuration came from posting a question on reddit's `/r/orgmode`. Add the following to the
top of your org file, at the bottom of your org file header.

```org
#+OPTIONS: H:0 num:nil toc:nil \n:nil @:t ::t |:t ^:t -:t f:t *:t
#+latex_header: \renewcommand{\labelitemi}{•}
#+latex_header: \renewcommand{\labelitemii}{•}
#+latex_header: \renewcommand{\labelitemiii}{•}
#+latex_header: \renewcommand{\labelitemiv}{•}
```
