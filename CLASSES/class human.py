class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "actor":
            print(self.name, " makes amazing movies")
        elif self.occupation == "Data Scientist":
            print(self.name, " is a Lead Data Scientist")

    def speaks(self):
        print(self.name, " is happy to meet you. \n ")


mabel = Human("Mabel", "Data Scientist")
mabel.do_work()
mabel.speaks()

jenny = Human("Jennifer", "actor")
jenny.do_work()
jenny.speaks()
