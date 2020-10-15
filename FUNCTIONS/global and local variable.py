x = 134  # global variable


def display():
    x = 2345    # local variable
    print(x)
    print(globals()['x'])


print(x)
z = display  # assigning functions to a variable
z()
