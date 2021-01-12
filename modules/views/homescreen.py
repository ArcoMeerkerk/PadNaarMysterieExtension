Timer = 0
ChangedAudioFiles = False
ChangeAudioFilesPressed1 = False
ChangeAudioFilesPressed2 = False
def Show(font, buttonFont, mouseInfo, soundFiles) :
    global ChangeAudioFilesPressed1, ChangeAudioFilesPressed2
    SoundFiles = soundFiles
    textFont(font)
    fill('#C69C6D')
    textAlign(CENTER)               
    text("Homescreen", width//2, 150)
    ChangeAudioFiles(mouseInfo["MouseReleased"], soundFiles)
    ChangeAudioFilesPressed1 = ShowButton(buttonFont, mouseInfo["MouseReleased"], 0, 15, 15, align="LEFT")
    ChangeAudioFilesPressed2 = ShowButton(buttonFont, mouseInfo["MouseReleased"], 0, 15, 15, align="RIGHT")
    return not ShowButton(buttonFont, mouseInfo["MouseReleased"], 75, 50, 300, "VECHT")

def ShowButton(buttonFont, mouseReleased, bottomMargin, buttonHeight, buttonWidth,  buttonText = "", align="CENTER") :
    global Timer
    if buttonText != "" :
        fill('#C69C6D')
        rectMode(CENTER)
        rect(width//2, height-bottomMargin, buttonWidth, buttonHeight)
        textFont(buttonFont)
        fill(255)
        textSize(32)
        text(buttonText, width//2, height-bottomMargin+10)
    Timer += 1
    if align == "CENTER" :
        if mousePressed and mouseButton == LEFT and Timer > 30 and \
            mouseX > width//2 - buttonWidth//2 and mouseX < width//2 + buttonWidth//2 and \
            mouseY > height-bottomMargin - buttonHeight//2 and mouseY < height-bottomMargin + buttonHeight//2:
            return True
        else :
            return False
    elif align == "LEFT" :
        if mousePressed and mouseButton == LEFT and Timer > 30 and \
            mouseX > 0 and mouseX < buttonWidth and \
            mouseY > height-bottomMargin - buttonHeight//2 and mouseY < height-bottomMargin + buttonHeight//2:
            return True
        else :
            return False
    elif align == "RIGHT" :
        if mousePressed and mouseButton == LEFT and Timer > 30 and\
            mouseX > width - buttonWidth and mouseX < width and \
            mouseY > height-bottomMargin - buttonHeight//2 and mouseY < height-bottomMargin + buttonHeight//2:
            return True
        else :
            return False

def ChangeAudioFiles(mouseReleased, soundFiles) :
    global ChangedAudioFiles
    if (ChangeAudioFilesPressed1 or ChangeAudioFilesPressed2) and mouseReleased:
        if ChangedAudioFiles == False:
            soundFiles["ClickSound"] = soundFiles["KlikGeluidSecond"]
            soundFiles["FightSound1"] = soundFiles["FightSound1Second"]
            soundFiles["FightSound2"] = soundFiles["FightSound2Second"]
            ChangedAudioFiles = True
        elif ChangedAudioFiles == True:
            soundFiles["ClickSound"] = soundFiles["ClickSoundOrg"]
            soundFiles["FightSound1"] = soundFiles["FightSound1Org"]
            soundFiles["FightSound2"] = soundFiles["FightSound1Org"]
            ChangedAudioFiles = False
