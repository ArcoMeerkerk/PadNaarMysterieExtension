gedrukt = False
from modules.vechtModules import karakter, vechtknop

def Show():
    global gedrukt
    if gedrukt == False:
        gedrukt = vechtknop.knop()
    if gedrukt == True:
        karakter.SelectieScherm()

def Setup():
    data["karakter1"] = loadImage("./assets/images/karakters/Berserker-min.png")
    data["karakter2"] = loadImage("./assets/images/karakters/Fighter-min.png")
    data["karakter3"] = loadImage("./assets/images/karakters/Goblin-min.png")
    data["karakter4"] = loadImage("./assets/images/karakters/Monk-min.png")
    data["karakter5"] = loadImage("./assets/images/karakters/Sorcerer-min.png")
    data["karakter6"] = loadImage("./assets/images/karakters/Turtle-min.png")
    data["karakterSpelerInfo"] = loadImage("./assets/images/achtergrondElementen/karakterInfo.png")
    data["selectieAchtergrond"] = loadImage("./assets/images/achtergrondElementen/selectieAchtergrond.png")
    data["houtenAchtergrond"] = loadImage("./assets/images/achtergrondElementen/houtenAchtergrond.jpg")
    data["geselecteerdeKarakterSpeler1"] = loadImage('/assets/images/achtergrondElementen/vraagteken.png')
    data["geselecteerdeKarakterSpeler2"] = loadImage('/assets/images/achtergrondElementen/vraagteken.png')

    return data