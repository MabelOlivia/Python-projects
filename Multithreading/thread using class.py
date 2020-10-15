from threading import *


class MyThread:

    def display_numbers(self):
        i = 0
        print(current_thread().getName())
        while i <= 10:
            print(i)
            i += 1


obj = MyThread()
t = Thread(target=obj.display_numbers())
t.start()

t2 = Thread(target=obj.display_numbers())
t2.start()

t3 = Thread(target=obj.display_numbers())
t3.start()
