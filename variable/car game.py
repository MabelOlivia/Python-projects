started = False
while True:
    select = input('>').lower()
    if select == 'start':
        if started:
            print('Car already started!!')
        else:
            started = True
            print('car started... ready to go')
    elif select == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('car stopped')

    elif select == "help":
        print('''
start - to start the car
stop - to stop the car
quit-to exit''')
    elif select == 'quit':
        break
    else:
        print('I do not understand that')

