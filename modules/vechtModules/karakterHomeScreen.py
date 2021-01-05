GekozenKarakters = [0, 0]
i = 0
speler = 0
gekozen = False
# Color values voor de vierkanten waar de plaatjes zijn
color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
aantalKaraktersGekozen = 0    
karakter1 = loadImage("./assets/images/karakters/Berserker-min.png")
karakter2 = loadImage("./assets/images/karakters/Fighter-min.png")
karakter3 = loadImage("./assets/images/karakters/Goblin-min.png")
karakter4 = loadImage("./assets/images/karakters/Monk-min.png")
karakter5 = loadImage("./assets/images/karakters/Sorcerer-min.png")
karakter6 = loadImage("./assets/images/karakters/Turtle-min.png")
selectieAchtergrond = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
def SelectieScherm():
    global GekozenKarakters, i, speler, gekozen, color, aantalKaraktersGekozen, karakter1, karakter2, karakter3, karakter4, karakter5, karakter6
    #poep
    imageMode(CENTER)
    image(selectieAchtergrond, 200, 108, 170, 170)
    imageMode(CENTER)
    image(selectieAchtergrond, 400, 108, 170, 170)
    imageMode(CENTER)
    image(selectieAchtergrond, 600, 108, 170, 170)
    imageMode(CENTER)
    image(selectieAchtergrond, 200, 308, 170, 170)
    imageMode(CENTER)
    image(selectieAchtergrond, 400, 308, 170, 170)
    imageMode(CENTER)
    image(selectieAchtergrond, 600, 308, 170, 170)
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
    imageMode(CENTER)
    image(karakter1, 200, 113, 140, 140)
    imageMode(CENTER)
    image(karakter2, 400, 113, 140, 140)
    imageMode(CENTER)
    image(karakter3, 600, 113, 140, 140)
    imageMode(CENTER)
    image(karakter4, 200, 313, 140, 140)
    imageMode(CENTER)
    image(karakter5, 400, 313, 140, 140)
    imageMode(CENTER)
    image(karakter6, 600, 313, 140, 140)
    # Karakters selecteren 
    if mousePressed:
        if (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
            i = 1
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[0] = "#338DFF"
            elif speler == 1:
                color[0] = "#FF1B1B"
        elif (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
            i = 2
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[1] = "#338DFF"
            elif speler == 1:
                color[1] = "#FF1B1B"
        elif (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
            i = 3
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[2] = "#338DFF"
            elif speler == 1:
                color[2] = "#FF1B1B"
        elif (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
            i = 4
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[3] = "#338DFF"
            elif speler == 1:
                color[3] = "#FF1B1B"
        elif (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
            i =5
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[4] = "#338DFF"
            elif speler == 1:
                color[4] = "#FF1B1B"    
        elif (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
            i =6
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[5] = "#338DFF"
            elif speler == 1:
                color[5] = "#FF1B1B"
    # Achtergrond van select knop
    fill(255)
    rectMode(CORNER)  
    rect(300, 500, 200, 50)
    # Select knop
    fill(0)
    textSize(32)
    textAlign(CENTER)
    text("Select", 400, 540)
    if mousePressed:
        if (gekozen == True) and (mouseX > 300 and mouseX < (300 + 200) and mouseY > 500 and mouseY < (500 + 50)):
            background(35)
            print(i)
            GekozenKarakters[speler] = i
            print(GekozenKarakters)
            speler = 1  
    
    if GekozenKarakters[1] != GekozenKarakters[0] and speler == 1:
        background(35)
    