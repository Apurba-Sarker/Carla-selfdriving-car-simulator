import math


class Point():
    def __init__(self, abscissa, ordinate):
        x = self.abscissa
        y = self.ordinate


class Parallelopiped():
    def __init__(self, top_left_abscissa, top_left_ordinate, side_1, side_2, Sangle):

        top_right_abscissa = self.top_left_abscissa + side_1
        top_right_ordinate = self.top_left_ordinate
        angle_rad = self.angle * (math.pi / 180)
        bottom_left_abscissa = top_left_abscissa + side_2 * math.cos(angle_rad)
        bottom_left_ordinate = top_left_ordinate - side_2 * math.sin(angle_rad)
        bottom_right_abscissa = bottom_left_abscissa + side_1
        bottom_right_ordinate = bottom_left_ordinate
        #top_right = Point()
        #bottom_left = Point()
        #bottom_right = Point()
        #top_right.x = top_right_abscissa
        #top_right.y = top_right_ordinate
        #bottom_left.x = bottom_left_abscissa
        #bottom_left.y = bottom_left_ordinate
        #bottom_right.x = bottom_right_abscissa
        #bottom_right.y = bottom_left_ordinate

    def __str__(self):
        print("The other vertices of the parallelepiped are:")
        print("("+ self.top_right.x + self.top_right.y, ")")
        print("("+ self.bottom_left.x + self.bottom_left.y, ")")
        print("("+ self.bottom_right.x + self.bottom_right.y, ")")

    def introduce(self):
        print("This is a parallelepiped:")
        print("Top left corner is " + " ( " + str(self.top_left_abscissa) +" , " + str(self.top_left_ordinate) + ")")
        print("The sides are " + str(self.side_1) + " and " + str(self.side_2))
        print("Angle is " + str(self.angle) + " degrees")


x1 = input()
y1 = input()
length1 = input()
length2 = input()
angle = input()

ABCD = Parallelopiped(x1, y1, length1, length2, angle)

ABCD.introduce()