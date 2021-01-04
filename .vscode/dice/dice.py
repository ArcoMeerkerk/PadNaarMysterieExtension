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
    rolleddice = int(random(1, 6))
    if rolleddice == 1:
        fill(0)
        global img1
        img1 = loadImage("../../assets/images/dice1.png")
        imageMode(CENTER)
    if rolleddice == 2:
        fill(0)
        global img2
        img2 = loadImage("../../assets/images/dice2.png")
        imageMode(CENTER)
    if rolleddice == 3:
        fill(0)
        global img3
        img3 = loadImage("../../assets/images/dice3.png")
        imageMode(CENTER)
    if rolleddice == 4:
        fill(0)
        global img4
        img4 = loadImage("../../assets/images/dice4.png")
        imageMode(CENTER)
    if rolleddice == 5:
        fill(0)
        global img5
        img5 = loadImage("../../assets/images/dice5.png")
        imageMode(CENTER)
    if rolleddice == 6:
        fill(0)
        global img6
        img6 = loadImage("../../assets/images/dice6.png")
        imageMode(CENTER)

def rollLeftDice(): 
    rolleddice = int(random(1, 6))
    rolleddice1 = int(random(1, 6))
    if rolleddice == 1:
        fill(0)
        global img1
        img1 = loadImage("../../assets/images/dice1.png")
        imageMode(CENTER)
        image(img1, 250, 250, 150, 150)
    if rolleddice == 2:
        fill(0)
        global img2
        img2 = loadImage("../../assets/images/dice2.png")
        imageMode(CENTER)
        image(img2, 250, 250, 150, 150)
    if rolleddice == 3:
        fill(0)
        global img3
        img3 = loadImage("../../assets/images/dice3.png")
        imageMode(CENTER)
        image(img3, 250, 250, 150, 150)
    if rolleddice == 4:
        fill(0)
        global img4
        img4 = loadImage("../../assets/images/dice4.png")
        imageMode(CENTER)
        image(img4, 250, 250, 150, 150)
    if rolleddice == 5:
        fill(0)
        global img5
        img5 = loadImage("../../assets/images/dice5.png")
        imageMode(CENTER)
        image(img5, 250, 250, 150, 150)
    if rolleddice == 6:
        fill(0)
        global img6
        img6 = loadImage("../../assets/images/dice6.png")
        imageMode(CENTER)
        image(img6, 250, 250, 150, 150)
    if rolleddice1 == 1:
        fill(0)
        global img1
        img1 = loadImage("../../assets/images/dice1.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)
    if rolleddice1 == 2:
        fill(0)
        global img2
        img2 = loadImage("../../assets/images/dice2.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)
    if rolleddice1 == 3:
        fill(0)
        global img3
        img3 = loadImage("../../assets/images/dice3.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)
    if rolleddice1 == 4:
        fill(0)
        global img4
        img4 = loadImage("../../assets/images/dice4.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)
    if rolleddice1 == 5:
        fill(0)
        global img5
        img5 = loadImage("../../assets/images/dice5.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)
    if rolleddice1 == 6:
        fill(0)
        global img6
        img6 = loadImage("../../assets/images/dice6.png")
        imageMode(CENTER)
        image(img1, 450, 250, 150, 150)

def RollButtons():
    fill(255)
    rectMode(CORNER)
    rect(580, 450, 120, 120)
    global img6
    img6 = loadImage('../../assets/images/dice6.png')
    imageMode(CORNER)
    image(img6, 580, 450, 120, 120)

# Rightbutton
    fill(255)
    rectMode(CORNER)
    rect(100, 450, 120, 120)
    global img3
    img3 = loadImage('../../assets/images/dice3.png')
    imageMode(CORNER)
    image(img3, 100, 450, 120, 120)

    if mousePressed:
        if (mouseX > 100 and mouseX < (100 + 120) and mouseY > 450 and mouseY < (450 + 120)):
            rollRightDice()
            print(rolleddice)
        else:
            print('wrong')


# def MouseInSpace(x, y, w, h):
#     if (mouseX > x) and (mouseX < x+w) and (mouseY > y) and (MouseY < y+h):
#         return True
#     else:
#         return False

# def mousePressed():
#     if MouseInSpace(100, 450, 120, 120)
#         rollRightDice()
#     if MouseInSpace(100, 250, 120, 120)
#         rollLeftDice()
