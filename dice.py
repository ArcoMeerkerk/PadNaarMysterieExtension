import random


def setup():
    size(800,600)
    background(255)
    RollButtons()
    upperText()

def upperText():
    fill(0)
    textSize(50)
    textAlign(CENTER)
    text('Choose Left or Right dice', width/2, 175)
    textSize(25)
    text('The right one has 6 sides and the left one has 12 sides', width/2, 275)

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
    rolleddice = int(random(1, 7))
    rolleddice1 = int(random(1, 7))
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
    if rolleddice1 == 1:
        fill(0)
        global img1
        img1 = loadImage("dice1.png")
        imageMode(CENTER)
    if rolleddice1 == 2:
        fill(0)
        global img2
        img2 = loadImage("dice2.png")
        imageMode(CENTER)
    if rolleddice1 == 3:
        fill(0)
        global img3
        img3 = loadImage("dice3.png")
        imageMode(CENTER)
    if rolleddice1 == 4:
        fill(0)
        global img4
        img4 = loadImage("dice4.png")
        imageMode(CENTER)
    if rolleddice1 == 5:
        fill(0)
        global img5
        img5 = loadImage("dice5.png")
        imageMode(CENTER)
    if rolleddice1 == 6:
        fill(0)
        global img6
        img6 = loadImage("dice6.png")
        imageMode(CENTER)

def RollButtons():
    fill(255)
    rectMode(CORNER)
    rect(100, 500, 120, 120)
    global img6
    img6 = loadImage('../images/dice6.png')
    imageMode(CORNER)
    image(img6, 100, 500, 120, 120)

# Rightbutton
    fill(0)
    rectMode(CORNER)
    rect(600, 500, 120, 50)