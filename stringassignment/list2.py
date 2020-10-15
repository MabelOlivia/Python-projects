number = [1, 3, 5, 6, 7]
matrix = [[0, 6], [1, 5]]
zeros = [0] * 5
combined = zeros + matrix
numbers = list(range(20))
chars = list("Hello, world")
print(matrix)
print(combined)
print(numbers)
print(f'{zeros}  {chars}')
print(chars)
print(number[::-1])

first, second, *others, last = number  # unpacking lists
print(first, last)
print(others)

for num in enumerate(number):
    print(num[0], num[1])