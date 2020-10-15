lst = [3, 7, 5, 4, 6]

filt = list(filter(lambda x: x % 2 == 0, lst))
print(filt)

for i in filt:
    print(i)

