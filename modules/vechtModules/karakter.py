GekozenKarakters = [0, 0]
i = 0
speler = 0
gekozen = False
# Color values voor de vierkanten waar de plaatjes zijn
color = [123, 123, 123, 123, 123, 123]
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
    #De Vierkanten waar de karakters op zitten
    rectMode(CENTER) 
    fill(color[0])
    rect(196, 135, 180, 180)
    fill(color[1])
    rect(401, 135, 180, 180)
    fill(color[2])
    rect(606, 135, 180, 180)
    fill(color[3])
    rect(196, 343, 180, 180)  
    fill(color[4])
    rect(400, 343, 180, 180)
    fill(color[5])
    rect(606, 343, 180, 180)
    # Plaatjes van de karakters
    imageMode(CENTER)
    image(karakter1, 196, 135, 170, 170)
    imageMode(CENTER)
    image(karakter2, 401, 135, 170, 170)
    imageMode(CENTER)
    image(karakter3, 606, 135, 170, 170)
    imageMode(CENTER)
    image(karakter4, 196, 343, 170, 170)
    imageMode(CENTER)
    image(karakter5, 400, 343, 170, 170)
    imageMode(CENTER)
    image(karakter6, 606, 343, 170, 170)
    # Karakters selecteren 
    if mousePressed:
        if (mouseX > 106 and mouseX < (106 + 180) and mouseY > 45 and mouseY < (45 + 180)):
            i = 1
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[0] = 0
            elif speler == 1:
                color[0] = 255
        elif (mouseX > 311 and mouseX < (311 + 180) and mouseY > 45 and mouseY < (45 + 180)):
            i = 2
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[1] = 0
            elif speler == 1:
                color[1] = 255
        elif (mouseX > 516 and mouseX < (516 + 180) and mouseY > 45 and mouseY < (45 + 180)):
            i = 3
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[2] = 0
            elif speler == 1:
                color[2] = 255
        elif (mouseX > 106 and mouseX < (106 + 180) and mouseY > 253 and mouseY < (253 + 180)):
            i = 4
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[3] = 0
            elif speler == 1:
                color[3] = 255
        elif (mouseX > 311 and mouseX < (311 + 180) and mouseY > 253 and mouseY < (253 + 180)):
            i =5
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[4] = 0
            elif speler == 1:
                color[4] = 255    
        elif (mouseX > 516 and mouseX < (516 + 180) and mouseY > 253 and mouseY < (253 + 180)):
            i =6
            gekozen = True
            color = [123, 123, 123, 123, 123, 123]
            if speler == 0:
                color[5] = 0
            elif speler == 1:
                color[5] = 255
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
    