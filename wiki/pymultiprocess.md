```text
#  __  __       _ _   _                                   _
# |  \/  |_   _| | |_(_)_ __  _ __ ___   ___ ___  ___ ___(_)_ __   __ _
# | |\/| | | | | | __| | '_ \| '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
# | |  | | |_| | | |_| | |_) | | | (_) | (_|  __/\__ \__ \ | | | | (_| |
# |_|  |_|\__,_|_|\__|_| .__/|_|  \___/ \___\___||___/___/_|_| |_|\__, |
#                      |_|                                        |___/
```

Python Multiprocessing
======================

The Python multiprocessing module allows one to create numerous different processes within their python
program. This is different than the subprocess module, which is for creating and managing processes that run
external applications.

## Working with multiprocesses

Starting a process uses the method `Process` to initialize a multiprocess instance. Then the function `start`
is used to run the instance. Below is an example.

```python
from multiprocessing import Process

# Define the task which will be ran by our process
def some_task(phrase, other_phrase):
    print(f'Printing the desired phrase: {phrase}')
    print(f'Now the other phrase: {other_phrase}')

# Create a process instance.
process = Process(target=some_task, args=(phrase='Hewo Worrrld!', other_phrase='For sure.'))

# Start our project.
process.start()
```

