def message(fun):
    return "Hello " + fun


def name():
    return "Livy"


print(message(name()))


# returning functions
def message1():
    def greet():
        return "Hello"
    return greet()


result = message1()
print(result)
