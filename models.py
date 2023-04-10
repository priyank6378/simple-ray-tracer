from utils import *

class Sphere:
    def __init__(self, r, center, color, specular_exponent=-1, reflective=0):
        self.r = r
        self.center = center
        self.s = specular_exponent
        self.color = color
        self.reflective = reflective

    def intersectionPoints(self, o, d):
        co = vector_ab(self.center,o)
        a = dot(d,d)
        b = 2*dot(co, d)
        c = dot(co,co) - (self.r)**2

        discriminant = b*b - 4*a*c
        if discriminant<0 or a == 0:
            return (INF ,INF)
        discriminant = (discriminant)**0.5
        t2 = (-b+discriminant)/(2*a)
        t1 = (-b-discriminant)/(2*a)

        return (t1, t2)
    

