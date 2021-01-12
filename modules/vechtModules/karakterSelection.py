GekozenKarakters = [0, 0]
i = 0
speler = 0
gekozen = False
# Color values voor de vierkanten waar de plaatjes zijn
color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]

rassen = ["Mens", "Goblin", "Tiefling", "Ketsudo", "Titaran"]
rasKarakter1 = ""
rasKarakter2 = ""
rollen = ["Monk", "Tovenaar", "Barbaar", "Vechter", "Schurk"]
rolKarakter1 = ""
rolKarakter2 = ""
IsFirst = True
Data = {}

def Show(bellFont):
    background(37)
    global GekozenKarakters, i, speler, gekozen, color, rasKarakter1, rasKarakter2, rolKarakter1, rolKarakter2, Data, IsFirst
    if IsFirst:
        IsFirst = False
        GekozenKarakters = [0, 0]
        i = speler = 0
        gekozen = False
        rasKarakter1 = rasKarakter2 = rolKarakter1 = rolKarakter2 = ""

    #De plaatjes waar de karakters op zitten
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 220, 88, 150, 150)
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 400, 88, 150, 150)
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 580, 88, 150, 150)
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 220, 259, 150, 150)
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 400, 259, 150, 150)
    imageMode(CENTER)
    image(Data["selectieAchtergrond"], 580, 259, 150, 150)
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
    image(Data["karakter1"], 220, 93, 120, 120)
    image(Data["karakter2"], 400, 93, 120, 120)
    image(Data["karakter3"], 580, 93, 120, 120)
    image(Data["karakter4"], 220, 264, 120, 120)
    image(Data["karakter5"], 400, 264, 120, 120)
    image(Data["karakter6"], 580, 264, 120, 120)
    # Karakters selecteren 
    if mousePressed:
        if (mouseX > 157.5 and mouseX < (157.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 1
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[0] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter1"]
                rasKarakter1 = rassen[4]
                rolKarakter1 = rollen[2]
            elif speler == 1:
                color[0] = "#00FF00"
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter1"]
                rasKarakter2 = rassen[4]
                rolKarakter2 = rollen[2]
        elif (mouseX > 337.5 and mouseX < (337.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 2
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[1] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter2"]
                rasKarakter1 = rassen[2]
                rolKarakter1 = rollen[3]
            elif speler == 1:
                color[1] = "#00FF00"
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter2"]
                rasKarakter2 = rassen[2]
                rolKarakter2 = rollen[3]
        elif (mouseX > 517.5 and mouseX < (517.5 + 125) and mouseY > 30.5 and mouseY < (30.5 + 125)):
            i = 3
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[2] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter3"]
                rasKarakter1 = rassen[1]
                rolKarakter1 = rollen[4]
            elif speler == 1:
                color[2] = "#00FF00"
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter3"]
                rasKarakter2 = rassen[1]
                rolKarakter2 = rollen[4]
        elif (mouseX > 157.5 and mouseX < (157.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i = 4
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[3] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter4"]
                rasKarakter1 = rassen[0]
                rolKarakter1 = rollen[0]
            elif speler == 1:
                color[3] = "#00FF00"
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter4"]
                rasKarakter2 = rassen[0]
                rolKarakter2 = rollen[0]
        elif (mouseX > 337.5 and mouseX < (337.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i =5
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[4] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter5"]
                rasKarakter1 = rassen[0]
                rolKarakter1 = rollen[1]
            elif speler == 1:
                color[4] = "#00FF00"    
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter5"]
                rasKarakter2 = rassen[0]
                rolKarakter2 = rollen[1]
        elif (mouseX > 517.5 and mouseX < (517.5 + 125) and mouseY > 201.5 and mouseY < (201.5 + 125)):
            i =6
            gekozen = True
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
            if speler == 0:
                color[5] = "#338DFF"
                Data["geselecteerdeKarakterSpeler1"] = Data["karakter6"]
                rasKarakter1 = rassen[3]
                rolKarakter1 = rollen[2]
            elif speler == 1:
                color[5] = "#00FF00"
                Data["geselecteerdeKarakterSpeler2"] = Data["karakter6"]
                rasKarakter2 = rassen[3]
                rolKarakter2 = rollen[2]
    # Speler info en Selectie
    textFont(bellFont)
    imageMode(CORNER)
    image(Data["houtenAchtergrond"], 52, 343, 335, 190)
    image(Data["houtenAchtergrond"], 412, 343, 335, 190)
    image(Data["karakterSpelerInfo"], 236, 343, 152, 190)
    image(Data["karakterSpelerInfo"], 595, 343, 152, 190)
    image(Data["geselecteerdeKarakterSpeler1"], 68, 360, 156, 156)
    image(Data["geselecteerdeKarakterSpeler2"], 425, 360, 156, 156)
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
    fill('#C69C6D')
    rectMode(CORNER)  
    rect(300, 548, 200, 35, 12)
    # Select knop
    fill(255)
    textSize(32)
    textAlign(CENTER)
    text("Select", 400, 576)
    if mousePressed:
        if (gekozen == True) and (mouseX > 300 and mouseX < (300 + 200) and mouseY > 548 and mouseY < (548 + 35)):
            GekozenKarakters[speler] = i
            print(GekozenKarakters)
            speler = 1
            color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"] 
    
    if GekozenKarakters[0] != 0 and GekozenKarakters[1] != 0 and speler == 1 \
        and GekozenKarakters[0] != GekozenKarakters[1] :
        IsFirst = True
        Data["geselecteerdeKarakterSpeler1"] = Data['vraagteken']
        Data["geselecteerdeKarakterSpeler2"] = Data['vraagteken']
        return False
    return True

def Setup():
    # Alle plaatjes
    global Data
    Data["karakter1"] = loadImage("./assets/images/karakters/Berserker-min.png")
    Data["karakter2"] = loadImage("./assets/images/karakters/Fighter-min.png")
    Data["karakter3"] = loadImage("./assets/images/karakters/Goblin-min.png")
    Data["karakter4"] = loadImage("./assets/images/karakters/Monk-min.png")
    Data["karakter5"] = loadImage("./assets/images/karakters/Sorcerer-min.png")
    Data["karakter6"] = loadImage("./assets/images/karakters/Turtle-min.png")
    Data["karakterSpelerInfo"] = loadImage("./assets/images/achtergrondElementen/karakterInfo.png")
    Data["selectieAchtergrond"] = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
    Data["houtenAchtergrond"] = loadImage("./assets/images/achtergrondElementen/houtenAchtergrond.jpg")
    Data["vraagteken"] = loadImage('/assets/images/achtergrondElementen/vraagteken.png')
    Data["geselecteerdeKarakterSpeler1"] = Data['vraagteken']
    Data["geselecteerdeKarakterSpeler2"] = Data['vraagteken']