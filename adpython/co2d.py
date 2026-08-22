import math

class coordinate2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __add__(self,other):
        if isinstance(other, coordinate2d):
            return coordinate2d(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self,other):
        if isinstance(other, coordinate2d):
            return coordinate2d(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int,float)):
            return coordinate2d(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, coordinate2d):
            val = ""
            if self.x == other.x and self.y == other.y:
                val = "true"
            else:
                val = "false"
            return val                                                
        return NotImplemented

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

print("enter your 2d coordinates x,y")
x = int(input("enter x coordinates:"))
y = int(input("enter y coordinates:"))
co1 = coordinate2d(x,y) 
print("select options to work with 2d coordinates")
print(" 1.To view your coordinates \n 2.To add your coordinates with another coordinates \n 3.To subract your coordinates with another coordinates \n 4.To multiply your coordinates with scalar units \n 5.To check if your coordinates are  equal with another coordinates \n 6.To see magnitude of your coordinates")
work = int(input(":"))
if work == 1:
    print(f"your coordinates are {co1}")
elif work == 2:
    print("enter your another coordinates")
    xx = int(input("enter x coordinate:"))
    yy = int(input("enter y coordinate:"))
    co2 = coordinate2d(xx,yy)
    co3 = co1 + co2
    print(f"coordinate 1 {co1} + coordinate 2 {co2} = {co3}")
elif work == 3:
    print("enter your another coordinates")
    xx = int(input("enter x coordinate:"))
    yy = int(input("enter y coordinate:"))
    co2 = coordinate2d(xx,yy)
    co3 = co1 - co2
    print(f"coordinate 1 {co1} - coordinate 2 {co2}  = {co3}")
elif work == 4:
    print("enter your scalar qunatity")
    scalar = int(input(":"))
    co3 = co1 * scalar
    print(f"coordinate 1 {co1} * {scalar} = {co3}")
elif work == 5:
    print("enter your another coordinates")
    xx = int(input("enter x coordinate:"))
    yy = int(input("enter y coordinate:"))
    co2 = coordinate2d(xx,yy)
    print(co1 == co2)
elif work == 6:
    print(abs(co1))
else:
    print("invalid input")




