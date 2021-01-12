ButtonYCord = 243
ButtonHeight = 58
ButtonWidth = 205
AmountofPlayers = 0
Timer = 0

def Show(font, buttonFont, bellFont):
    textFont(bellFont)
    fill(255)
    textAlign(CENTER, CENTER)
    textSize(72)
    text("Kies het aantal spelers", width//2, 113)
    return ShowAmountButtons(bellFont)

def ShowAmountButtons(bellFont):
    global AmountofPlayers, Timer
    Timer += 1

    fill('#C69C6D')
    rectMode(CENTER)
    rect(width//2, ButtonYCord, ButtonWidth, ButtonHeight, 12)
    textFont(bellFont)
    fill(255)
    textSize(32)
    text("4 Spelers", width//2, ButtonYCord)

    fill('#C69C6D')
    rectMode(CENTER)
    rect(width//2, ButtonYCord + 114, ButtonWidth, ButtonHeight, 12)
    textFont(bellFont)
    fill(255)
    textSize(32)
    text("5 Spelers", width//2, ButtonYCord + 114)

    fill('#C69C6D')
    rectMode(CENTER)
    rect(width//2, ButtonYCord + 227, ButtonWidth, ButtonHeight, 12)
    textFont(bellFont)
    fill(255)
    textSize(32)
    text("6 Spelers", width//2, ButtonYCord + 227)

    if Timer > 30 :
        if mousePressed and mouseButton == LEFT and \
            mouseX > width//2 - ButtonWidth//2 and mouseX < width//1 + ButtonWidth//2 and \
            mouseY > ButtonYCord - ButtonHeight//2 and mouseY < ButtonYCord + ButtonHeight//2:
            AmountofPlayers = 4
            return False
        elif mousePressed and mouseButton == LEFT and \
            mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
            mouseY > ButtonYCord + 114 - ButtonHeight//2 and mouseY < ButtonYCord + 114 + ButtonHeight//2:
            AmountofPlayers = 5
            return False
        elif mousePressed and mouseButton == LEFT and \
            mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
            mouseY > ButtonYCord + 227 - ButtonHeight//2 and mouseY < ButtonYCord + 227 + ButtonHeight//2:
            AmountofPlayers = 6
            return False
        else :
            return True
    else :
        return True