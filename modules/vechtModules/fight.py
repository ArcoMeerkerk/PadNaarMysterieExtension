# from modules.vechtModules import karakter
sizeKarakter1 = 0
sizeKarakter2 = 0
xKarakter1 = 0
yKarakter1 = 0
xKarakter2 = 0
yKarakter2 = 0
score1 = 0
score2 = 0
gekozenKarakters = [6, 6]
isErEenWinnaar = False
scoreLimit = 25
victoryPlayer = 0
frameCounter1 = 0
frameCounter2 = 0
clicked1 = False
clicked2 = False
def Setup(gekozenKarakters):
    global plaatjes, achtergrond, spark, Speler1, Speler2
    Speler1 = gekozenKarakters[0]
    Speler2 = gekozenKarakters[1]
    achtergrond = loadImage("./assets/images/achtergrondElementen/vs_achtergrond.png")
    plaatjes = [
        loadImage("./assets/images/karakters/BerserkerFullshot.png"),
        loadImage("./assets/images/karakters/FighterFullshot.png"),
        loadImage("./assets/images/karakters/GoblinFullshot.png"),
        loadImage("./assets/images/karakters/MonkFullshot.png"),
        loadImage("./assets/images/karakters/SorcererFullshot.png"),
        loadImage("./assets/images/karakters/TurtleFullshot.png")
    ]
    spark = [
        loadImage('./assets/Gifs/Sparks/sparkFrame0.gif'),
        loadImage('./assets/Gifs/Sparks/sparkFrame1.gif'),
        loadImage('./assets/Gifs/Sparks/sparkFrame2.gif'),
        loadImage('./assets/Gifs/Sparks/sparkFrame3.gif'),
        loadImage('./assets/Gifs/Sparks/sparkFrame4.gif')
    ]

def Show(keyInfo):
    global Data, isErEenWinnaar, score1, score2, IsFirst, sizeKarakter1, xKarakter1, yKarakter1, \
    sizeKarakter1, xKarakter2, yKarakter2, sizeKarakter2, victoryPlayer, frameCounter1, frameCounter2 , clicked1, clicked2
    handleKeypress(keyInfo)
    # Kijkt welke plaatjes van de karakters op welke plek moet komen en hoe groot het moet zijn
    if isErEenWinnaar == False:
        imageMode(CORNER)
        image(achtergrond, 0, 0)
        if clicked1 == True:
            if frameCount % 5 == 0 and frameCounter1 < 4:
                frameCounter1 += 1
            if frameCounter1 == 4:
                frameCounter1 = 0
                clicked1 = False
            image(spark[frameCounter1], 200, 115, 82, 82)
        if clicked2 == True:
            if frameCount % 5 == 0 and frameCounter2 < 5:
                frameCounter2 += 1
            if frameCounter2 == 5:
                frameCounter2 = 0
                clicked2 = False
            image(spark[frameCounter2], 668, 115, 82, 82)
        if score1 == scoreLimit or score2 == scoreLimit:
            isErEenWinnaar = True
        if gekozenKarakters[0] == 1:
            sizeKarakter1 = 339
            xKarakter1 = 170
            yKarakter1 = 431
        if gekozenKarakters[1] == 1:
            sizeKarakter2 = 339
            xKarakter2 = 631
            yKarakter2 = 431
        if gekozenKarakters[0] == 2:
            sizeKarakter1 = 280
            xKarakter1 = 158
            yKarakter1 = 461
        if gekozenKarakters[1] == 2:
            sizeKarakter2 = 280
            xKarakter2 = 656
            yKarakter2 = 461
        if gekozenKarakters[0] == 3:
            sizeKarakter1 = 225
            xKarakter1 = 159
            yKarakter1 = 488
        if gekozenKarakters[1] == 3:
            sizeKarakter2 = 225
            xKarakter2 = 651
            yKarakter2 = 488
        if gekozenKarakters[0] == 4:
            sizeKarakter1 = 256
            xKarakter1 = 156
            yKarakter1 = 472
        if gekozenKarakters[1] == 4:
            sizeKarakter2 = 256
            xKarakter2 = 646
            yKarakter2 = 472
        if gekozenKarakters[0] == 5:
            sizeKarakter1 = 312
            xKarakter1 = 156
            yKarakter1 = 444
        if gekozenKarakters[1] == 5:
            sizeKarakter2 = 312
            xKarakter2 = 628
            yKarakter2 = 444
        if gekozenKarakters[0] == 6:
            sizeKarakter1 = 345
            xKarakter1 = 173
            yKarakter1 = 429
        if gekozenKarakters[1] == 6:
            sizeKarakter2 = 345
            xKarakter2 = 613
            yKarakter2 = 429
        # rectMode(CENTER)
        # rect(xKarakter1, yKarakter1, sizeKarakter1, sizeKarakter1)
        # rect(xKarakter2, yKarakter2, sizeKarakter2, sizeKarakter2)
        imageMode(CENTER)
        image(plaatjes[Speler1 - 1], xKarakter1, yKarakter1, sizeKarakter1, sizeKarakter1)
        image(plaatjes[Speler2 - 1], xKarakter2, yKarakter2, sizeKarakter2, sizeKarakter2)
        # Al het text dat op de scherm komt te staan
        textSize(32)
        textAlign(CENTER, CENTER)
        fill(255)
        text('Klik zo snel mogelijk op\nhet knopje dat boven je karakter staat\n' + str(scoreLimit) + ' keer', 406, 76)
        textAlign(CORNER)
        textSize(48)
        text("Score: " + str(score1), 70, 172)
        text("Score: " + str(score2), 544, 172)
        text('Knop: Q', 73, 217)
        text('Knop: P', 547, 217)
        text('Speler 1', 68, 582) 
        text('Speler 2', 546, 582)

        if isErEenWinnaar:
            victoryPlayer = 1 if score1 >= scoreLimit else 2
            print(victoryPlayer)
            IsFirst = False
            isErEenWinnaar = False
            sizeKarakter1 = 0
            sizeKarakter2 = 0
            yKarakter1 = 0
            xKarakter2 = 0
            yKarakter2 = 0
            score1 = 0
            score2 = 0
            return False
    return True

# Detecteerd welke knoppen word in gedrukt en geeft een punt voor elke dat een knop wordt ingedrutk
def handleKeypress(keyInfo):
    global score1, score2, isErEenWinnaar, frameCounter, clicked1, clicked2
    if isErEenWinnaar == False and keyInfo["KeyReleased"]:
        if key == 'q' or key == 'Q':
            score1 += 1
            background(37)
            clicked1 = True
        if key == 'p' or key == 'P':
            score2 += 1
            background(37)
            clicked2 = True

