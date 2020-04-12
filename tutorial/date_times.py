'''
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import datetime
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'datetime']
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> help(datetime.date)
Help on class date in module datetime:

class date(builtins.object)
 |  date(year, month, day) --> date object
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(...)
 |      Formats self with strftime.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
>>> jhumur.day
26
>>> dt = datetime.timedelta(100)
>>> print(jhumur + dt)
1985-06-06

# Day-name, Month-name Day-#, Year

>>> print(jhumur.strftime("%A, %B %d, %Y"))
Tuesday, February 26, 1985
>>> message = "Jhumur was born on {:%A, %B %d, %Y}."
>>> print(message.format(jhumur))
Jhumur was born on Tuesday, February 26, 1985.

>>> launch_time = datetime.time(22, 27, 0)
>>> launch_time.hour
>>> launch_time.minute
>>> launch_time.second
0
>>> now = datetime.datetime.today()
>>> print(now)
2020-03-04 19:58:41.680281
>>> now.microsecond
680281
>>> moon_landing = "7/22/1969"

>>> moon_landing_datetime = datetime.datetime.strptime(moon_landing,"%m/%d/%Y")

>>> print(moon_landing_datetime)
1969-07-22 00:00:00
'''