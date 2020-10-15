import os,sys


if os.path.isfile("myfile123.txt"):
    f = open("myfile123.txt", "r")
    print(f.read())
    f.close()
else:
    print("file does not exist")
    sys.exit()

