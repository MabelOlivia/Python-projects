import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two number: ").split()]
    c = a/b
    logging.info("division in progress")
    print(c)
    f.write(f"writing {c} into file")
except ZeroDivisionError:
    print("dividing by zero is not allowed")
    print("kindly input a nonzero value")
    logging.error("division by zero")
else:
    print("you have entered a non zero number")
finally:
    f.close()
    print("file closed")
print("proceed")
