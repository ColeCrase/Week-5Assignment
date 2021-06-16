"""
Program: Project2
Author: Cole Crase
This program is to let the user input the three sides of a triangle and it
would indicate whether or not the triangle is a right triangle.
"""
print("Enter the length of each side of the triangle: ")
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if z > x and z > y:
    print("It is a right triangle")
else:
    print("It is not a right triangle")

