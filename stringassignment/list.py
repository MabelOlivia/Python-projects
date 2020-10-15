numbers = [1, 6 ,8 ,8, 9, 5]
print(numbers)
max = numbers[1]

for large in numbers:
    if large>max:
        max = large
print(max)