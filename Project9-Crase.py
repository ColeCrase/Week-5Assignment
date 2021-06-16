"""
Program: Project9
Author: Cole Crase
This program let the users receives a series of numbers and allows the user
to press the enter key to indicate that he or she is finished providing inputs.
The program should print the sum of the numbers and their average.
"""
theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    avg = theSum/number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)
print("The average is", avg)
