weight= int(input("weight: "))
unit= input("(l)bs or (k)g :")
pound = 'l'
kg= 'k'

if unit.lower() == pound:
    convert = weight*0.45
    print(f"you are {convert}kgs")
elif unit.lower() == kg:
    convert = weight/0.45
    print(f"you are {convert}pounds")
