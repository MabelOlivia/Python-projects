from abc import abstractmethod, ABC


class TouchScreenLaptop:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def __init__(self, type, make, model):
        super().__init__(make, model)
        self.type = type

    def scroll(self):
        print("scrolls fast")

    @abstractmethod
    def click(self):
        pass


class DELL(TouchScreenLaptop):
    def __init__(self, kind, make, model):
        super().__init__(make, model)
        self.kind = kind

    def scroll(self):
        print("scrolls slow")

    @abstractmethod
    def click(self):
        pass


class HPNotebook(HP):
    def __init__(self, version, type, make, model):
        super().__init__(type, make, model)
        self.version = version

    def click(self):
        print("clicks twice")


class DELLNotebook(DELL):
    def __init__(self, quality, kind, make, model):
        super().__init__(kind, make, model)
        self.quality = quality

    def click(self):
        print("clicks once")


hp = HPNotebook("Elitebook", "8470p", "HP", "laptop")
print(hp.model)
print(hp.type)
hp.click()

print(" ")

dell = DELLNotebook("Best", "54830K", "make3", "DELL")
print(dell.kind)
print(dell.model)
dell.scroll()