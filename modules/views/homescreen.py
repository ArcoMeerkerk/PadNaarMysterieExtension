
import glob, random
from modules.screen import SetScreenLocation
from modules.screen import GetWindowLocation
from modules.views import pdfViewer

IconFont = None
PdfViewerWindowScreen = None
Timer = 0
ChangedAudioFiles = False
ChangeAudioFilesPressed1 = False
ChangeAudioFilesPressed2 = False

BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300
charSize = [50,50] # x & y ; width and height ro fullshots
EndPosShift = 0
CharacterImages = None
CharacterCoordinates = None
mapImage = None

def Setup(characters):
    global mapImage, fullShot, CharacterImages, CharacterCoordinates, allowedPos, handleidingIcon, vechtIcon, Characters
    CharacterCoordinates = [
        ((width // 2) - (charSize[0] //2) + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110+3,charSize[0],charSize[1]),
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50-1, (height // 2) - charSize[1] +2 -105+5, charSize[0], charSize[1]), # x positie hetzelfde als pos 3, y als pos 6
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50-1, (height // 4 * 3) - charSize[1] -80 - 1.25, charSize[0],charSize[1]),
        ((width // 2) - (charSize[0] //2) + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70+1,charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50+7, (height // 4 * 3) - charSize[1] - 5 - 80+3, charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50+5+2,(height // 2) - charSize[1] +2 -110+7, charSize[0], charSize[1])
    ]
    Characters = characters
    
    if len(characters) == 6:
        allowedPos = [0,1,2,3,4,5]

    elif len(characters) == 5:
        if random.choice([True, False]):
          allowedPos = [1,2,3,4,5]  
        else :
            allowedPos = [0,1,2,4,5]
    else:
        allowedPos = [1,2,4,5]        
                   
    coordinateIndexes = range(len((allowedPos)))
    charColour =[
        ("#F15F74","Red"),
        ("#F76D3C","Orange"),
        ("#913CCD","Purple"),
        ("#98CB4A","Green"),
        ("#5481E6","Blue"),
        ("#FFF452","Yellow")
    ]
    random.shuffle(charColour)
    random.shuffle(characters)
    CharacterImages = [
        (loadImage("./assets/images/karakters/" + cursorImage + "Fullshot.png"),
        allowedPos[index],
        charColour[index][0],
        loadImage("./assets/images/tiles/Tile" + charColour[index][1] + ".png")
    ) for index,
        cursorImage in enumerate(characters)]
    mapImage = loadImage("./assets/images/Bord.png")
    handleidingIcon = loadImage('./assets/images/icons/scroll.png')
    vechtIcon = loadImage('./assets/images/icons/swords.png')

def Show(font, buttonFont, mouseInfo, soundFiles, iconFont, bellFont, fightCounter) :
    global ChangeAudioFilesPressed1, ChangeAudioFilesPressed2, PdfViewerWindowScreen, BellFont, EndPosShift
    BellFont = bellFont
    EndPosShift = fightCounter % 6
    imageMode(CORNER)
    image(mapImage, 0,0, 800, 800 / 1.41)
    ShowStartingPos()
    ShowEndPos(iconFont)

    SoundFiles = soundFiles
    ChangeAudioFiles(mouseInfo["MouseReleased"], soundFiles)
    ChangeAudioFilesPressed1 = ShowButton(buttonFont, mouseInfo["MouseReleased"], 0, 15, 15, align="LEFT")
    ChangeAudioFilesPressed2 = ShowButton(buttonFont, mouseInfo["MouseReleased"], 0, 15, 15, align="RIGHT")
    if ShowButton(buttonFont, mouseInfo["MouseReleased"], 15, 40, 200, "Handleiding", align="RIGHT", rightMargin=100) :
        if PdfViewerWindowScreen == None :
            PdfViewerWindowScreen = pdfViewer.PdfViewerWindow([loadImage(pageFile) for pageFile in glob.glob("./assets/pdf/handleiding/Page-*.png")],
            iconFont,
            loadImage("./assets/images/icons/document.png"),
            GetWindowLocation(this))
            SetScreenLocation(this)
        elif PdfViewerWindowScreen.IsVisable == False :
            PdfViewerWindowScreen.getSurface().setVisible(True)
            PdfViewerWindowScreen.SetWindowLocation(SetScreenLocation(this))

    vechtKnop = not ShowButton(buttonFont, mouseInfo["MouseReleased"], 15, 40, 200, "Vecht", align="LEFT", leftMargin=100)
    imageMode(CENTER)
    image(handleidingIcon, 600, 530, 50, 50)
    image(vechtIcon, 200, 530, 50, 50)
    rectMode(CENTER)
    rect(403, 47, 273, 41, 12)
    textAlign(CENTER, CENTER)
    fill('#C69C6D')
    textFont(bellFont)
    textSize(27)
    text('Gevechten Teller: ' + str((fightCounter- 3) % 6), 400, 46)
    return vechtKnop

def ShowButton(buttonFont, mouseReleased, bottomMargin, buttonHeight, buttonWidth,  buttonText = "", align="CENTER", rightMargin=0, leftMargin=0) :
    global Timer
    if buttonText != "" :
        fill('#C69C6D')
        if align == "CENTER" :
            rectMode(CENTER)
            rect(width//2, height-bottomMargin, buttonWidth, buttonHeight, 12)
        if align == "LEFT" :
            rectMode(CORNER)
            rect(leftMargin, height - bottomMargin - buttonHeight, buttonWidth, buttonHeight, 12)
        if align == "RIGHT" :
            rectMode(CORNER)
            rect(width - rightMargin - buttonWidth, height-bottomMargin - buttonHeight, buttonWidth, buttonHeight, 12)
        textFont(BellFont)
        fill(255)
        textSize(27)
        textAlign(CENTER, CENTER)
        if align == "CENTER" :
            text(buttonText, width//2, height-bottomMargin+10)
        if align == "LEFT" :
            text(buttonText, leftMargin + buttonWidth // 2, height-bottomMargin - buttonHeight // 2)
        if align == "RIGHT" :
            text(buttonText, width - rightMargin - buttonWidth // 2,  height-bottomMargin - buttonHeight // 2)
        
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
            mouseX > leftMargin and mouseX < buttonWidth + leftMargin and \
            mouseY > height-bottomMargin - buttonHeight//2 and mouseY < height-bottomMargin + buttonHeight//2:
            return True
        else :
            return False
    elif align == "RIGHT" :
        if mousePressed and mouseButton == LEFT and Timer > 30 and\
            mouseX > width - rightMargin - buttonWidth and mouseX < width - rightMargin and \
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

def ShowStartingPos():
    for i in range(len(CharacterImages)):
        image(CharacterImages[i][3],CharacterCoordinates[CharacterImages[i][1]][0]-10,CharacterCoordinates[CharacterImages[i][1]][1]-10,62,62)
        image(CharacterImages[i][0],CharacterCoordinates[CharacterImages[i][1]][0],CharacterCoordinates[CharacterImages[i][1]][1],CharacterCoordinates[CharacterImages[i][1]][2],CharacterCoordinates[CharacterImages[i][1]][3])

def ShowEndPos(iconFont):
    for i in range(len(CharacterImages)):
        fill(CharacterImages[i][2])
        textFont(iconFont)
        textSize(32)
        text(u"\uf024",CharacterCoordinates[(allowedPos[i]+ EndPosShift) % 6][0] -10,CharacterCoordinates[(allowedPos[i]+ EndPosShift) % 6][1]+65)

