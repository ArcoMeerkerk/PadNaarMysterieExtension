#Width, height
appSize = [800, 600]
from modules import vechtknop

def setup():
    # The size of the canvas
    size(appSize[0], appSize[1])
    background(0)
    # dice.setupFuctions()

def draw():
    vechtknop.knop()

# def keyPressed():
# def keyReleased():