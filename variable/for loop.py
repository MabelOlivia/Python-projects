item = (10, 20, 30)
total = 0
for prices in [10,20, 30]:
    total += prices
print(f' TOTAL: {total}')


for number in range(1,4):
    print("Attempt", number, number*".")

count = 0
for even in range(1, 10):
    if even % 2 == 0:
        count += 1
        print(even)

print(f"we have {count} even numbers")