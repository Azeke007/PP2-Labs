class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

length = int(input())
a = Shape()
b = Square(length)
print(a.area())
print(b.area())