import math
class Polar:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def add(self, radius1, angle1):
        print(f"({self.radius * math.cos(self.angle * math.pi/180) + radius1 * math.cos(angle1 * math.pi/180)} , {self.radius * math.sin(self.angle * math.pi / 180) + radius1 * math.sin(angle1 * math.pi/180)})")

    def __add__(self,other):
        radius = self.radius + other.radius
        angle = self.angle + other.angle
        print(f"{radius, angle}")
        self.x1 = self.radius * math.cos(self.angle * math.pi/180) 
        self.y1 = self.radius * math.sin(self.angle * math.pi/180) 
        self.x2 = other.radius * math.cos(other.angle * math.pi/180)
        self.y2 = other.radius * math.sin(other.angle * math.pi/180)
        return [self.x1, self.y1, self.x2, self.y2]

    def plane_add(self,other):
        ls = Polar.__add__(self,other)
        z1 = ls[0] + ls[2]
        z2 = ls[1] + ls[3]
        print(f"({z1}, {z2})")

        print(f"(radius = {(z1**2 + z2**2)**0.5}, angle = {math.atan(z2/z1)})")



    def __repr__(self):
        return f"Polar coordinates are (radius = {self.radius}, angle = {self.angle})."
    
polar1 = Polar(5, 0)
polar2 = Polar(5,90)
print(repr(polar1))
print(polar1.__add__(polar2))
polar1.plane_add(polar2)
