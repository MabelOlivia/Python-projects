def fizz_buz(input):
    if (input % 5 == 0) and (input % 3 ==0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "buzz"
    if input % 5 == 0:
        return "fizz"
    return input


print(fizz_buz(1))