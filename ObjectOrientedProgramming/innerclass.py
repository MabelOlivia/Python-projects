class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine started")


c = Car("BMW", 2007)
e = c.Engine(8975)
e.start()