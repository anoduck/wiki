## Working with datetime and time.time in python


### Converting time.time to datetime

```python
"""x = datetime_obj"""
time_obj = time.mktime(x.timetuple()) + x.microsecond / 1E6
```

### Working with time objects and `timedelta()`


(AND then for some reason prose does not want me to paste entries.)

#### Getting setup for work

```python
import re
import time
from datetime import date, datetime, timedelta

from scheduler import Scheduler

today = datetime.today()
schedule = Scheduler()
format = '%m/%d/%Y %I:%M %p'
```

#### The Code

```python
# Lets turn this lovely forumula into a function now
def convert_to_timetime(dt):
    time_obj = time.mktime(dt.timetuple()) + dt.microsecond / 1E6
    return time_obj
```


```python
#Acquire the current time as time.time obj
current_time = time.localtime(time.time())
```


```python
import re
# acquire a datetime obj from a time.time obj
def get_dt_now(datetime_obj):
    date_num = re.findall(r'\d+', str(datetime_obj))
    dti = list(map(int, date_num))
    yr = dti[0]
    mnt = dti[1]
    day = dti[2]
    hr = dti[3]
    mnu = dti[4]
    if dti[5]:
        sec = dti[5]
    else:
        sec = 0
    return datetime(yr, mnt, day, hr, mnu, sec)
```


```python
def get_atime(dt):
    sec = 0
    minute = int(dt.minute) + 3
    year = dt.year
    month = dt.month
    day = dt.day
    hour = int(dt.hour) + 1
    return datetime(year, month, day, hour, minute, sec)
```


```python
#Acquire a date time obj for now
datetime_now = get_dt_now(current_time)

# Now get a time in the future in datetime obj form
future_time = get_atime(datetime_now)

"""
    Now convert both from a datetime obj to a time obj
"""
time_now = convert_to_timetime(datetime_now)
new_future = convert_to_timetime(future_time)

"""
    Now lets acquire the difference and reflect it to a timedelta obj
"""
difference = int(new_future) - int(time_now)
print('Seconds: ' + difference)
```
