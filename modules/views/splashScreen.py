BottomMargin = 61
ButtonHeight = 53
ButtonWidth = 199

def Show(font, buttonFont, bellFont) :
    textFont(font)
    fill('#C69C6D')
    textAlign(CENTER, CENTER)
    textSize(48)               
    text("PAD NAAR", width//2, 50)
    textSize(72)
    text("MYSTERIE", width//2, 113)
    fill(250)
    rectMode(CORNER)
    rect(33, 190, 734, 266, 13.5)
    textAlign(LEFT, TOP)
    textFont(bellFont)
    textSize(19)
    fill('#C69C6D')
    text(u"Dit is een uitbreiding op het spel: Pad Naar Mysterie.\nIn deze uitbreiding bevinden zich de volgende features:\n\
    \u2022    Evenementen: Eens in de zoveel tijd komt er een popup melding van een\n         event. Dit event moet vervolgens meteen uitgevoerd worden.\n\
    \u2022    Vecht knop: De twee spelers die het gevecht aan gaan kunnen hier zijn of\n         haar karakter selecteren. Nadat dit gebeurt is rolt er een dobbelsteen die\n\
         aantoont wie de winnaar is van het gevecht.\n\
    \u2022    Eind/Begin punten overzicht: Op het hoofdscherm zal er een overzicht zijn\n         van ieder eindpunt/beginpunt.\n\
    \u2022    Dobbelsteen rol: De spelers kunnen hiervan gebruik maken, in plaats van een\n         eigen dobbelsteen gebruiken.", 50, 203)
    return ShowStartButton(bellFont)

def ShowStartButton(buttonFont) :
    fill('#C69C6D')
    rectMode(CENTER)
    rect(width//2, height-BottomMargin, ButtonWidth, ButtonHeight, 12)
    textFont(buttonFont)
    fill(255)
    textAlign(CENTER, CENTER)
    textSize(36)
    text("Play", width//2, height-BottomMargin)

    if mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
        mouseY > height-BottomMargin - ButtonHeight//2 and mouseY < height-BottomMargin + ButtonHeight//2:
        return False
    else :
        return True