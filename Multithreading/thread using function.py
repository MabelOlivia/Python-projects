from threading import *


def display_numbers():
    print(current_thread().getName())
    i = 0
    while i <= 10:
        print(i)
        i += 1


t = Thread(target=display_numbers())
t.start()
