class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def get_summ(self):
        return self.width + self.height

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())
print(r2.get_square())
r3 = Rectangle(4, 6)
r4 = Rectangle(6, 12)
print(r3.get_summ())
print(r4.get_summ())