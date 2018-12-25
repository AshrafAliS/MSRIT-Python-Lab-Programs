#(b)	Write a python program to Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Create a variable named number_of_sides and set it equal to 3.Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.Print out my_triangle.number_of_sides and print out my_triangle.check_angles().
class Triangle():
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
x=int(input("Enter Angle 1\t"))
y=int(input("Enter Angle 2\t"))
z=int(input("Enter Angle 3\t"))
my_triangle = Triangle(x,y,z)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())
