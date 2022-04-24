class Person:
    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname

    def printname(self):
        print(self.fname, self.sname)

class Student(Person):
    def __init__(self, fname, sname, year):
        super().__init__(fname, sname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.sname, "to the class of", self.graduationyear)

if __name__ == "__main__":
    O = Student("Valeeswaran", "Krishnamoorthy", 1998)
    O.welcome()
    O.printname()