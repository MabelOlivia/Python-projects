import datetime
import time

epochtime = time.time()
print(epochtime)

t = time.ctime()
print(t)

dt = datetime.datetime.today()
print(dt)
print(f'Current date is : {dt.day}/{dt.month}/{dt.year}')
print(f'Current time is : {dt.hour}:{dt.minute}:{dt.second}')
