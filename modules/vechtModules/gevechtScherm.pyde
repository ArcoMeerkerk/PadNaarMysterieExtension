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
# scoreText1 = "Score: " + score1
# scoreText2 = "Score: " + score2
isErEenWinnaar = False
IsFirst = True
def setup():
    background(37)
    size(800, 600)
    frameRate(60)
    # achtergrond = loadImage("./assets/images/achtergrondElementen/vs_achtergrond.png")
    # spark = loadImage("./assets/images/achtergrondElementen/spark.gif")
    # plaatjes = list(
    # berserker = loadImage("./assets/images/karakters/BerserkerFullshot.png"),
    # fighter = loadImage("./assets/images/karakters/FighterFullshot.png"),
    # goblin = loadImage("./assets/images/karakters/GoblinFullshot.png"),
    # monk = loadImage("./assets/images/karakters/MonkFullshot.png"),
    # sorcerer = loadImage("./assets/images/karakters/SorcererFullshot.png"),
    # turtle = loadImage("./assets/images/karakters/TurtleFullshot.png")
    # )
    
def draw():
    gevechtScherm()
def gevechtScherm():
    global Data, isErEenWinnaar, score1, score2, IsFirst, sizeKarakter1, xKarakter1, yKarakter1, sizeKarakter1, xKarakter2, yKarakter2, sizeKarakter2
    # Reset wanneer de programma opnieuwe word gebruikt
    if IsFirst:
        IsFirst = False
        sizeKarakter1 = 0
        sizeKarakter2 = 0
        xKarakter1 = 0
        yKarakter1 = 0
        xKarakter2 = 0
        yKarakter2 = 0
        score1 = 0
        score2 = 0
        isErEenWinnaar = False
    # Kijkt welke plaatjes van de karakters op welke plek moet komen en hoe groot het moet zijn
    if isErEenWinnaar == False:
        # Speler1 = GekozenKarakters[0]
        # Speler2 = GekozenKarakters[1]
        # image(achtergrond, 0, 0)
        if score1 == 25 or score2 == 25:
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
        # imgageMode(CENTER)
        # image(plaatjes[Speler1], xKarakter1, yKarakter1, sizeKarakter1, sizeKarakter1)
        # image(plaatjes[Speler2], xKarakter2, yKarakter2, sizeKarakter2, sizeKarakter2)
        # Al het text dat op de scherm komt te staan
        textSize(32)
        textAlign(CENTER, CENTER)
        text("Klik zo snel mogelijk op\nhet knopje dat boven je karakter staat\n25 keer", 406, 76)
        textAlign(CORNER)
        textSize(48)
        text("Score: " + str(score1), 70, 172)
        text("Score: " + str(score2), 544, 172)
        text('Knop: Q', 73, 217)
        text('Knop: P', 547, 217)
        text('Speler 1', 68, 582) 
        text('Speler 2', 546, 582) 
    # Victory scherm
    if isErEenWinnaar == True:
        background(37)
        textAlign(CENTER)
        textSize(86)
        text('Victory', 400, 150)
        fill(255)
        if score1 >=25:
            textSize(55)
            text('Speler 1 heeft gewonnen', 402, 284)
        elif score2 >= 25:
            textSize(55)
            text('Speler 2 heeft gewonnen', 402, 284)
        fill('#808080')
        # Terug knop
        rectMode(CORNER)  
        rect(298, 419, 206, 55)
        fill(255)
        textSize(16)
        textAlign(CENTER)
        text("Terug naar Homescreen", 400, 448)
        if mousePressed:
            if (mouseX > 298 and mouseX < (298 + 206) and mouseY > 419 and mouseY < (419 + 55)):
                background(37)
                IsFirst = True
                isErEenWinnaar = False
# Detecteerd welke knoppen word in gedrukt en geeft een punt voor elke dat een knop wordt ingedrutk
def keyReleased():
    global score1, score2, isErEenWinnaar
    if isErEenWinnaar == False:
        if key == 'q' or key == 'Q':
            score1 += 1
            # image(spark, 218, 125, 50, 63)
            background(37)
        elif key == 'p' or key == 'P':
            score2 += 1
            # image(spark, 688, 125, 50, 63)
            background(37)

