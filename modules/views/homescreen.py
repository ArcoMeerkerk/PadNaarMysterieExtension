BottomMargin = 75
ButtonHeight = 50
ButtonWidth = 300
charSize = [50,50] # x & y ; width and height ro fullshots
tempCharselect= [True,True,True,True,True,True] # in order of fullshot, see setup()
offsetXaxisPerFullShot = [0,0,0,0,-3,0] #some renders are not geomatrically centered, this adjustes the rendering for that
battles = 0 #should be Jue Jun's variable, not sure if his bit is working atm
EndPosShift = battles % 6

def Setup():
    global mapImage, fullShot
    mapImage = loadImage("../assets/images/Bord-4.png")
    fullShot = [loadImage("../assets/images/karakters/BerserkerFullshotTransparent.png"),loadImage("../assets/images/karakters/FighterFullshotTransparent.png"),loadImage("../assets/images/karakters/GolbinFullshotTransparent.png"),loadImage("../assets/images/karakters/MonkFullshotTransparent.png"),loadImage("../assets/images/karakters/SorcererFullshotTransparent.png"),loadImage("../assets/images/karakters/TurtleFullshotTransparent.png")]

def Show(font, buttonFont) :
    ShowMap()
    ShowStartingPos()
    
    return ShowVechtButton(buttonFont)

def ShowVechtButton(buttonFont) :
    fill(0)
    rectMode(CENTER)
    rect(width//2, height-(BottomMargin // 2), ButtonWidth, ButtonHeight)
    textFont(buttonFont)
    fill(255)
    textSize(32)
    text("VECHT", width//2, height-(BottomMargin // 2))

    if mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - ButtonWidth//2 and mouseX < width//2 + ButtonWidth//2 and \
        mouseY > height-(BottomMargin // 2) - ButtonHeight//2 and mouseY < height-(BottomMargin // 2) + ButtonHeight//2:
        return False
    else :
        return True

def ShowMap():
    image(mapImage, 0,100,800,500) #667, 500 voor beter verhouding

def ShowStartingPos():
    #first version, later on this will be changed, might throw a tint over it for instance
    image(fullShot[0], (width // 2) - (charSize[0] //2) - offsetXaxisPerFullShot[0], (height // 4) - (charSize[1] // 2) + charSize[1],charSize[0],charSize[1])
    image(fullShot[1], (width // 4 * 3) - offsetXaxisPerFullShot[1] - charSize[0] - charSize[0] // 2  - charSize[0] // 10, (height // 2) - charSize[1] +2, charSize[0], charSize[1]) # x positie hetzelfde als pos 3, y als pos 6
    image(fullShot[2], (width // 4 * 3) - offsetXaxisPerFullShot[2] - charSize[0] - charSize[0] // 2  - charSize[0] // 10, (height // 4 * 3) - charSize[1] - 5, charSize[0],charSize[1])
    image(fullShot[3], (width // 2) - (charSize[0] //2) - offsetXaxisPerFullShot[3], (height // 1.35) - (charSize[1] // 2) + charSize[1],charSize[0],charSize[1]) #-7 needed beacuse render is not centered smh
    image(fullShot[4], (width // 4) - offsetXaxisPerFullShot[4] + (charSize[0] // 2), (height // 4 * 3) - charSize[1] - 5, charSize[0],charSize[1])
    image(fullShot[5], (width // 4) - offsetXaxisPerFullShot[5] + (charSize[0] // 2),(height // 2) - charSize[1] +2, charSize[0], charSize[1])

