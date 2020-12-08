BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300

def Show(font) :
    textFont(font)
    fill(0)
    textAlign(CENTER)               
    text("Pad naar Mysterie", width//2, 150)
    
    return ShowStartButton()

def ShowStartButton() :
    fill(0)
    rectMode(CENTER)
    rect(width//2, height-BottomMargin, ButtonWidth, ButtonHeight)
    textFont(createFont("Arial", True))
    fill(255)
    textSize(32)
    text("Spel Starten!", width//2, height-BottomMargin+10)

    if mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        return False
    else :
        return True