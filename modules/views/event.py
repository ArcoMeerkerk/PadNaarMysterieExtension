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
CloseButtonX, CloseButtonY, CloseButtonSizeX, CloseButtonSizeY = 625, 75, 50, 50
TextPlaceX, TextPlaceY, TextSizeX, TextSizeY = 400, 275, 500, 300
BackgroundPlaceX, BackgroundPlaceY, BackgroundSizeX, BackgroundSizeY = 400, 250, 600, 400

def LoadEvent():
    global EventKeuze,LoadEventCheck, TextEvent
    #Kiest een random value/event uit Evenementen.json en return deze
    EventKeuze = random.choice(list(obj.values()))
    return str(EventKeuze)

def Show(fonts):
    global EventKeuze, LoadEventCheck, TimeTicker, EventTimer,TextEvent, CloseButtonSizeX, CloseButtonSizeY, CloseButtonX, CloseButtonY, TextSizeX, TextSizeY, TextPlaceX, TextPlaceY
    TimeTicker = False
    textFont(fonts["ButtonFont"])
    textAlign(CENTER, CENTER)
    textSize(26)
    noStroke()
    fill(100)
    rect(BackgroundPlaceX, BackgroundPlaceY, BackgroundSizeX, BackgroundSizeY, 5)
    if LoadEventCheck == True:
        LoadEventCheck = False
        TextEvent = LoadEvent()
    textFont(fonts["IconFont"])
    fill(255)
    text(u"\uf057", CloseButtonX, CloseButtonY)
    textFont(fonts["ButtonFont"])
    text(TextEvent, TextPlaceX, TextPlaceY, TextSizeX, TextSizeY)

    if mousePressed:
        if(mouseX > CloseButtonX and mouseX < (CloseButtonX + CloseButtonSizeX) and mouseY > CloseButtonY and mouseY < (CloseButtonY + CloseButtonSizeY)):
            EventTimer = 0 + (randomEventTimer - EventEndTime)
            LoadEventCheck = True
            TimeTicker = True

def TimerForEvent(fonts):
    global TimeTicker, randomEventTimer, EventEndTime, EventTimer, LoadEventCheck
    if EventTimer == 0 or EventTimer >= EventEndTime:
        EventTimer = 1
        randomEventTimer = random.choice(range(EventEndTime))
    if EventTimer < EventEndTime and TimeTicker == True:
        EventTimer += 1
    if EventTimer >= randomEventTimer:
        Show(fonts)
    else:
        TimeTicker = True