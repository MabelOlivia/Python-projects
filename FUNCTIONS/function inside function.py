def greeting(name):
    def message():
        return "Hello "
    message = message() + name
    return message


print(greeting('Mabel'))