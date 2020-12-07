from modules import dice

from music import *
 
note = Note(443.1, HN)     # create a note a bit over A4 (440.0)
Play.midi(note)            # and play it!

#Width, height
appSize = [800, 600]
def setup():
    global font, f
    # The size of the canvas
    # smooth()

    # The font must be located in the sketch's
# "data" directory to load successfully
    font = loadFont("./assets/fonts/AventineRegular-64.vlw")
    textFont(font)
    text("word", 10, 50)
    size(appSize[0], appSize[1])
    background(255)
    textSize(64)      
    fill(0)                       
    text("Hello Strings!",100,100)

def draw():
    global font, f
    # dice.showButton()
    # textFont (font, 16)
# def keyPressed():

# def keyReleased():