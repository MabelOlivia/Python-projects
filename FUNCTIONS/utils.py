def find_max():
    numbers = input()
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
