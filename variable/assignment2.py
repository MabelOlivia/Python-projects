x = int(input("enter a number : "))
prime = True

for i in range(2, x-1):
    if x % i == 0:
        prime = False
if prime:
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")
