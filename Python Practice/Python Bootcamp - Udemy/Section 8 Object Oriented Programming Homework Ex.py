



"""Problem 1
Fill in the Line class methods to accept coordinates
as a pair of tuples and return the slope and distance of the line."""




class Line:

    def __init__(self,cor1,cor2):

        self.cor1 = cor1
        self.cor2 = cor2

    def Distance(self):
        print((((self.cor1[0]) - (self.cor2[0]))**2 +
               ((self.cor1[1]) - (self.cor2[1]))**2)**(1/2))

    def Gradient(self):
        print((self.cor2[1] - self.cor1[1])/
              (self.cor2[0] - self.cor1[0]))



coor = Line(cor1 = (1,1), cor2 = (5,8))

coor.Distance()
8.06225774829855

coor.Gradient()
1.75


coor2 = Line(cor1 = (2,2), cor2 = (10,10))


coor2.Distance()
11.313708498984761

coor2.Gradient()
1.0


####################################################################



"""Problem 2
Fill in the class
"""


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        print((self.pi*((self.radius)**2))*self.height)


    def surface_area(self):
        print((self.pi*((self.radius) ** 2))*2 + \
        ((2*self.pi*(self.radius))*self.height))


c = Cylinder(2,3)
c.volume()
56.52


c1 = Cylinder(6,2)

c1.volume()
75.36

c1.surface_area()
100.48

