import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


    def __rmul__(self, factor):
        return Vec(self.x * factor, self.y * factor)
    
    def __mul__(self, factor):
        return self.__rmul__(factor)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

def dot(u, v):
    return u.x * v.x + u.y * v.y

class Particle:
    def __init__(self, m, p, v, r):
        self.mass = m
        self.position = p  
        self.velocity = v  
        self.radius = r
u=Vec(5,2)
v=Vec(1,1)