from threading import *


class MyThread(Thread):
    def run(self):
        print(current_thread().getName())
        i = 0
        while i <= 10:
            print(i)
            i += 1


print(current_thread().getName())
t = MyThread()
t.start()
