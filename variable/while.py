x = int(input("Enter min number: "))
y = int(input("Enter max number: "))
i = x
if i % 2 == 0:
    i += 1
while i <= y:
    print(i)
    i += 2

a = 0
while a < 20:
    a += 1
    if a % 3 == 0:
        continue
    print(a)

