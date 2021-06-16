"""
Program: Project1
Author: Cole Crase
This program is to let the user input the three sides of a triangle and it
would indicate whether or not the triangle is an equilateral triangle.
"""
print("Enter the length of each side of the triangle: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("It is an equilateral triangle")
elif x == y or z == y or z == x:
    print("It is not an equilateral triangle")
