class Karakter:
    Image = None

    def __init__(self, image) :
        self.IsGekozen = False
        self.Image = image
Karakters = []
GekozenKarakters = []
# Color values voor de vierkanten waar de plaatjes zijn
color = ["#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C", "#C0963C"]
AmountofPlayers = 6
aantalKaraktersGekozen = 0

def Setup(amountOfPlayers):
    global Karakters, SelectieAchtergrond, AmountofPlayers
    Karakters = [
        Karakter(loadImage("./assets/images/karakters/Berserker-min.png")),
        Karakter(loadImage("./assets/images/karakters/Fighter-min.png")),
        Karakter(loadImage("./assets/images/karakters/Goblin-min.png")),
        Karakter(loadImage("./assets/images/karakters/Monk-min.png")),
        Karakter(loadImage("./assets/images/karakters/Sorcerer-min.png")),
        Karakter(loadImage("./assets/images/karakters/Turtle-min.png")),
    ]
    SelectieAchtergrond = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
    AmountofPlayers = amountOfPlayers

def Show():
    global Karakters, GekozenKarakters, color, aantalKaraktersGekozen
    background(37)
    #Achtergrond voor de karakter selectie knoppen
    imageMode(CENTER)
    image(SelectieAchtergrond, 200, 108, 170, 170)
    image(SelectieAchtergrond, 400, 108, 170, 170)
    image(SelectieAchtergrond, 600, 108, 170, 170)
    image(SelectieAchtergrond, 200, 308, 170, 170)
    image(SelectieAchtergrond, 400, 308, 170, 170)
    image(SelectieAchtergrond, 600, 308, 170, 170)
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
    image(Karakters[0].Image, 200, 113, 140, 140)
    image(Karakters[1].Image, 400, 113, 140, 140)
    image(Karakters[2].Image, 600, 113, 140, 140)
    image(Karakters[3].Image, 200, 313, 140, 140)
    image(Karakters[4].Image, 400, 313, 140, 140)
    image(Karakters[5].Image, 600, 313, 140, 140)
    # Karakters selecteren 
    if aantalKaraktersGekozen < AmountofPlayers:
        if mousePressed:
            if Karakters[0].IsGekozen == False:
                if (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append('Berserker')
                    color[0] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[0].IsGekozen = True
            if Karakters[1].IsGekozen == False:
                if (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append('Fighter')
                    color[1] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[1].IsGekozen = True
            if Karakters[2].IsGekozen == False:
                if (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 42.5 and mouseY < (42.5 + 145)):
                    GekozenKarakters.append('Goblin')
                    color[2] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[2].IsGekozen = True
            if Karakters[3].IsGekozen == False:
                if (mouseX > 127.5 and mouseX < (127.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append('Monk')
                    color[3] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[3].IsGekozen = True
            if Karakters[4].IsGekozen == False:
                if (mouseX > 327.5 and mouseX < (327.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append('Sorcerer')
                    color[4] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[4].IsGekozen = True
            if Karakters[5].IsGekozen == False:
                if (mouseX > 526.5 and mouseX < (526.5 + 145) and mouseY > 240.5 and mouseY < (240.5 + 145)):
                    GekozenKarakters.append('Turtle')
                    color[5] = "#00FF00"
                    aantalKaraktersGekozen += 1
                    Karakters[5].IsGekozen = True
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
            for karakter in Karakters :
                karakter.IsGekozen = False
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
                print(GekozenKarakters)
                return False
    
    return True