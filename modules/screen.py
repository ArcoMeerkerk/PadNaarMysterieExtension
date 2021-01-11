from java.awt.GraphicsEnvironment import getLocalGraphicsEnvironment

def SetScreenLocation(window, xOffset=-800) :
    windowLocation = GetWindowLocation(window)
    
    windowXPos = windowLocation[0][0] + windowLocation[1][0] - window.width + xOffset - 20
    windowYPos = (windowLocation[0][1] // 2 - window.height // 2) - 40 + windowLocation[1][1]

    window.surface.setLocation(windowXPos, windowYPos)
    return windowLocation

def GetWindowLocation(window) :
    currentFrame =  window.surface.getNative().getFrame()
    screens = list(getLocalGraphicsEnvironment().getScreenDevices())
    screens.sort(key=lambda screen: screen.getDefaultConfiguration().getBounds().x)
    currentScreen = None

    for screen in screens:
        if currentFrame.getX() + window.width // 2 > screen.getDefaultConfiguration().getBounds().x and \
            currentFrame.getX() + window.width // 2 < screen.getDefaultConfiguration().getBounds().x + screen.getDisplayMode().getWidth() :
            currentScreen = screen
    
    #Window on the right monitor
    if currentScreen == None :
        for screen in screens:
            if currentFrame.getX() > screen.getDefaultConfiguration().getBounds().x and \
                currentFrame.getX() < screen.getDefaultConfiguration().getBounds().x + screen.getDisplayMode().getWidth() :
                currentScreen = screen
    
    #Window on the left monitor
    if currentScreen == None :
        for screen in screens:
            if currentFrame.getX() + window.width * 2 > screen.getDefaultConfiguration().getBounds().x and \
                currentFrame.getX() + window.width * 2 < screen.getDefaultConfiguration().getBounds().x + screen.getDisplayMode().getWidth() :
                currentScreen = screen

    currentDisplayWidth = window.displayWidth
    currentDisplayHeight = window.displayHeight
    offsetX = 0
    offsetY = 0

    if currentScreen != None :
        currentDisplayWidth = currentScreen.getDisplayMode().getWidth()
        currentDisplayHeight = currentScreen.getDisplayMode().getHeight()
        offsetX = currentScreen.getDefaultConfiguration().getBounds().x
        offsetY = currentScreen.getDefaultConfiguration().getBounds().y

    return ((currentDisplayWidth, currentDisplayHeight), (offsetX, offsetY))
