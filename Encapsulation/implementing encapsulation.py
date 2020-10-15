class Student:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

s = Student()
s.setName("Livy")
s.setId(97654)
print(s.getId())
print(s.getName())

