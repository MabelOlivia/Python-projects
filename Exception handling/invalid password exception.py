class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    password = input("Enter password of 8 or more characters: ")

    if len(password) < 8:
        raise InvalidPasswordException("Password should have 8 or more characters")
except InvalidPasswordException as obj:
    print(obj)
else:
    print(f"Your password is : {password} ")
