import pickle, student

f = open("student.dat", "wb")
s = student.Student(123, "Kev", 98)
pickle.dump(s, f)
f.close()