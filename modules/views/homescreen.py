BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300

def Show(font, buttonFont) :
    textFont(font)
    fill(0)
    textAlign(CENTER)               
    text("Homescreen", width//2, 150)
    
    return ShowVechtButton(buttonFont)

def ShowVechtButton(buttonFont) :
    fill(0)
    rectMode(CENTER)
    rect(width//2, height-BottomMargin, ButtonWidth, ButtonHeight)
    textFont(buttonFont)
    fill(255)
    textSize(32)
    text("VECHT", width//2, height-BottomMargin+10)

    if mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        return False
    else :
        return True