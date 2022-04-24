from abc import ABC, abstractmethod


class Polygon(ABC):

    def __init__(self):
        self.a = 10
        self.b = 10

    @abstractmethod
    def noofsides(self):
        pass

    def noofsides_2(self):
        pass

class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")

    def noofsides_2(self):
        pass


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    def prints(self):
        pass


if __name__ == "__main__":
    # Driver code
    R = Triangle()
    R.noofsides()

    K = Quadrilateral()
    K.noofsides()

    R = Pentagon()
    R.noofsides()

    K = Hexagon()
    K.noofsides()