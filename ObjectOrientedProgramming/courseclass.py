class Course:
    def __init__(self, n, r):
        self.name = n
        self.ratings = r

    def average(self):
        number_of_ratings = len(self.ratings)
        average = sum(self.ratings) / number_of_ratings
        print("Average Ratings of", self.name, "is", average)


c1 = Course("Assembly", [4, 4, 7, 9, 8])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Signals", [1, 2, 3, 4])
print(c2.name)
print(c2.ratings)
c2.average()
