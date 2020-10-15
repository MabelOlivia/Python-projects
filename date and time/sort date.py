from datetime import *
import time

starttime = time.perf_counter()
ldates = []

d1 = date(2017, 6, 21)
d2 = date(2017, 7, 21)
d3 = date(2017, 9, 21)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()
time.sleep(1)

for d in ldates:
    print(d)

endtime = time.perf_counter()
print("Execution time: ", endtime - starttime)
