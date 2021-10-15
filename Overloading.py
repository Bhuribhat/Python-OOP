import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self):        # same as __len__
        return math.sqrt(self.x**2 + self.y**2)

    # Overloading method
    def __add__(self, p):    # +
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):    # -
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):    # *
        return (self.x * p.x) + (self.y * p.y)
    
    def __len__(self):       # len()
        return math.sqrt(self.x**2 + self.y**2)

    # Comparison -> return boolean
    def __gt__(self, p):     # greater than >
        return self.length() > p.length()

    def __ge__(self, p):     # greater than and equal to >=
        return self.length() >= p.length()

    def __lt__(self, p):     # less than <
        return self.length() < p.length()

    def __le__(self, p):     # less than and equal to <=
        return self.length() <= p.length()

    def __eq__(self, other):     # equal to ==
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = p1 + p2
p4 = p2 - p1
p5 = p1 * p2
print(p3, p4, p5)
print(len(p1))
print(p1 == p2)
print(p1 < p1 + p2)