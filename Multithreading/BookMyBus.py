from threading import *


class BookMyBus:

    def buy(self):
        print("confirming a seat")
        print("processing payment")
        print("printing a ticket")
        print("")


obj = BookMyBus()
t1 = Thread(target=obj.buy())
t2 = Thread(target=obj.buy())
t3 = Thread(target=obj.buy())

t1.start()
t2.start()
t3.start()
