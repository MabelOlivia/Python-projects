# open file for writing
f = open('myfile.txt', "w")
print("Enter text (press # when done): ")
s = " "

while s != "#":
    s = input()
    f.write(s)
f.close()
