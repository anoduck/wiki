```text
#  ____       _                   _____
# |  _ \  ___| |__  _   _  __ _  | ____|_ __ ___   __ _  ___ ___
# | | | |/ _ \ '_ \| | | |/ _` | |  _| | '_ ` _ \ / _` |/ __/ __|
# | |_| |  __/ |_) | |_| | (_| | | |___| | | | | | (_| | (__\__ \
# |____/ \___|_.__/ \__,_|\__, | |_____|_| |_| |_|\__,_|\___|___/
#                         |___/
#
```

## Troubleshooting Emacs

For when shit goes pear shaped, you have this annoying as hell message that keeps popping up, or your Emacs
session locks up without any warning and leaves you high and dry without any indication where this lock up is
coming from.

```elisp
 (defadvice message (before who-said-that activate)
    "Find out who said that thing. and say so."
    (let ((trace nil) (n 1) (frame nil))
      (while (setq frame (backtrace-frame n))
        (setq n     (1+ n)
              trace (cons (cadr frame) trace)) )
      (ad-set-arg 0 (concat "<<%S>>:\n" (ad-get-arg 0)))
      (ad-set-args 1 (cons trace (ad-get-args 1))) ))

	  (defadvice message (before when-was-that activate)
    "Add timestamps to `message' output."
    (ad-set-arg 0 (concat (format-time-string "[%Y-%m-%d %T %Z] ")
                          (ad-get-arg 0)) ))
```

Later when you have finished discovering the mystical source of that annoying lock up, you can deactivate all
of this with:

```elisp
   (ad-disable-advice 'message 'before 'who-said-that)
   (ad-update 'message)

    (ad-disable-advice 'message 'before 'when-was-that)
    (ad-update 'message)
```

Best of luck.
