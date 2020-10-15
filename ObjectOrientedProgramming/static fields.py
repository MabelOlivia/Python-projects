class Student:
    major = "CSE"   # static field

    def __init__(self, regno, name):
        self.regno = regno
        self.name = name


s1 = Student(2345, "Mabel")
print(s1.major)
print(Student.major)
