```text
#   ____                _         ____
#  / ___|_ __ ___  __ _| |_ ___  |  _ \  __ _  ___ _ __ ___   ___  _ __  ___
# | |   | '__/ _ \/ _` | __/ _ \ | | | |/ _` |/ _ \ '_ ` _ \ / _ \| '_ \/ __|
# | |___| | |  __/ (_| | ||  __/ | |_| | (_| |  __/ | | | | | (_) | | | \__ \
#  \____|_|  \___|\__,_|\__\___| |____/ \__,_|\___|_| |_| |_|\___/|_| |_|___/
#
```

## Creating Daemons

There are three known ways to configure a task to run in the background; you can configure a shell script, use
the threading module, and use the multi-process module.

### Using the multi-process module

```python
def proc_daemonize():
    mp.set_start_method('spawn')
    the_daemon = mp.Process(target=start_process, args=(), name='daemon', daemon=True)
    daemon = False
    if daemon:
        log.info('Daemonizing & sending to background...')
        the_daemon.start()
        the_daemon.join()
    else:
        log.info('Running in foreground...')
        exit(0)
```

### Using the Threading Module

From [Super Fast Python](https://superfastpython.com/thread-long-running-background-task/)

```python
# SuperFastPython.com
# example of a long-running daemon thread
from time import sleep
from random import random
from threading import Thread
 
# long-running background task
def background_task():
    global data
    # record the last seen value
    last_seen = data
    # run forever
    while True:
        # check for change
        if data != last_seen:
            # report the change
            print(f'Monitor: data has changed to {data}')
            # update last seen
            last_seen = data
        # block for a while
        sleep(0.1)
 
# global data
data =  0
# create and start the daemon thread
print('Starting background task...')
daemon = Thread(target=background_task, daemon=True, name='Monitor')
daemon.start()
# main thread is carrying on...
print('Main thread is carrying on...')
for _ in range(5):
    # block for a while
    value = random() * 5
    sleep(value)
    # update the data variable
    data = value
print('Main thread done.')
```

### References

- [Getting Python Script to run in the background as a service.](https://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
- [Thread Long Running Background Task](https://superfastpython.com/thread-long-running-background-task/)

