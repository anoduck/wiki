```text
#   ____   ____  _             _       ___                  __ _
#  / ___| / ___|| |_ __ _  ___| | __  / _ \__   _____ _ __ / _| | _____      __
# | |     \___ \| __/ _` |/ __| |/ / | | | \ \ / / _ \ '__| |_| |/ _ \ \ /\ / /
# | |___   ___) | || (_| | (__|   <  | |_| |\ V /  __/ |  |  _| | (_) \ V  V /
#  \____| |____/ \__\__,_|\___|_|\_\  \___/  \_/ \___|_|  |_| |_|\___/ \_/\_/
#
```

## The most evasive emacs error to resolve

For heaven's sake, I have been recieving the same error in Emacs now for almost two years. It's severity
variates between inexistence and completely locking up my session of Emacs. It has been a big problem, but the
source of this error has always evaded me. Over numerous days of troubleshooting, I have narrowed it down to
somthing that is occurring with Emacs completion system. It is also highly likely correlated with the
completion package company.

- [Debugging doc](https://github.com/emacs-mirror/emacs/blob/master/etc/DEBUG)

### Starting again

As suggested in the `emacs/DEBUG` file, I am not going to strip my init file down to it's bare core, and
slowly add pieces back in until I am able to recreate the error. This is opposite of, and a much better
approach, than removing parts of my init until the error disappears, which is what every one most often does.


### Enter GDB

__Finally!!!__ Some progress!

As previously mentioned, further reading let me to use gdb to debug my emacs session. After learned it would
be easier to run the gdb from the command line, and then run emacs from the gdb. I finally was able to catch a
segmentation fault. This segfault output the location of the memory where the error was occurring, AND the
function that is causing the error. Which is `resolve_face_name+19` The full section of debug output is as
follows:

```bash

0x00000b2d251dc5f7 <resolve_face_name+7>:       xor    (%rsp),%r11
0x00000b2d251dc5fb <resolve_face_name+11>:      push   %rbp
0x00000b2d251dc5fc <resolve_face_name+12>:      mov    %rsp,%rbp
0x00000b2d251dc5ff <resolve_face_name+15>:      push   %r11
0x00000b2d251dc601 <resolve_face_name+17>:      push   %r15
0x00000b2d251dc603 <resolve_face_name+19>:      push   %r14 # <--- The error occurred here.
0x00000b2d251dc605 <resolve_face_name+21>:      push   %r13
0x00000b2d251dc607 <resolve_face_name+23>:      push   %r12
0x00000b2d251dc609 <resolve_face_name+25>:      push   %rbx
0x00000b2d251dc60a <resolve_face_name+26>:      sub    $0x10,%rsp
0x00000b2d251dc60e <resolve_face_name+30>:      mov    %esi,%ebx
```

Further examining the stack and digging a little deeper, gave me:

```bash
#0  0x00000b2d251dc603 in resolve_face_name () from /usr/local/bin/emacs
(gdb) return 0
Make selected stack frame return now? (y or n) y
#0  0x00000b2d251dc427 in lface_from_face_name () from /usr/local/bin/emacs
(gdb) return
Make selected stack frame return now? (y or n) y
#0  0x00000b2d251de79e in Finternal_get_lisp_face_attribute () from /usr/local/bin/emacs
(gdb) return
Make selected stack frame return now? (y or n) y
#0  0x00000b2d252bf741 in Ffuncall () from /usr/local/bin/emacs
(gdb) return
Make selected stack frame return now? (y or n) y
#0  0x00000b2d2530add6 in exec_byte_code () from /usr/local/bin/emacs
```

A quick search with ag, told me where these functions came from, the `xfaces.c` file. Here is the output of ag
from searching for the original function that caused the error, and the function that called the original function.

```bash

# For resolve_face_name
xfaces.c
1941:resolve_face_name (Lisp_Object face_name, bool signal_p)
2015:  face_name = resolve_face_name (face_name, signal_p);
2059:  face_name = resolve_face_name (face_name, signal_p);
2977:  face = resolve_face_name (face, true);
3083:  face = resolve_face_name (face, true);

# For lface_from_face_name
xfaces.c
1987:lface_from_face_name_no_resolve (struct frame *f, Lisp_Object face_name,
2013:lface_from_face_name (struct frame *f, Lisp_Object face_name, bool signal_p)
2016:  return lface_from_face_name_no_resolve (f, face_name, signal_p);
2033:  lface = lface_from_face_name_no_resolve (f, face_name, signal_p);
2889:  global_lface = lface_from_face_name (NULL, face, false);
2895:      lface = lface_from_face_name (f, face, false);
2982:      lface = lface_from_face_name (XFRAME (frame), face, false);
2985:    lface = lface_from_face_name (NULL, face, false);
3013:      lface = lface_from_face_name (NULL, from, true);
3024:      lface = lface_from_face_name (XFRAME (frame), from, true);
3100:      lface = lface_from_face_name (NULL, face, true);
3119:      lface = lface_from_face_name (f, face, false);
3727:      lface = lface_from_face_name (f, face, true);
3743:      lface = lface_from_face_name (f, face, true);
3752:      lface = lface_from_face_name (f, face, true);
3759:      lface = lface_from_face_name (f, face, true);
3766:      lface = lface_from_face_name (f, face, true);
3937:      Lisp_Object lface = lface_from_face_name (f, Qmenu, true);
4079:  Lisp_Object lface = lface_from_face_name (f, symbol, true), value = Qnil;
4166:  global_lface = lface_from_face_name (NULL, face, true);
4167:  local_lface = lface_from_face_name (f, face, false);
4269:      Lisp_Object lface = lface_from_face_name (NULL, face, true);
4377:  lface1 = lface_from_face_name (f, face1, true);
4378:  lface2 = lface_from_face_name (f, face2, true);
4394:  Lisp_Object lface = lface_from_face_name (f, face, true);
5789:  lface = lface_from_face_name (f, Qdefault, false);
5910:  Lisp_Object lface = lface_from_face_name (f, symbol, false);
```

### Resolution discovered!

It was an incredibly tedious and time consuming process, but the two lines of code that were discovered to be
the pinnacle variable to whether the error occurred or not were:

```bash
(set-default 'indicate-empty-lines t) #<--- Almost certain this one setting was the cause of the issue.
(set-default 'imenu-auto-rescan t)
```

In fact, since imenu is never used, the `indicate-empty-lines` variable is the most probable cause to this
crippling error. Almost certain this variable can either be `nil` or a function defining the type of
indication. This means that `t` would be an uncomputable answer, and thus resulted in the segmentation fault.

#### Steps towards discovering the resultion.

1. Most certainly the approach of starting from scratch until the error is reproduced, is a better strategy
	 than removing code until the error stops.
2. Breaking the solitary init file down into several files also aided this process well. It allowed for
	 massive blocks of code to be excluded from loading with a single comment tick. Organizing these smaller
	 files by subject also helped to elemenate possible sources of the error.
3. In the end, using gdb was rather pointless, as it was elbow grease that allowed for the source of the error
	 to be discovered.

### Not so fast!

Again, it appeared as if a solution had been reached, and again once it was assumed the problem was over, it
rose again unexpectedly. Regardless, it appears most definitely the error emerging from the `xfaces.c` file,
specifically the `resolve_face_name` function. This is a big step, as it confirms previous suspicions over
this function, and aligns with previous data recieved from gdb.

### A small update.

After what appears to be two weeks I have struggled discovering the actual cause of the error. It seems that
everytime it seems to be resolved, it returns from the blue. Attempts at using GDB have been abandoned, and my
configuration files must have been rewritten once every two or three days.

#### Isolation to `org-agenda-files`

Now that my init file is spread out across seven different files, I finally isolated the error to my org
initialization file. This took longer than one would expect, because not in a thousand years would I have
suspected this file of containing any erros, and it was the last place I suspected to be problematic.
Furthermore, it was the last place I wanted to look, since it was so critical for me to keep org together and
running, but at last, I finally broke down and discovered it's betrayal. Then very slowly began to strip that
file until the error disappeared. Then I was able to isolate the error to a single configuration statement
that repeatedly reproduced the same error once added back into the init file. To my horror this setting was
`(setq org-agenda-files $FILES)`. This one setting is at the core of org functionality, and it meant that
until the error was resolved, org was broken.

#### Finally, building a minimal example for reproduction

Once the problematic variable was discovered, it was a matter of creating a init file that would reproduce the
error using the minimal amount of code, settings, and packages to reproduce it. By doing this alone, I
discovered the source of several other qwerks I have been concerned about.

##### The `void variable ("C-c t")`

Turns out this is related to centaur tabs, seeing how `C-c t` is centaur tab's prefix keymap. This conflicts
with custom designated keymaps, and requires change.

##### Potential cause

I just recieved the following error:
	`Corfu completion error: The connected server(s) does not support method textDocument/completion.`
This might be the potential cause of the `C-stack` error. Appeared once enabling loading my misc package
designation file.

##### Invalid-face attribute `:foreground nil`

This is a long time bug that has remained a part of my configuration. Because of the creation of a minimal
init file, I now have tracked this error to my misc package designation file, which was once suspected.

#### Appears I hit something

Just recieved the `Re-entering top level after C stack overflow` error. This was after I enably my
customization file loading. Once enabled, this file generated errors repeatedly.
