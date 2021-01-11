import random
BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300
charSize = [50,50] # x & y ; width and height ro fullshots
#some renders are not geomatrically centered, this adjustes the rendering for that
battles = 0 #should be Jue Jun's variable, not sure if his bit is working atm
EndPosShift = battles % 6
CharacterImages = None
CharacterCoordinates = None

def Setup(characters):
    global mapImage, fullShot, CharacterImages, CharacterCoordinates
    CharacterCoordinates = [
        ((width // 2) - (charSize[0] //2) + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110,charSize[0],charSize[1]),
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 2) - charSize[1] +2 -105, charSize[0], charSize[1]), # x positie hetzelfde als pos 3, y als pos 6
        ((width // 4 * 3) - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 4 * 3) - charSize[1] - 5 -80, charSize[0],charSize[1]),
        ((width // 2) - (charSize[0] //2) + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70,charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50, (height // 4 * 3) - charSize[1] - 5 - 80, charSize[0],charSize[1]),
        ((width // 4) + (charSize[0] // 2) + 50,(height // 2) - charSize[1] +2 -110, charSize[0], charSize[1])
    ]
    random.shuffle(CharacterCoordinates)
    random.shuffle(characters)
    print(characters)
    print(CharacterCoordinates)
    # print(enumerate(random.shuffle(characters)))
    CharacterImages = [(loadImage("../assets/images/karakters/" + cursorImage + "FullshotTransparent.png"), CharacterCoordinates[index]) for index, cursorImage in enumerate(characters)]
    print(CharacterImages)

    mapImage = loadImage("../assets/images/Bord-4.png")

def Show(font, buttonFont) :
    ShowMap()
    return True
    # ShowStartingPos()
    #ShowEndPos()
    
def ShowMap():
    image(mapImage, 0,0, 800, 800 / 1.41) #667, 500 voor iets betere verhouding 1682 * 1190  1.41

# def ShowStartingPos():
    #first version, later on this will be changed, might throw a tint over it for instance
    # if len(Characters) == 6:
    #     image(fullShot[Characters[0]], (width // 2) - (charSize[0] //2) - offsetXaxisPerFullShot[0] + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110,charSize[0],charSize[1])
    #     image(fullShot[1], (width // 4 * 3) - offsetXaxisPerFullShot[1] - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 2) - charSize[1] +2 -105, charSize[0], charSize[1]) # x positie hetzelfde als pos 3, y als pos 6
    #     image(fullShot[2], (width // 4 * 3) - offsetXaxisPerFullShot[2] - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 4 * 3) - charSize[1] - 5 -80, charSize[0],charSize[1])
    #     image(fullShot[3], (width // 2) - (charSize[0] //2) - offsetXaxisPerFullShot[3] + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70,charSize[0],charSize[1])
    #     image(fullShot[4], (width // 4) - offsetXaxisPerFullShot[4] + (charSize[0] // 2) + 50, (height // 4 * 3) - charSize[1] - 5 - 80, charSize[0],charSize[1])
    #     image(fullShot[5], (width // 4) - offsetXaxisPerFullShot[5] + (charSize[0] // 2) + 50,(height // 2) - charSize[1] +2 -110, charSize[0], charSize[1])
    # elif len(Characters) == 5:
    #     temp= 0
    # else:
    #     temp = ''



    #first version, later on this will be changed, might throw a tint over it for instance
    #fill(0)
    #textSize(32)
    #text("1", width//2, height-(BottomMargin // 2))
    #text("1", (width // 2) - (charSize[0] //2) + 50, (height // 4) - (charSize[1] // 2) + charSize[1] - 110)
    #fill(0) #colour change
    #text("2", (width // 4 * 3) - offsetXaxisPerFullShot[1] - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 2) - charSize[1] +2 -105) # x positie hetzelfde als pos 3, y als pos 6
    #text("3", (width // 4 * 3) - offsetXaxisPerFullShot[2] - charSize[0] - charSize[0] // 2  - charSize[0] // 10 + 50, (height // 4 * 3) - charSize[1] - 5 -80)
    #text("4", (width // 2) - (charSize[0] //2) - offsetXaxisPerFullShot[3] + 50, (height // 1.35) - (charSize[1] // 2) + charSize[1] - 70)
    #text("5", (width // 4) - offsetXaxisPerFullShot[4] + (charSize[0] // 2) + 50, (height // 4 * 3) - charSize[1] - 5 - 80)
    #text("6", (width // 4) - offsetXaxisPerFullShot[5] + (charSize[0] // 2) + 50,(height // 2) - charSize[1] +2 -110)
