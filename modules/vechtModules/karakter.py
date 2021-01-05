GekozenKarakters = [0, 0]
i = 0
speler = 0
gekozen = False
# Color values voor de vierkanten waar de plaatjes zijn
color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
aantalKaraktersGekozen = 0   
# Alle plaatjes 
karakter1 = loadImage("./assets/images/karakters/Berserker-min.png")
karakter2 = loadImage("./assets/images/karakters/Fighter-min.png")
karakter3 = loadImage("./assets/images/karakters/Goblin-min.png")
karakter4 = loadImage("./assets/images/karakters/Monk-min.png")
karakter5 = loadImage("./assets/images/karakters/Sorcerer-min.png")
karakter6 = loadImage("./assets/images/karakters/Turtle-min.png")
karakterSpelerInfo = loadImage("./assets/images/achtergrondElementen/karakterInfo.png")
selectieAchtergrond = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
houtenAchtergrond = loadImage("./assets/images/achtergrondElementen/houtenAchtergrond.jpg")
geselecteerdeKarakterSpeler1 = loadImage('/assets/images/achtergrondElementen/vraagteken.png')
geselecteerdeKarakterSpeler2 = loadImage('/assets/images/achtergrondElementen/vraagteken.png')
rassen = ["Mens", "Goblin", "Tiefling", "Kestudo", "Titaran"]
rasKarakter1 = ""
rasKarakter2 = ""
rollen = ["Monk", "Tovenaar", "Barbaar", "Vechter", "Schurk"]
rolKarakter1 = ""
rolKarakter2 = ""
def SelectieScherm():
    global GekozenKarakters, i, speler, gekozen, color, aantalKaraktersGekozen, geselecteerdeKarakterSpeler1, geselecteerdeKarakterSpeler2, rasKarakter1, rasKarakter2, rolKarakter1, rolKarakter2
    #De plaatjes waar de karakters op zitten
    imageMode(CENTER)
    image(selectieAchtergrond, 220, 88, 150, 150)
    imageMode(CENTER)
    image(selectieAchtergrond, 400, 88, 150, 150)
    imageMode(CENTER)
    image(selectieAchtergrond, 580, 88, 150, 150)
    imageMode(CENTER)
    image(selectieAchtergrond, 220, 259, 150, 150)
    imageMode(CENTER)
    image(selectieAchtergrond, 400, 259, 150, 150)
    imageMode(CENTER)
    image(selectieAchtergrond, 580, 259, 150, 150)
    # De Selectie Border
    noStroke()
    rectMode(CENTER) 
    fill(color[0])
    rect(220, 93, 125, 125)
    fill(color[1])  
    rect(400, 93, 125, 125)
    fill(color[2])
    rect(580, 93, 125, 125)
    fill(color[3])
    rect(220, 264, 125, 125)  
    fill(color[4])  
    rect(400, 264, 125, 125)
    fill(color[5])
    rect(580, 264, 125, 125)
    # Plaatjes van de karakters
    imageMode(CENTER)
    image(karakter1, 220, 93, 120, 120)
    image(karakter2, 400, 93, 120, 120)
    image(karakter3, 580, 93, 120, 120)
    image(karakter4, 220, 264, 120, 120)
    image(karakter5, 400, 264, 120, 120)
    image(karakter6, 580, 264, 120, 120)
    # Karakters selecteren 
    if mousePressed:
        if (mouseX > 157.5 and mouseX < (157.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 1
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[0] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter1
                rasKarakter1 = rassen[4]
                rolKarakter1 = rollen[2]
            elif speler == 1:
                color[0] = "#00FF00"
                geselecteerdeKarakterSpeler2 = karakter1
                rasKarakter2 = rassen[4]
                rolKarakter2 = rollen[2]
        elif (mouseX > 337.5 and mouseX < (337.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 2
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[1] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter2
                rasKarakter1 = rassen[2]
                rolKarakter1 = rollen[3]
            elif speler == 1:
                color[1] = "#00FF00"
                geselecteerdeKarakterSpeler2 = karakter2
                rasKarakter2 = rassen[2]
                rolKarakter2 = rollen[3]
        elif (mouseX > 517.5 and mouseX < (517.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 3
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[2] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter3
                rasKarakter1 = rassen[1]
                rolKarakter1 = rollen[4]
            elif speler == 1:
                color[2] = "#00FF00"
                geselecteerdeKarakterSpeler2 = karakter3
                rasKarakter2 = rassen[1]
                rolKarakter2 = rollen[4]
        elif (mouseX > 157.5 and mouseX < (157.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i = 4
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[3] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter4
                rasKarakter1 = rassen[0]
                rolKarakter1 = rollen[0]
            elif speler == 1:
                color[3] = "#00FF00"
                geselecteerdeKarakterSpeler2 = karakter4
                rasKarakter2 = rassen[0]
                rolKarakter2 = rollen[0]
        elif (mouseX > 337.5 and mouseX < (337.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i =5
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[4] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter5
                rasKarakter1 = rassen[0]
                rolKarakter1 = rollen[1]
            elif speler == 1:
                color[4] = "#00FF00"    
                geselecteerdeKarakterSpeler2 = karakter5
                rasKarakter2 = rassen[0]
                rolKarakter2 = rollen[1]
        elif (mouseX > 517.5 and mouseX < (517.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i =6
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[5] = "#338DFF"
                geselecteerdeKarakterSpeler1 = karakter6
                rasKarakter1 = rassen[3]
                rolKarakter1 = rollen[2]
            elif speler == 1:
                color[5] = "#00FF00"
                geselecteerdeKarakterSpeler2 = karakter6
                rasKarakter2 = rassen[3]
                rolKarakter2 = rollen[2]
    # Speler info en Selectie
    imageMode(CORNER)
    image(houtenAchtergrond, 52, 343, 335, 190)
    image(houtenAchtergrond, 412, 343, 335, 190)
    image(karakterSpelerInfo, 236, 343, 152, 190)
    image(karakterSpelerInfo, 595, 343, 152, 190)
    image(geselecteerdeKarakterSpeler1, 68, 360, 156, 156)
    image(geselecteerdeKarakterSpeler2, 425, 360, 156, 156)
    fill(0)
    textSize(24)
    textAlign(CORNER)
    text("Speler 1", 263, 520)
    text("Speler 2", 625, 520)
    text(rasKarakter1, 255, 393)
    text(rolKarakter1, 255, 431)
    text(rasKarakter2, 614, 393)
    text(rolKarakter2, 614, 431)
    # Achtergrond van select knop  
    fill(255)
    rectMode(CORNER)  
    rect(300, 548, 200, 35)
    # Select knop
    fill(0)
    textSize(32)
    textAlign(CENTER)
    text("Select", 400, 576)
    if mousePressed:
        if (gekozen == True) and (mouseX > 300 and mouseX < (300 + 200) and mouseY > 548 and mouseY < (548 + 35)):
            background(35)
            print(i)
            GekozenKarakters[speler] = i
            print(GekozenKarakters)
            speler = 1
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"] 
    
    if GekozenKarakters[1] != GekozenKarakters[0] and speler == 1:
        background(35)
    