try:
    x = int(input("Enter a number greater than 10: "))
    assert x > 10, "wrong number entered"
    print("You entered ", x)
except AssertionError:
    print("you've entered number less than 10")



