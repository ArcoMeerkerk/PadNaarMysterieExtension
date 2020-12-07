#Daan Enders 1018410
# Width, height
import json
import random
#import PIL
#backgroundPicture = loadImage("Bord-3.png")
Gamemode = "Start"
#json file inladen + Eventrunner
myjsonfile = open('Evenementen.json', 'r')
jsondata = myjsonfile.read()
Eventrunner = True
obj = json.loads(jsondata)
def eventbepaler():
    #kiest een random value/event uit Evenementen.json en return deze
    EventKeuze = (random.choice(list(obj.values())))
    return str(EventKeuze)
def setup():
    global backgroundPicture, backgroundPicture
    # The size of the canvas
    backgroundPicture = loadImage("Bord-3.png")
    size(800,600)
    textAlign(CENTER,CENTER)
    #backgroundPicture = loadShape('BordBackground.svg')
def event():
    global Gamemode, EventKeuze, Eventrunner, backgroundPicture
    background(100)
    #popupIMG = loadImage("EventWithText.png")
    image(backgroundPicture, 150, 100, 500, 300)
    textSize(26)
    #runt eventrunner 1 keer om te bepalen welke event er geprint wordt op de afbeelding
    if Eventrunner == True:
        Eventrunner = False
        EventKeuze = eventbepaler()
    text(EventKeuze , 150, 50,500,300)
def draw():
    global Gamemode, Eventrunner
    if Gamemode == "Start":
        background(0)
        if key == 'e': 
            event()
        elif key == 'q':
            background(0)
            Eventrunner = True
    

# def draw():


# def keyPressed():


# def keyReleased(): 
#C:\Users\dfend\OneDrive\Documents\GitHub\PadNaarMysterieExtension\PadNaarMysterieExtension\PadNaarMysterieExtension\EventFunctie\Event.pyde