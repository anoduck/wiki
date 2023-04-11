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

### False positives on a cosmic scale.

Attempting to find the cause of the error was an incredibly tedious and time consuming process, and has continuously
resulted in false positives. Again and agina, just as I would mentally assume I finally found the cause of the error,
it would magically re-appear and reak havok on my emacs session. There was eveven a time spanning nearly a month, where
I thought I had finally seen the last of it, then after hooking an already loaded command to a editor mode, it came back.
The false positives are as follows:

1. The `indicate-empty-lines` farse.
   ```bash
   (set-default 'indicate-empty-lines t) #<--- Almost certain this one setting was the cause of the issue.
   (set-default 'imenu-auto-rescan t)
   ```
2. The prank of `resolve_face_name` in `xfaces.c`.
3. The charade of Org Agenda Files.
4. Centaurian Lies
5. In lou of a viable theme.

Each of the above false flags mentioned above took days to isolate and attempt to provide a solution two.
Overall the hunt for the elusive error has so far taken one month of breaking down and rebuilding my emacs init file piece by
piece.

### Make one move, lose out on your work.

After a month of possessing a functional emacs configuration, I enabled one setting, and that was to hook
org-recur-mode when org-mode loads. Then just like that I recieved an error stating too many files are open to
load org-recur. Once the setting to resolve this `max-lisp-eval-depth` was modified, it all began to crash
down all over again. The C stack overflow was back with a vengence, and now it does not seem to want to go
away.

#### Steps towards discovering the resultion.

1. Most certainly the approach of starting from scratch until the error is reproduced, is a better strategy
	 than removing code until the error stops.
2. Breaking the solitary init file down into several files also aided this process well. It allowed for
	 massive blocks of code to be excluded from loading with a single comment tick. Organizing these smaller
	 files by subject also helped to elemenate possible sources of the error.
3. In the end, using gdb was rather pointless, as it was elbow grease that allowed for the source of the error
	 to be discovered.

<!-- Why is nvim not allowing me to add an additional line? -->
