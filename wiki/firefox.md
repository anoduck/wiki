```text
#  _____ _           __
# |  ___(_)_ __ ___ / _| _____  __
# | |_  | | '__/ _ \ |_ / _ \ \/ /
# |  _| | | | |  __/  _| (_) >  <
# |_|   |_|_|  \___|_|  \___/_/\_\
#
```

## Firefox

Firefox is honestly, the lesser of two evils. The other evil being Chrome browser, where Internet Explorer is
not even a consideration worth having. 

What began humbly as Netscape, then realesed to the public as Mozilla, has become the most common browser
available to this day. It is renowned for its compromise between usability and security, and sincerely has
shaped the world we know as it is today.

### Tridactyl

Those in the know, know there is a secret method to configurating to where it's use is akin to gaining
enlightenment. This great secret is Tridactyl, and it is better than it has ever been. There is just one
problem, the keymappings are difficult to remember. So here is the cheatsheet tha twas unashamedly copied 
directly from Tridactyl's readme file. May you have good luck with it.



#### Default normal-mode bindings

This is a (non-exhaustive) list of the most common normal-mode bindings. Type `:help` to open the online help for more details.

-   `:` — activate the command line
-   `Shift` + `Insert` — enter "ignore mode". Press `Shift` + `Insert` again to return to "normal mode".
-   `ZZ` — close all tabs and windows, but only "save" them if your about:preferences are set to "show your tabs and windows from last time"
-   `.` — repeat the last command
-   `<C-v>` – send a single keystroke to the current website, bypassing bindings

You can try `:help key` to know more about `key`. If it is an existing binding, it will take you to the help section of the command that will be executed when pressing `key`. For example `:help .` will take you to the help section of the `repeat` command.

##### Navigating with the current page

-   `j`/`k` — scroll down/up
-   `h`/`l` — scroll left/right
-   `^`/`$` — scroll to left/right margin
-   `gg`/`G` — scroll to start/end of page
-   `f`/`F`/`gF` — enter "hint mode" to select a link to follow. `F` to open in a background tab (note: hint characters should be typed in lowercase). `gF` to repeatedly open links until you hit `<Escape>`.
-   `gi` — scroll to and focus the last-used input on the page
-   `r`/`R` — reload page or hard reload page
-   `yy` — copy the current page URL to the clipboard
-   `[[`/`]]` — navigate forward/backward though paginated pages, for example comics, multi-part articles, search result pages, etc.
-   `]c`/`[c` — increment/decrement the current URL by 1
-   `gu` — go to the parent of the current URL
-   `gU` — go to the root domain of the current URL
-   `gr` — open Firefox reader mode (note: Tridactyl will not work in this mode)
-   `zi`/`zo`/`zz` — zoom in/out/reset zoom
-   `<C-f>`/`<C-b>` — jump to the next/previous part of the page
-   `g?` — Apply Caesar cipher to page (run `g?` again to switch back)
-   `g!` — Jumble words on page

##### Find mode

Find mode is still incomplete and uses the Firefox feature "Quick Find". This will be improved eventually.

-   `/` — open the Quick Find search box
-   `/` then `<C-f>` — open the Find in page search box
-   `<C-g>`/`<C-G>` — find the next/previous instance of the last find operation (note: these are the standard Firefox shortcuts)

Please note that Tridactyl overrides Firefox's `<C-f>` search, replacing it with a binding to go to the next part of the page. 
If you want to be able to use `<C-f>` to search for things, use `<C-f>` after opening the Quick Find box (`/`), or any input field such as the address bar or search bar (use default browser shortcuts to activate these). To allow usage of `<C-f>` at any time, use `unbind <C-f>` to unset the scrollpage binding.

##### Bookmarks and quickmarks

-   `A` — bookmark the current page
-   `a` — bookmark the current page, but allow the URL to be modified first
-   `M<key>` — bind a quickmark to the given key
-   `go<key>`/`gn<key>`/`gw<key>` — open a given quickmark in current tab/new tab/new window

If you want to use Firefox's default `<C-b>` binding to open the bookmarks sidebar, make sure to run `unbind <C-b>` because Tridactyl replaces this setting with one to go to the previous part of the page.

##### Marks

-   `m a-zA-Z` — set a local mark (lowercase letter), or a global mark (uppercase letter)
-   `` ` a-zA-Z `` — jump to a local mark (lowercase letter), or a global mark (uppercase letter)
-   ``` `` ``` — jump to the location before the last mark jump

##### Navigating to new pages:

-   `o`/`O` — open a URL (or default search) in this tab (`O` to pre-load current URL)
-   `t`/`T` — open a URL (or default search) in a new tab (`T` to pre-load current URL)
-   `w`/`W` — open a URL (or default search) in a new window (`W` to pre-load current URL)
-   `p`/`P` — open the clipboard contents in the current/new tab
-   `s`/`S` — force a search using the default Tridactyl search engine, opening in the current/new tab. This is useful when searching for something that would otherwise be treated as a URL by `o` or `t`
-   `H`/`L` — go back/forward in the tab history
-   `gh`/`gH` — go to the pages you have set with `set home [url1] [url2] ...`

##### Handling tabs

-   `d` — close the current tab
-   `u` — undo the last tab/window closure
-   `gt`/`gT` — go to the next/previous tab
-   `g^ OR g0`/`g$` — go to the first/last tab
-   `ga` — go to the tab currently playing audio
-   `<C-^>` — go to the last active tab
-   `b` — bring up a list of open tabs in the current window; you can type the tab ID or part of the title or URL to choose a tab

##### Extended hint mode

Extended hint modes allow you to perform actions on page items:

-   `;i`/`;I` — open an image (in current/new tab)
-   `;s`/`;a` — save/save-as the linked resource
-   `;S`/`;A` — save/save-as the selected image
-   `;p` — copy an element's text to the clipboard
-   `;P` — copy an element's title/alt text to the clipboard
-   `;y` — copy an element's link URL to the clipboard
-   `;#` — copy an element's anchor URL to the clipboard
-   `;r` — read the element's text with text-to-speech
-   `;k` — delete an element from the page
-   `;;` — focus an element

Additionally, you can hint elements matching a custom CSS selector with `:hint -c [selector]` which is useful for site-specific versions of the standard `f` hint mode.
