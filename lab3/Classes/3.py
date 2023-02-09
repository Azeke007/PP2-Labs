class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input())
width = int(input())
a = Shape()
b = Rectangle(length, width)
print(a.area())
print(b.area())
