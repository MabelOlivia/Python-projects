x = 3
y = 24
i = x

print("Here are odd numbers between 3 and 24:")
if i % 2 == 0:
    i += 1
while i <= y:
    print(i)
    i += 2

print("Here are even numbers between 3 and 24:")
for num in range(x, y):
    if num % 2 == 0:
        print(num)

for num in range(x, y):
    if num % 2 != 0:
        print(num)





