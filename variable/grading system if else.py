math = int(input("Math Grade = "))
physics = int(input("Physics Grade = "))
chemistry = int(input("Chemistry Grade = "))

if math and physics and chemistry < 35:
    print("you have failed the exam")
else:
    average = (math + physics + chemistry)/3
    print(f" Average = {average}")
    if average <= 59:
        print("Your Grade is C")
    elif average <= 69:
        print("Your Grade is B")
    else:
        print("Your Grade is A")





