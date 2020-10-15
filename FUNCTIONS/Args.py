total = 7   # global variable


def multiply(*numbers):
    total = 1   # local variable
    for number in numbers:
        total = total * number
    return total


print(total)
print(multiply(2, 4, 1, 4))


# **args
# can be used to pass multiple keyword arguments and forms a dictionary
def save_user(**user):
    print(user)


save_user(ID=4398, Name="livy", age=75)


# default arguments
def sum(number, by=6):
    sum_ = number + by
    return sum_


print(sum(5, 9))