GekozenKarakters = []
gekozen1 = gekozen2 = gekozen3 = gekozen4 = gekozen5 = gekozen6 = False
# Color values voor de vierkanten waar de plaatjes zijn
color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
# karakter1 = loadImage("./assets/images/karakters/Berserker-min.png")
# karakter2 = loadImage("./assets/images/karakters/Fighter-min.png")
# karakter3 = loadImage("./assets/images/karakters/Goblin-min.png")
# karakter4 = loadImage("./assets/images/karakters/Monk-min.png")
# karakter5 = loadImage("./assets/images/karakters/Sorcerer-min.png")
# karakter6 = loadImage("./assets/images/karakters/Turtle-min.png")
# selectieAchtergrond = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
AmountofPlayers = 5
aantalKaraktersGekozen = 0    
def setup():
    background(37)
    size(800, 600)
    frameRate(60)
def draw():
    SelectieScherm()
def SelectieScherm():
    global GekozenKarakters, color, aantalKaraktersGekozen, karakter1, karakter2, karakter3, \
    karakter4, karakter5, karakter6, gekozen1, gekozen2, gekozen3, gekozen4, gekozen5, gekozen6
    #Achtergrond voor de karakter selectie knoppen
    # imageMode(CENTER)
    # image(selectieAchtergrond, 200, 108, 170, 170)
    # imageMode(CENTER)
    # image(selectieAchtergrond, 400, 108, 170, 170)
    # imageMode(CENTER)
    # image(selectieAchtergrond, 600, 108, 170, 170)
    # imageMode(CENTER)
    # image(selectieAchtergrond, 200, 308, 170, 170)
    # imageMode(CENTER)
    # image(selectieAchtergrond, 400, 308, 170, 170)
    # imageMode(CENTER)
    # image(selectieAchtergrond, 600, 308, 170, 170)
    #De Vierkanten waar de karakters op zitten
    noStroke()
    rectMode(CENTER) 
    fill(color[0])
    rect(200, 113, 145, 145)
    fill(color[1])  
    rect(400, 113, 145, 145)
    fill(color[2])
    rect(600, 113, 145, 145)
    fill(color[3])
    rect(200, 313, 145, 145)  
    fill(color[4])  
    rect(400, 313, 145, 145)
    fill(color[5])
    rect(600, 313, 145, 145)
    # Plaatjes van de karakters
    # imageMode(CENTER)
    # image(karakter1, 200, 113, 140, 140)
    # imageMode(CENTER)
    # image(karakter2, 400, 113, 140, 140)
    # imageMode(CENTER)
    # image(karakter3, 600, 113, 140, 140)
    # imageMode(CENTER)
    # image(karakter4, 200, 313, 140, 140)
    # imageMode(CENTER)
    # image(karakter5, 400, 313, 140, 140)
    # imageMode(CENTER)
    # image(karakter6, 600, 313, 140, 140)
    # Karakters selecteren 
    if aantalKaraktersGekozen < AmountofPlayers:
        if mousePressed:
            if gekozen1 == False:
                if (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append(1)
                    color[0] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen1 = True
            if gekozen2 == False:
                if (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append(2)
                    color[1] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen2 = True
            if gekozen3 == False:
                if (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append(3)
                    color[2] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen3 = True
            if gekozen4 == False:
                if (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append(4)
                    color[3] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen4 = True
            if gekozen5 == False:
                if (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append(5)
                    color[4] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen5 = True
            if gekozen6 == False:
                if (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append(6)
                    color[5] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    gekozen6 = True
            print(GekozenKarakters)
    # Reset Knop vakje en text
    fill(255)   
    rectMode(CORNER)  
    rect(505, 505, 188, 42)
    fill(0)
    textSize(29)
    textAlign(CENTER, CENTER)
    text("Reset", 597, 525)
    # Uileg text
    textSize(32)
    fill(255)
    text("Kies " + str(AmountofPlayers) + " karakters", 398, 449)
    # Reset knop dat alle selecties reset
    if mousePressed:
        if (mouseX > 505 and mouseX < (505 + 188) and mouseY > 505 and mouseY < (505 + 42)):
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            gekozen1 = gekozen2 = gekozen3 = gekozen4 = gekozen5 = gekozen6 = False
            GekozenKarakters = []
            aantalKaraktersGekozen = 0
            background(37)
    #Accepteer knop
    if aantalKaraktersGekozen == AmountofPlayers:
        fill(255)   
        rectMode(CORNER)  
        rect(105, 505, 188, 42)
        fill(0)
        textSize(29)
        textAlign(CENTER, CENTER)
        text("Accepteer", 205, 525)
        if mousePressed:
            if (mouseX > 105 and mouseX < (105 + 188) and mouseY > 505 and mouseY < (505 + 42)):
                background(35)
                print(GekozenKarakters)
    