BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 150
AmountofPlayers = 0
Timer = 0

def Show(fonts) :
    textFont(fonts["MainFont"])
    fill(0)
    textAlign(CENTER)
    text("Selecteer spelers", width//2, 150)

    return ShowAmountButtons(fonts["ButtonFont"])

def ShowAmountButtons(buttonFont):
    global AmountofPlayers, Timer
    Timer += 1

    fill(0)
    rectMode(CENTER)
    rect(width//4, height-BottomMargin, ButtonWidth, ButtonHeight)
    textFont(buttonFont)
    fill(255)
    textSize(32)
    text("4 Spelers", width//4, height-BottomMargin+10)

    fill(0)
    rectMode(CENTER)
    rect(width//2, height-BottomMargin, ButtonWidth, ButtonHeight)
    textFont(buttonFont)
    fill(255)
    textSize(32)
    text("5 Spelers", width//2, height-BottomMargin+10)

    fill(0)
    rectMode(CENTER)
    rect(3*(width//4), height-BottomMargin, ButtonWidth, ButtonHeight)
    textFont(buttonFont)
    fill(255)
    textSize(32)
    text("6 Spelers", 3*(width//4), height-BottomMargin+10)

    if Timer > 30 :
        if mousePressed and mouseButton == LEFT and \
            mouseX > width//4 - ButtonWidth//2 and mouseX < width//4 + ButtonWidth//2 and \
            mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
            AmountofPlayers = 4
            return False
        elif mousePressed and mouseButton == LEFT and \
            mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
            mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
            AmountofPlayers = 5
            return False
        elif mousePressed and mouseButton == LEFT and \
            mouseX > 3*(width//4) - ButtonWidth//2 and mouseX < 3*(width//4) + ButtonWidth//2 and \
            mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
            AmountofPlayers = 6
            return False
        else :
            return True
    else :
        return True