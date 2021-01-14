gedrukt = False
rolleddice = 0
images = []

def Setup():
    global images

    images = [
        loadImage("./assets/images/dice/dice1.png"),
        loadImage("./assets/images/dice/dice2.png"),
        loadImage("./assets/images/dice/dice3.png"),
        loadImage("./assets/images/dice/dice4.png"),
        loadImage("./assets/images/dice/dice5.png"),
        loadImage("./assets/images/dice/dice6.png"),
    ]

def Show():
    RollButtons()   

def RollButtons(): 
    global rolleddice 
    imageMode(CORNER)
    image(images[rolleddice], 368, 530, 64, 64)

    if mousePressed:
        if (mouseX > 368 and mouseX < (368 + 54) and mouseY > 530 and mouseY < (530 + 64)):
            rolleddice = int(random(1, 6))