numbers = [8, 7, 4, 3, 8, 7, 9]
print(numbers.count(9))
numbers.pop(2)
print(numbers)
numbers.append(10)
print(numbers)
numbers.insert(2, 9)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(50 in numbers)
print(numbers.count(8))
numbers2 = numbers.copy()
print(numbers2)
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
