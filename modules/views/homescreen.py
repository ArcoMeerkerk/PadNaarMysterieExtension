BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300
Timer = 0

def Show(font) :
    global Timer
    Timer += 1
    textFont(font)
    fill(0)
    textAlign(CENTER)               
    text("Homescreen", width//2, 150)

    # Rechthoek
    fill(255)
    rectMode(CENTER)
    rect(300, 500, 200, 50)
    # Vecht
    fill(0)
    textSize(32)
    textAlign(CENTER)
    text("VECHT", 400, 540)
    if mousePressed and Timer > 30:
        if (mouseX > 300 and mouseX < (300 + 200) and mouseY > 500 and mouseY < (500 + 50)):
            Timer = 0
            return False
    return True