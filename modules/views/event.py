import json
import random

myjsonfile = open('./assets/json/Evenementen.json', 'r')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)
EventEndTime = 600
EventTimer = 0
randomEventTimer = 0
TimeTicker = True
TextEvent = ''
LoadEventCheck = True
ImagePlaceX, ImagePlaceY, ImageSizeX, ImageSizeY = 625, 75, 50, 50
TextPlaceX, TextPlaceY, TextSizeX, TextSizeY = 400, 275, 500, 300
BackgroundPlaceX, BackgroundPlaceY, BackgroundSizeX, BackgroundSizeY = 400, 250, 600, 400

def LoadEvent():
    global EventKeuze,LoadEventCheck, TextEvent
    #Kiest een random value/event uit Evenementen.json en return deze
    EventKeuze = random.choice(list(obj.values()))
    return str(EventKeuze)

def Show(backButton, bellFont):
    global EventKeuze, LoadEventCheck, TimeTicker, EventTimer,TextEvent, ImageSizeX, ImageSizeY, ImagePlaceX, ImagePlaceY, TextSizeX, TextSizeY, TextPlaceX, TextPlaceY
    TimeTicker = False
    imageMode(CORNER)
    textAlign(CENTER, CENTER)
    textFont(bellFont)
    textSize(28)
    noStroke()
    rectMode(CENTER)
    fill(250, 235)
    rect(BackgroundPlaceX, BackgroundPlaceY, BackgroundSizeX, BackgroundSizeY, 12)
    if LoadEventCheck == True:
        LoadEventCheck = False
        TextEvent = LoadEvent()
    image(backButton, ImagePlaceX, ImagePlaceY, ImageSizeX, ImageSizeY)
    fill('#C69C6D')
    text(TextEvent, TextPlaceX, TextPlaceY, TextSizeX, TextSizeY)

    if mousePressed:
        if(mouseX > ImagePlaceX and mouseX < (ImagePlaceX + ImageSizeX) and mouseY > ImagePlaceY and mouseY < (ImagePlaceY + ImageSizeY)):
            EventTimer = 0 + (randomEventTimer - EventEndTime)
            LoadEventCheck = True
            TimeTicker = True

def TimerForEvent(backButton, bellFont):
    global TimeTicker, randomEventTimer, EventEndTime, EventTimer, LoadEventCheck
    if EventTimer == 0 or EventTimer >= EventEndTime:
        EventTimer = 1
        randomEventTimer = random.choice(range(EventEndTime))
    if EventTimer < EventEndTime and TimeTicker == True:
        EventTimer += 1
    if EventTimer >= randomEventTimer:
        Show(backButton, bellFont)
    else:
        TimeTicker = True