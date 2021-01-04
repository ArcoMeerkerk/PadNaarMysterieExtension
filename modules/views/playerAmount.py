BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 150
amountofPlayers = 0


def Show(font) :
    textFont(font)
    fill(0)
    textAlign(CENTER)               
    text("Selecteer spelers", width//2, 150)
    
    return ShowAmountButtons()

def ShowAmountButtons() :
     global amountofPlayers
     fill(0)
     rectMode(CENTER)
     rect(width//4, height-BottomMargin, ButtonWidth, ButtonHeight)
     textFont(createFont("Arial", True))
     fill(255)
     textSize(32)
     text("4 Spelers", width//4, height-BottomMargin+10)

     fill(0)
     rectMode(CENTER)
     rect(width//2, height-BottomMargin, ButtonWidth, ButtonHeight)
     textFont(createFont("Arial", True))
     fill(255)
     textSize(32)
     text("5 Spelers", width//2, height-BottomMargin+10)

     fill(0)
     rectMode(CENTER)
     rect(3*(width//4), height-BottomMargin, ButtonWidth, ButtonHeight)
     textFont(createFont("Arial", True))
     fill(255)
     textSize(32)
     text("6 Spelers", 3*(width//4), height-BottomMargin+10)

     if mousePressed and mouseButton == LEFT and \
        mouseX > width//4 - ButtonWidth//2 and mouseX < width//4 + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        amountofPlayers = 4
        return False
     elif mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        amountofPlayers = 5
        return False
     elif mousePressed and mouseButton == LEFT and \
        mouseX > 3*(width//4) - ButtonWidth//2 and mouseX < 3*(width//4) + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        amountofPlayers = 6
        return False             
     else :
        return True