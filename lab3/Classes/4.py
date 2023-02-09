import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self):
        dx = int(input())
        dy = int(input())
        self.x = dx
        self.y = dy
    def dist(self):
        print(math.sqrt(self.x*self.x+self.y*self.y))

x = int(input())
y = int(input())
p = Point(x, y)
p.show()
p.move()
p.show()
p.dist()