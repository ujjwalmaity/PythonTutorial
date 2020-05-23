class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Points(x, y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


point1 = Points(1, 4)
point2 = Points(2, 8)
print(point1 + point2)
