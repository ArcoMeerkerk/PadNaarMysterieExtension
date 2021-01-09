import random

img1 = loadImage("../../assets/images/dice1.png")
img2 = loadImage("../../assets/images/dice2.png")
img3 = loadImage("../../assets/images/dice3.png")
img4 = loadImage("../../assets/images/dice4.png")
img5 = loadImage("../../assets/images/dice5.png")
img6 = loadImage("../../assets/images/dice6.png")

gedrukt = False
y = 0

def setup():
    size(800,600)

def draw():
    RollButtons()
    upperText()

def upperText():
    if gedrukt == False:
        fill(0)
        textSize(50)
        textAlign(CENTER)
        text('Click the dice', width/2, 175)

def rollRightDice(): 
    global img1, img2, img3, img4, img5, img6, false, gedrukt
    rolleddice = int(random.randint(1, 6))
    if gedrukt == False:
        if rolleddice == 1:
            background(255)
            imageMode(CENTER)
            image(img1, 401, 233, 227, 227)
        if rolleddice == 2:
            background(255)
            imageMode(CENTER)
            image(img2, 401, 233, 227, 227)
        if rolleddice == 3:
            background(255)
            imageMode(CENTER)
            image(img3, 401, 233, 227, 227)
        if rolleddice == 4:
            background(255)
            imageMode(CENTER)
            image(img4, 401, 233, 227, 227)
        if rolleddice == 5:
            background(255)
            imageMode(CENTER)
            image(img5, 401, 233, 227, 227)
        if rolleddice == 6:
            background(255)
            imageMode(CENTER)
            image(img6, 401, 233, 227, 227)
    if gedrukt == True:
        fill(255)
        rectMode(CORNER)
        rect(278, 472, 243, 64)
        textAlign(CENTER, CENTER)
        fill(0)
        textSize(20)
        text('Terug naar homescreen', 400, 498)
        if (mouseX > 278 and mouseX < (278 + 243) and mouseY > 472 and mouseY < (472 + 64)):      
            rolleddice = 0
            background(255)
            gedrukt = False              

def RollButtons():
    global img3, img6, gedrukt
    if gedrukt == False:
        fill(255)
        rectMode(CORNER)
        rect(330, 380, 143, 143)
        imageMode(CORNER)
        image(img6, 330, 380, 143, 143)

    if mousePressed:
        if (mouseX > 330 and mouseX < (330 + 143) and mouseY > 380 and mouseY < (380 + 143)):
            rollRightDice()
            gedrukt = True
    