import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getCircumference(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    circle = Circle(5)
    print("Area:", circle.getArea())
    print("Circumference:", circle.getCircumference())
