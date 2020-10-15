customer = {
    "name" : "John Smith",
    "age" : 30,
    "phone number" : 12325
}


customer["name"] = "Jack Smith"
customer["birthdate"] = "12 sept 1997"
print(customer['name'])
print(customer['birthdate'])
print(customer.get('size'))
print(customer.get('size' , 865))

phone = input(" Phone: ")
digit_mapping = {
    '1' : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

output = ""

for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)


