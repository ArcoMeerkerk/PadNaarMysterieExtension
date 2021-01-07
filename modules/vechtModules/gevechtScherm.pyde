# from modules.vechtModules import karakter
def setup():
    background(255)
    size(800, 600)
    frameRate(60)
    berserker = loadImage("./assets/images/karakters/BerserkerFullshot.png"),
    fighter = loadImage("./assets/images/karakters/FighterFullshot.png"),
    goblin = loadImage("./assets/images/karakters/GoblinFullshot.png"),
    monk = loadImage("./assets/images/karakters/MonkFullshot.png"),
    sorcerer = loadImage("./assets/images/karakters/SorcererFullshot.png"),
    turtle = loadImage("./assets/images/karakters/TurtleFullshot.png")
def draw():
    gevechtScherm()
def gevechtScherm():
    # Speler1 = GekozenKarakters[0]
    Speler1 = 3
    # Speler2 = GekozenKarakters[1]
    Speler2 = 5
    image(berserker, 50, 50, 50, 50)

