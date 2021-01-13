import random, copy
BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300
charSize = [50,50] # x & y ; width and height ro fullshots
battles = 0 #should be Jue Jun's variable, not sure if his bit is working atm
EndPosShift = battles % 6
CharacterImages = None
CharacterCoordinates = None
mapImage = None

def Setup(characters):
    global mapImage, fullShot, CharacterImages, CharacterCoordinates, allowedPos
    CharacterCoordinates = [
        ((width // 2) - (charSize[0] //2) + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110+3,charSize[0],charSize[1]),
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50-1, (height // 2) - charSize[1] +2 -105+5, charSize[0], charSize[1]), # x positie hetzelfde als pos 3, y als pos 6
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50-1, (height // 4 * 3) - charSize[1] -80 - 1.25, charSize[0],charSize[1]),
        ((width // 2) - (charSize[0] //2) + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70+1,charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50+7, (height // 4 * 3) - charSize[1] - 5 - 80+3, charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50+5+2,(height // 2) - charSize[1] +2 -110+7, charSize[0], charSize[1])
    ]
    
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
    charColour =(
        ("#F15F74","Red"),
        ("#F76D3C","Orange"),
        ("#913CCD","Purple"),
        ("#98CB4A","Green"),
        ("#5481E6","Blue"),
        ("#FFF452","Yellow")
    )
    #charColour = ["#FFF452","#A2DCF2","#82C91E","#FF5751","#FF57D0","#FF6100"]

    #random.shuffle(coordinateIndexes)
    random.shuffle(characters)
    CharacterImages = [
        (loadImage("../assets/images/karakters/" + cursorImage + "FullshotTransparent.png"),
        allowedPos[index],
        charColour[index][0],
        loadImage("../assets/images/tiles/Tile" + charColour[index][1] + ".png")
    ) for index,
        cursorImage in enumerate(characters)]
    print(coordinateIndexes)
    print(CharacterImages)
    print(characters)
    mapImage = loadImage("../assets/images/Bord-4.png")

def Show(font, buttonFont, iconFont, battleCount) :
    image(mapImage, 0,0, 800, 800 / 1.41)

    ShowStartingPos()
    ShowEndPos(iconFont)
    return True

def ShowStartingPos():
    #[(processing.core.PImage@cd16430, 3), (processing.core.PImage@66dda403, 4), (processing.core.PImage@5f304d3b, 6), (processing.core.PImage@592ad14c, 5), (processing.core.PImage@5e5ddebd, 1)]
    for i in range(len(CharacterImages)):
        image(CharacterImages[i][3],CharacterCoordinates[CharacterImages[i][1]][0]-10,CharacterCoordinates[CharacterImages[i][1]][1]-10,62,62)
        image(CharacterImages[i][0],CharacterCoordinates[CharacterImages[i][1]][0],CharacterCoordinates[CharacterImages[i][1]][1],CharacterCoordinates[CharacterImages[i][1]][2],CharacterCoordinates[CharacterImages[i][1]][3])

def ShowEndPos(iconFont):
    
    #colorMode(RGB)
    for i in range(len(CharacterImages)):
        
        
        fill(CharacterImages[i][2])
        textFont(iconFont)
        textSize(32)	
        if len(CharacterImages) == 4:
            if i + 3 + EndPosShift < 4:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]+3+EndPosShift][0],CharacterCoordinates[allowedPos[i]+3+EndPosShift][1]+75)
            if i + 3 + EndPosShift >= 4:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]-3+EndPosShift][0],CharacterCoordinates[allowedPos[i]-3+EndPosShift][1]+75)        
        
        elif len(CharacterImages) == 5:
            #text("temp",CharacterCoordinates[CharacterImages[i][1]][0]+50,CharacterCoordinates[CharacterImages[i][1]][1]+50) test to see if offset actually works, if battles = 0, difference between temp and shift should be 3(straight across the middle)
            if i + 3 + EndPosShift < 5:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]+3+EndPosShift][0],CharacterCoordinates[allowedPos[i]+3+EndPosShift][1]+75)
            if i + 3 + EndPosShift >= 5:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]-3+EndPosShift][0],CharacterCoordinates[allowedPos[i]-3+EndPosShift][1]+75)
        else:
            if i + 3 + EndPosShift < 6:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]+3+EndPosShift][0],CharacterCoordinates[allowedPos[i]+3+EndPosShift][1]+75)
            if i + 3 + EndPosShift >= 6:
                text(u"\uf024",CharacterCoordinates[allowedPos[i]-3+EndPosShift][0],CharacterCoordinates[allowedPos[i]-3+EndPosShift][1]+75) 

        #fill(255)           


