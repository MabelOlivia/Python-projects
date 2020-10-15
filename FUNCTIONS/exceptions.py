try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("division by zero is not allowed")




