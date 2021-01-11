import glob
CursorImages = None
CursorCounter = 0

def Setup() :
    global CursorImages
    CursorImages = [loadImage(cursorImage) for cursorImage in glob.glob("./assets/gif/cursor/cursor-*.png")]

def Show() :
    global CursorCounter
    if frameCount % 8 == 0 :
        cursor(CursorImages[CursorCounter])

    CursorCounter += 1
    if CursorCounter >= len(CursorImages) :
        CursorCounter = 0