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
    global mapImage, fullShot, CharacterImages, CharacterCoordinates
    CharacterCoordinates = [
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 2) - charSize[1] +2 -105, charSize[0], charSize[1]), # x positie hetzelfde als pos 3, y als pos 6
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 4 * 3) - charSize[1] - 5 -80, charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50, (height // 4 * 3) - charSize[1] - 5 - 80, charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50,(height // 2) - charSize[1] +2 -110, charSize[0], charSize[1])
    ]
    
    pos1 = ((width // 2) - (charSize[0] //2) + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110,charSize[0],charSize[1])
    pos4 = ((width // 2) - (charSize[0] //2) + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70,charSize[0],charSize[1])
    
    

    if len(characters) == 6:
        CharacterCoordinates.extend(pos1, pos4)

    elif len(characters) == 5:
        if random.choice([True, False]):
            CharacterCoordinates.append(pos1)
        else :
            CharacterCoordinates.append(pos4)
    print(CharacterCoordinates)        
    
     

        
    coordinateIndexes = range(len((CharacterCoordinates)))
    #print(coordinateIndexes)
    #random.shuffle(coordinateIndexes)
    random.shuffle(characters)
    CharacterImages = [(loadImage("../assets/images/karakters/" + cursorImage + "FullshotTransparent.png"), coordinateIndexes[index]) for index, cursorImage in enumerate(characters)]
    print(CharacterImages)
    print(characters)

    mapImage = loadImage("../assets/images/Bord-4.png")

def Show(font, buttonFont, battleCount) :
    image(mapImage, 0,0, 800, 800 / 1.41)

    ShowStartingPos()
    #ShowEndPos()
    return True

def ShowStartingPos():
    #[(570, 147, 50, 50), (570, 315, 50, 50), (275, 315, 50, 50), (275, 142, 50, 50), (425, 65, 50, 50), (425, 399.0, 50, 50), None]
    #[(processing.core.PImage@cd16430, 3), (processing.core.PImage@66dda403, 4), (processing.core.PImage@5f304d3b, 6), (processing.core.PImage@592ad14c, 5), (processing.core.PImage@5e5ddebd, 1)]
    for i in range(len(CharacterImages)):
        image(CharacterImages[i][0],CharacterCoordinates[CharacterImages[i][1]][0],CharacterCoordinates[CharacterImages[i][1]][1],CharacterCoordinates[CharacterImages[i][1]][2],CharacterCoordinates[CharacterImages[i][1]][3])

def ShowEndPos():
    for i in range(len(CharacterImages)):
        fill
        text("temp",CharacterCoordinates[CharacterImages[i][1]][0],CharacterCoordinates[CharacterImages[i][1]][1],CharacterCoordinates[CharacterImages[i][1]][2],CharacterCoordinates[CharacterImages[i][1]][3])


