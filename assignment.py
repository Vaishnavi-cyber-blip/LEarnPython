class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        print(area)

    def getCircumference(self):
        circum = 2 * 3.14 * self.radius
        print(circum)


game = Circle(5)
game.getArea()



