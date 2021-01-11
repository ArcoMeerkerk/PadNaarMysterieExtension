gedrukt = False
y = 0
images = []

def setup():
    global images
    
    size(800,600)

    images = [
        loadImage("./assets/images/dice1.png"),
        loadImage("./assets/images/dice2.png"),
        loadImage("./assets/images/dice3.png"),
        loadImage("./assets/images/dice4.png"),
        loadImage("./assets/images/dice5.png"),
        loadImage("./assets/images/dice6.png"),
    ]

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
    global images, false, gedrukt
    rolleddice = int(random(1, 6))
    if gedrukt == False:
        if rolleddice == 1:
            background(255)
            imageMode(CENTER)
            image(images[0], 401, 233, 227, 227)
        if rolleddice == 2:
            background(255)
            imageMode(CENTER)
            image(images[1], 401, 233, 227, 227)
        if rolleddice == 3:
            background(255)
            imageMode(CENTER)
            image(images[2], 401, 233, 227, 227)
        if rolleddice == 4:
            background(255)
            imageMode(CENTER)
            image(images[3], 401, 233, 227, 227)
        if rolleddice == 5:
            background(255)
            imageMode(CENTER)
            image(images[4], 401, 233, 227, 227)
        if rolleddice == 6:
            background(255)
            imageMode(CENTER)
            image(images[5], 401, 233, 227, 227)
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
    global images,gedrukt
    if gedrukt == False:
        fill(255)
        rectMode(CORNER)
        rect(330, 380, 143, 143)
        imageMode(CORNER)
        image(images[5], 330, 380, 143, 143)

    if mousePressed:
        if (mouseX > 330 and mouseX < (330 + 143) and mouseY > 380 and mouseY < (380 + 143)):
            rollRightDice()
            gedrukt = True
    