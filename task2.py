"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your script here

import random

jedinice = 0
dvojke = 0
trojke = 0
cetvorke = 0
petice = 0
sestice = 0

for i in range(1000):
    palo = random.randint(1,6)
    if palo == 1:
        jedinice +=1
    if palo == 2:
        dvojke +=1
    if palo ==3:
        trojke +=1
    if palo ==4:
        cetvorke +=1
    if palo ==5:
        petice +=1
    else:
        sestice +=1


print("Pala jedinica: " + str(jedinice))
print("Pala dvojka: " + str(dvojke))
print("Pala trojka: "+str(trojke))
print("Pala cetvorka: "+str(cetvorke))
print("Pala petica: "+str(petice))
print("Pala sestica: "+str(sestice))