from functools import reduce

lst = [6, 9, 3, 3]
result = reduce(lambda x, y: x * y, lst)
print(result)