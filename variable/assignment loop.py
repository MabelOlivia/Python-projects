x = int(input("Enter a number: "))
a = 0
while a < 39 and a < x :
    a += 1
    if a % 10 == 0:
        a += 1
    print(a)
