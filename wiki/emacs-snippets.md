```
#  _____ _ _
# | ____| (_)___ _ __
# |  _| | | / __| '_ \
# | |___| | \__ \ |_) |
# |_____|_|_|___/ .__/
#               |_|
#  ____        _                  _
# / ___| _ __ (_)_ __  _ __   ___| |_ ___
# \___ \| '_ \| | '_ \| '_ \ / _ \ __/ __|
#  ___) | | | | | |_) | |_) |  __/ |_\__ \
# |____/|_| |_|_| .__/| .__/ \___|\__|___/
#               |_|   |_|
#
```

## Elisp Snippets

I cannot promise there will be much activity or maintainance on this page, but for the time being, it will
house miscellaneous elisp statements for one's `init.el` file.

### Adding a timeout to a process

```elisp
(with-current-buffer (get-buffer-create "*my-proc-buffer*")
  (let ((proc (start-process "myproc" (current-buffer) "bash" "-c" "sleep 4"))) ;; start an async process
    (with-timeout (2 (kill-process proc)) ;; on timeout, kill the process
      (while (process-live-p proc) ;; while process is running
        (sit-for .05)) ;; let emacs read events and run timmers (and check for timeout)
      (message "finished on time!!")))) ;; this will run only if there is no timeout
```
