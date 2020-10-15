x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number = int(input("Enter number: "))

for table in x:
    mult = table * number
    print(f'{number} x {table} = {mult}')