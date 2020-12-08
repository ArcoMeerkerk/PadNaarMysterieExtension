""" import random

numberList = [1,2,3,4,5,6]
print("dice number is: ", random.choice(numberList)

int(random.choice(numberList)) = n 
n = number
while n != 0:
    if n == 1:
        print("Number is 1")
        n -= 1
    if n == 2:
        print("Number is 2")
        n -= 2
    if n == 3:
        print("Number is 3")
        n -= 3
    if n == 4:
        print("Number is 4")
        n -= 4
    if n == 5:
        print("Number is 5")
        n -= 5
    if n == 6:
        print("Number is 6")
        n -= 6
    else:
        print("error") """
    
    

import random

while True:

   ans=input("do you want to roll the dice y/n ?").lower()

   if ans=="y": 

       dice1=random.randint(1,6)

       print("your nummber is",dice1)

        while dice1 != 0:
        
            """ if dice1 = 1:
                print("1")
                dice1 -= 1
            if dice1 = 2:
                print("2")
                dice1 -= 2
            if dice1 = 3:
                print("3")
                dice1 -= 3
            if dice1 = 4:
                print("4")
                dice1 -= 4
            if dice1 = 5:
                print("5")
                dice1 -= 5
            if dice1 = 6:
                print("6")
                dice1 -= 6
                hello
 """
   
   yelif ans=="n":

       print("okay, have a nice day")    