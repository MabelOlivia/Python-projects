i = 1
while i <= 3:
    print('*' * i)
    i+= 1

secret_number= 9
guess_count=0

while guess_count < 3:
    guess_count += 1
    guess= int(input('Guess: '))
    if guess == secret_number:
        print('You won!')
        break
else:
    print("you've failed")

