
#  ____        _   _                   ____            _   _       _
# |  _ \ _   _| |_| |__   ___  _ __   |  _ \ __ _ _ __| |_(_) __ _| |
# | |_) | | | | __| '_ \ / _ \| '_ \  | |_) / _` | '__| __| |/ _` | |
# |  __/| |_| | |_| | | | (_) | | | | |  __/ (_| | |  | |_| | (_| | |
# |_|    \__, |\__|_| |_|\___/|_| |_| |_|   \__,_|_|   \__|_|\__,_|_|
#        |___/
#

Python Partial
--------------

The partial module can be found in the functools library which is a built-in library for the python language, and although it's first appearance 
may be intimidating it is really nothing to get excited about. All that the partial module does is allow
for the creation of a new function by setting a specific set of arguments for another function. Thus is how it
    earned it's name, because the new function is only a partial representation of the full function that is
    being processed. 

And now for a boring example using a real world example:

```python
from functools import partial
import pytz, datetime
os

# The first function which the partial will be based on.
def get_path(time, directory, file):
    tz = pytz.timezone("America/Los_Angeles")
    naive = datetime.datetime.strptime(time, "%Y-%m-%d_%H:%M:%S")
    real_time = tz.localize(naive, is_dst=None)
    file_dir = os.path.basename(os.path.abspath(file))
    filename = "new-file" + '-' + file_dir + '-' + str(real_time)
    file_path = os.path.join(directory, filename)

my_path = partial(get_path, some_time, some_directory)

print(my_path(some_file))
```
