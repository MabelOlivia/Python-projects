secret_number = 9
count = 0

while count < 3:
    count += 1
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("you won")
        break
    else:
        print("Oops! Try again")
else:
    print("Game over!")
