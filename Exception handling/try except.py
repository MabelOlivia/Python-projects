try:
    a, b = [int(x) for x in input("Enter two number: ").split()]
    c = a/b
    print(c)
except ZeroDivisionError:
    print("dividing by zero is not allowed")
    print("kindly input a nonzero value")
print("proceed")
