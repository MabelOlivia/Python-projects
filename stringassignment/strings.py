for name in ("Mabel"):
    print(name)

l = "refrigerator"
count = 0
for length in l:
    count += 1
print(count)

u = "umbrella"
print(u.find('e'))
print("e" in "umbrella")

msg = "This is orange juice"
print("orange" in msg)
print("orange" in msg.split())

msg1 = "hello, world"
print(msg1.find("o" ,0,-1))

nme = input(" you're name: ")
s = nme.split()
new = ' '
for i in range(len(1)-1):
    m = 1[i]
    new += (m[0].upper() + '.')
new += 1[-1].title()
return new