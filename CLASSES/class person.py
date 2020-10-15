class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


mabel = Person("Mabel")
mabel.talk()

bob = Person("Bob")
bob.talk()
