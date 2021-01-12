import glob
CursorImages = None
CursorCounter = 0

def Setup() :
    global CursorImages
    CursorImages = [loadImage(cursorImage) for cursorImage in glob.glob("./assets/gif/cursor/cursor-*.png")]

def Show(window) :
    global CursorCounter
    if window.frameCount % 8 == 0 :
        window.cursor(CursorImages[CursorCounter])

    CursorCounter += 1
    if CursorCounter >= len(CursorImages) :
        CursorCounter = 0