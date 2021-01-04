import random

def Draw():
    size(800,600)
    background(255)

def rollRightDice(): 
    rolleddice = int(random(1, 7))
    if rolleddice == 1:
        fill(0)
        global img1
        img1 = loadImage("dice1.png")
        imageMode(CENTER)
    if rolleddice == 2:
        fill(0)
        global img2
        img2 = loadImage("dice2.png")
        imageMode(CENTER)
    if rolleddice == 3:
        fill(0)
        global img3
        img3 = loadImage("dice3.png")
        imageMode(CENTER)
    if rolleddice == 4:
        fill(0)
        global img4
        img4 = loadImage("dice4.png")
        imageMode(CENTER)
    if rolleddice == 5:
        fill(0)
        global img5
        img5 = loadImage("dice5.png")
        imageMode(CENTER)
    if rolleddice == 6:
        fill(0)
        global img6
        img6 = loadImage("dice6.png")
        imageMode(CENTER)

def rollLeftDice(): 
    rolleddice = int(random(1, 13))
    if rolleddice == 1:
        fill(0)
        global img1
        img1 = loadImage("dice1.png")
        imageMode(CENTER)
    if rolleddice == 2:
        fill(0)
        global img2
        img2 = loadImage("dice2.png")
        imageMode(CENTER)
    if rolleddice == 3:
        fill(0)
        global img3
        img3 = loadImage("dice3.png")
        imageMode(CENTER)
    if rolleddice == 4:
        fill(0)
        global img4
        img4 = loadImage("dice4.png")
        imageMode(CENTER)
    if rolleddice == 5:
        fill(0)
        global img5
        img5 = loadImage("dice5.png")
        imageMode(CENTER)
    if rolleddice == 6:
        fill(0)
        global img6
        img6 = loadImage("dice6.png")
        imageMode(CENTER)
    if rolleddice == 7:
        fill(0)
        global img1
        img1 = loadImage("dice7.png")
        imageMode(CENTER)
    if rolleddice == 8:
        fill(0)
        global img2
        img2 = loadImage("dice8.png")
        imageMode(CENTER)
    if rolleddice == 9:
        fill(0)
        global img3
        img3 = loadImage("dice9.png")
        imageMode(CENTER)
    if rolleddice == 10:
        fill(0)
        global img4
        img4 = loadImage("dice10.png")
        imageMode(CENTER)
    if rolleddice == 11:
        fill(0)
        global img5
        img5 = loadImage("dice11.png")
        imageMode(CENTER)
    if rolleddice == 12:
        fill(0)
        global img6
        img6 = loadImage("dice12.png")
        imageMode(CENTER)