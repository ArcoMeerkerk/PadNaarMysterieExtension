#Daan Enders 1018410
# Width, height
import json
import random
#import PIL
Gamemode = "Start"
#json file inladen + Eventrunner
myjsonfile = open('../assets/json/Evenementen.json', 'r')
jsondata = myjsonfile.read()
Eventrunner = True
obj = json.loads(jsondata)
timer_for_event = 0
event_time = 600
timer_enabled = True
random_event_time = 0
def loadEvent():
    #kiest een random value/event uit Evenementen.json en return deze
    EventKeuze = (random.choice(list(obj.values())))
    return str(EventKeuze)
def setup():
    global backgroundPicture, backgroundPicture
    # The size of the canvas + foto inladen + tekst centreren
    backgroundPicture = loadImage("../assets/images/Bord-0.png")
    size(800,600)
    textAlign(CENTER,CENTER)
def ShowEvent():
    global Gamemode, EventKeuze, Eventrunner, backgroundPicture
    background(100)
    #Afbeelding inladen
    image(backgroundPicture, 150, 100, 500, 300)
    textSize(26)
    #runt eventrunner 1 keer om te bepalen welke event er geprint wordt op de afbeelding
    if Eventrunner == True:
        Eventrunner = False
        EventKeuze = loadEvent()
    text(EventKeuze , 150, 50,500,300)
    if key == 'o':
        background(0)
        return True
    else:
        return False
def timer():
    global timer_for_event, random_event_time, timer_enabled
    print("timer_for_event", timer_for_event)
    print("random_event_time", random_event_time)
    if timer_for_event == 0 or timer_for_event >= event_time:
        timer_for_event = 1
        random_event_time = random.choice(range(event_time))
    elif timer_for_event < event_time and timer_enabled == True: 
        timer_for_event += 1
    if random_event_time >= timer_for_event:
        timer_enabled = ShowEvent()
    else:
        timer_enabled = True

def draw():
    global Gamemode, Eventrunner, timer_for_event
    if Gamemode == "Start":
        background(0)
        timer()
        
    

# def draw():


# def keyPressed():


# def keyReleased(): 
#C:\Users\dfend\OneDrive\Documents\GitHub\PadNaarMysterieExtension\PadNaarMysterieExtension\PadNaarMysterieExtension\EventFunctie\Event.pyde