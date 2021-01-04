import random

def Draw():
    size(800,600)
    background(255)
#Draw()
def Dice():

    uitkomst = ""
    rannum = random.randint(1,6)
    if rannum == 1:
        print("your number is 1")
    if rannum == 2:
        print("your number is 2")
    if rannum == 3:
        print("your number is 3")
    if rannum == 4:
        print("your number is 4")
    if rannum == 5:
        print("your number is 5")
    if rannum == 6:
        print("your number is 6")
        uitkomst = "Your number is" + str(rannum)

    else:
        uitkomst = 'have a nice day!'
    return(uitkomst)

print(Dice())