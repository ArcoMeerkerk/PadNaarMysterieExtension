from modules import audio
from modules.views import viewsModel, splashScreen, playerAmount, homescreen
add_library("sound")

MouseScroll = 0
IsShowingSplashScreen = True
IsShowingPlayerAmount = False
IsShowingPlayerSelection = False
IsShowingHomescreen = False
MainFont = loadFont("./assets/fonts/Algerian-64.vlw")
ButtonFont = loadFont("./assets/fonts/ArialMT-32.vlw")
# Font = loadFont("./assets/fonts/AventineRegular-64.vlw")
Sf1 = SoundFile(this, "./assets/audio/piano.wav")
Sf2 = SoundFile(this, "./assets/audio/hertz.wav")

def setup():
    audio.SetVolume([Sf1, Sf2], [0.5, 0.5])

    background(255)
    size(800, 600)
    frameRate(60)
    
    # Sf1.play()
    
def draw():
    global MouseScroll

    background(255)
    viewsModel.Show(MainFont, ButtonFont)

    # audio.MouseEffect([Sf1, Sf2])
    # audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)
    MouseScroll = 0

# def keyPressed():
# def keyReleased():

def mouseWheel(event):
    global MouseScroll
    MouseScroll = event.getCount()