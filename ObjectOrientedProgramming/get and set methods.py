class Programmer:
    def setName(self, n):
        self.name = n

    def getName(self):
        return "Name: " + self.name

    def setSalary(self, sal):
        self.salary = sal
    def getSalary(self):
        return self.salary

    def setTechnologies(self, techs):
        self.technologies = techs
    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Mabel")
p1.setSalary(10000000)
p1.setTechnologies(["Python", "Machine learning", "Data Science"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

