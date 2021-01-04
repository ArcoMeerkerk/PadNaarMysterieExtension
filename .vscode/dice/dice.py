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
    background(255)
    RollButtons()
    upperText()

def upperText():
    if gedrukt == False:
        fill(0)
        textSize(50)
        textAlign(CENTER)
        text('Choose Right or Left dice', width/2, 175)
        textSize(25)
        text('The right one has 6 sides and the left one has 12 sides', width/2, 275)

def rollRightDice(): 
    global img1, img2, img3, img4, img5, img6, false, y
    rolleddice = int(random.randint(1, 6))
    if gedrukt == False:
        while y < 1:
            if rolleddice == 1:
                background(255)
                imageMode(CENTER)
                image(img1, 400, 250)
                y += 1
            if rolleddice == 2:
                background(255)
                imageMode(CENTER)
                image(img2, 400, 250)
                y += 1
            if rolleddice == 3:
                background(255)
                imageMode(CENTER)
                image(img3, 400, 250)
                y += 1
            if rolleddice == 4:
                background(255)
                imageMode(CENTER)
                image(img4, 400, 250)
                y += 1
            if rolleddice == 5:
                background(255)
                imageMode(CENTER)
                image(img5, 400, 250)
                y += 1
            if rolleddice == 6:
                background(255)
                imageMode(CENTER)
                image(img6, 400, 250)
                y += 1

def rollLeftDice():
    global img1, img2, img3, img4, img5, img6, y
    rolleddice = int(random.randint(1, 6))
    rolleddice1 = int(random.randint(1, 6))
    if gedrukt == False:
        while y < 1:
            if rolleddice == 1:
                background(255)
                imageMode(CENTER)
                image(img1, 250, 150, 100, 100)
                y += 1
            if rolleddice == 2:
                background(255)
                imageMode(CENTER)
                image(img2, 250, 150, 100, 100)
                y += 1
            if rolleddice == 3:
                background(255)
                imageMode(CENTER)
                image(img3, 250, 150, 100, 100)
                y += 1
            if rolleddice == 4:
                background(255)
                imageMode(CENTER)
                image(img4, 250, 150, 100, 100)
                y += 1
            if rolleddice == 5:
                background(255)
                imageMode(CENTER)
                image(img5, 250, 150, 100, 100)
                y += 1
            if rolleddice == 6:
                background(255)
                imageMode(CENTER)
                image(img6, 250, 150, 100, 100)
                y += 1
            if rolleddice1 == 1:
                background(255)
                imageMode(CENTER)
                image(img1, 450, 150, 100, 100)
                y += 1
            if rolleddice1 == 2:
                background(255)
                imageMode(CENTER)
                image(img2, 450, 150, 100, 100)
                y += 1
            if rolleddice1 == 3:
                background(255)
                imageMode(CENTER)
                image(img3, 450, 150, 100, 100)
                y += 1
            if rolleddice1 == 4:
                background(255)
                imageMode(CENTER)
                image(img4, 450, 150, 100, 100)
                y += 1
            if rolleddice1 == 5:
                background(255)
                imageMode(CENTER)
                image(img5, 450, 150, 100, 100)
                y += 1
            if rolleddice1 == 6:
                background(255)
                imageMode(CENTER)
                image(img6, 450, 150, 100, 100)
                y += 1

def RollButtons():
    global img3, img6, gedrukt
    if gedrukt == False:
        fill(255)
        rectMode(CORNER)
        rect(580, 450, 120, 120)
        imageMode(CORNER)
        image(img6, 580, 450, 120, 120)

# Left button
    if gedrukt == False:
        fill(255)
        rectMode(CORNER)
        rect(100, 450, 120, 120)
        imageMode(CORNER)
        image(img3, 100, 450, 120, 120)


    if mousePressed:
        if (mouseX > 100 and mouseX < (100 + 120) and mouseY > 450 and mouseY < (450 + 120)):
            rollLeftDice()
            gedrukt = True
        elif (mouseX > 580 and mouseX < (580 + 120) and mouseY > 450 and mouseY < (450 + 120)):
            rollRightDice()
            gedrukt = True

# def MouseInSpace(x, y, w, h):
#     if (mouseX > x) and (mouseX < x+w) and (mouseY > y) and (MouseY < y+h):
#         return True
#     else:
#         return False

# def mousePressed():
#     if MouseInSpace(100, 450, 250, 250)
#         rollRightDice()
#     if MouseInSpace(100, 250, 250, 250)
#         rollLeftDice()
