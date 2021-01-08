from modules import audio
from modules.views import viewsModel, splashScreen, playerAmount, homescreen
from java.awt.event import KeyEvent
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
KeyInfo = {}

def setup():
    global BackButton
    audio.SetVolume([Sf1, Sf2], [0.5, 0.5])
    BackButton = loadImage('./assets/images/BackButton.png')

    background(255)
    size(800, 600)
    frameRate(60)
     
    # Sf1.play()
    
def draw():
    global KeyInfo, MouseScroll
    background(255)
    viewsModel.Show(KeyInfo, MainFont, ButtonFont, BackButton)          

    # audio.MouseEffect([Sf1, Sf2])
    # audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)
    MouseScroll = 0
    KeyInfo["KeyReleased"] = False

def keyReleased(event) :
    global KeyInfo
    KeyInfo["KeyReleased"] = True

    KeyInfo["KeyLocation"] = []
    if event.getNative().getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT and event.getNative().getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT :
        KeyInfo["KeyLocation"].append("right")
        KeyInfo["KeyLocation"].append("left")
    if event.getNative().getKeyLocation() == KeyEvent.KEY_LOCATION_RIGHT :
        KeyInfo["KeyLocation"].append("right")
    if event.getNative().getKeyLocation() == KeyEvent.KEY_LOCATION_LEFT :
        KeyInfo["KeyLocation"].append("left")
    print(KeyInfo)

# def keyPressed():

def mouseWheel(event):
    global MouseScroll
    MouseScroll = event.getCount()