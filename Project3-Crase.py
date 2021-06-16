"""
Program: Project3
Author: Cole Crase
This program is a modified example of the guessing-game program where instead
of the user guessing what the number the computer is thinking, it is the
computer who have to guess what the number the user is thinking.
"""
import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint (smaller, larger)
count = 0

while True:
   count += 1
   print()
   print('%d %d' % (smaller, larger))
   print('Your number is:', myNumber)
   print()
   choice = input('Is this correct?: ')
   print()
   if choice == 'yes':
      print("Alright! I got it in", count, "attempts!")
      break
   else:
      myNumber = random.randint (smaller, larger)
   if count == 3:
      print("I give up, you are a cheater!")
      break
