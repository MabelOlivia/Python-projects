from datetime import *

d = date(2020, 10, 1)
t = time(6, 4)

dt = datetime.combine(d, t)
print(dt)
