name = input("What is your name? ")

if len(name) < 3:
    print('name must be at least 3 characters long')
elif len(name) > 50:
    print('name should be a maximum of 50 characters')
else:
    print('name looks good')
    print(name * 10)