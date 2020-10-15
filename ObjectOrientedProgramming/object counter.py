class ObjectCounter:
    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def display():
        print(ObjectCounter.numberOfObjects)


o1 = ObjectCounter()
o2 = ObjectCounter()
o3 = ObjectCounter()
o4 = ObjectCounter()

ObjectCounter.display()
o1.display()