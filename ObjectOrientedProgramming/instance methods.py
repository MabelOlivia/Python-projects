class Product:
    def __init__(self):
        self.name = 'Samsung'
        self.description = "it's awesome"
        self.price = "30000/-"

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)


p1 = Product()
p1.display()

p2 = Product()
p2.display()