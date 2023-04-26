class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        self.a= round(3.14*self.r*self.r,2)
    def __str__(self):
        return str(self.a)
class Cylinder(Circle):
    def __init__(self,r,h):
        super().__init__(r)
        self.h=h
    def vol(self):
        super().area()
        self.v= self.a*self.h
    def __str__(self):
        return str(self.v)
class Cone(Cylinder):
    def __init__(self,r,h):
        super().__init__(r,h)
    def vol1(self):
        super().vol()
        self.v1= round(self.v/3,2)
    def __str__(self):
        return str(self.v1)

r=float(input('Enter r'))
h=float(input('Enter h'))
c=Cone(r,h)
p=Cylinder(r,h)
p.vol()
print(p)
c.vol1()
print(c)
        
