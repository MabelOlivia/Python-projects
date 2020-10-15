for x in range(4):
    for y in range(3):
        print(f'{x} , {y}')


numbers = (5,2,5,2,2)

for pattern in numbers:
    print(pattern * "x")

number = (1,1,1,1,5)
for x_count in number:
     count = ''
     for output in range(x_count):
         count += 'X'
     print(count)