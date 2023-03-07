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

Currently the eroor message recieved is:

```elisp

<<(timer-event-handler apply flycheck-display-error-at-point flycheck-display-errors
flycheck-display-error-messages display-message-or-buffer message apply ad-Advice-message)>>

<<(timer-event-handler apply #[0 "H\204^M^@    \205^]^@\302... [eldoc-mode global-eldoc-mode
eldoc--supported-p (debug-error) eldoc-print-current-symbol-info message "eldoc error: %s" 4]
eldoc-print-current-symbol-info..."])>>

```

None of the above were correct, but as a side note I am recieving the following error in vertical:
`(vertico--prepare) (void-function nil)`

got another: `timer-event-handler message. Which-key--update which-key-create-buffer-and-show`.

### Starting again

As suggested in the `emacs/DEBUG` file, I am not going to strip my init file down to it's bare core, and
slowly add pieces back in until I am able to recreate the error. This is opposite of, and a much better
approach, than removing parts of my init until the error disappears, which is what every one most often does.
