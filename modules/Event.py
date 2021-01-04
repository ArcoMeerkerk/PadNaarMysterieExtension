import json
import random
myjsonfile = open('../assets/json/Evenementen.json', 'r')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)
EventEndTime = 600
EventTimer = 0
randomEventTimer = 0
TimeTicker = True
TextEvent = ''
loadEventCheck = True
ImagePlaceX, ImagePlaceY, ImageSizeX, ImageSizeY = 600, 60, 50, 50
TextPlaceX, TextPlaceY, TextSizeX, TextSizeY = 150, 50, 500, 300

def loadEvent():
    global EventKeuze,loadEventCheck, TextEvent
    #kiest een random value/event uit Evenementen.json en return deze
    EventKeuze = random.choice(list(obj.values()))
    return str(EventKeuze)

def ShowEvent():
    global EventKeuze, loadEventCheck, TimeTicker, EventTimer,TextEvent, backbutton, ImageSizeX, ImageSizeY, ImagePlaceX, ImagePlaceY, TextSizeX, TextSizeY, TextPlaceX, TextPlaceY
    TimeTicker = False
    textSize(26)
    background(100)
    if loadEventCheck == True:
        textSize(26)
        loadEventCheck = False
        TextEvent = loadEvent()
    image(backbutton, ImagePlaceX, ImagePlaceY, ImageSizeX, ImageSizeY)
    text(TextEvent, TextPlaceX, TextPlaceY,TextSizeX,TextSizeY)

    if mousePressed:
        if(mouseX > ImagePlaceX and mouseX < (ImagePlaceX + ImageSizeX) and mouseY > ImagePlaceY and mouseY < (ImagePlaceY + ImageSizeY)):
            background(0)
            EventTimer = 0 + (randomEventTimer - EventEndTime)
            loadEventCheck = True
            TimeTicker = True

def TimerForEvent():
    global TimeTicker, randomEventTimer, EventEndTime, EventTimer,loadEventCheck, TextEvent, backbutton
    print("Event timer", EventTimer)
    print("RandomEventTimer", randomEventTimer)
    if EventTimer == 0 or EventTimer >= EventEndTime:
        EventTimer = 1
        randomEventTimer = random.choice(range(EventEndTime))
    if EventTimer < EventEndTime and TimeTicker == True:
        EventTimer += 1
    if EventTimer >= randomEventTimer:
        ShowEvent()
    else:
        TimeTicker = True
def setup():
    global backbutton
    backbutton = loadImage('../assets/images/BackButton.png')
    size(800,600)
    textAlign(CENTER,CENTER)

def draw():
    global TimeTicker, randomEventTimer, EventEndTime, EventTimer, EventKeuze,loadEventCheck, TextEvent, backbutton
    background(0)
    TimerForEvent()