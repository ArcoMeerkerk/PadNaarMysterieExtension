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
# f2 = SoundFile(this, "./assets/audio/multimedia_button_click_001.wav")
KeyInfo = {}
SoundFiles = {}
KlikGeluid = SoundFile(this, "./assets/audio/selectionClickSound.wav")
def setup():
    global BackButton, Sf2, spark
    # audio.SetVolume([Sf2], [0.5, 0.5])
    # SoundFiles['naam'] = SoundFile(this, "./assets/audio/------.wav")
    BackButton = loadImage('./assets/images/BackButton.png')
    background(255)
    size(800, 600)
    frameRate(60)
    # Sf2.play()
    
def draw():
    global KeyInfo, MouseScroll, SoundFiles, spark
    background(255)
    viewsModel.Show(KeyInfo, SoundFiles, MainFont, ButtonFont, BackButton)          
    # audio.MouseEffect([Sf1, Sf2])
    # audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)
    MouseScroll = 0
    KeyInfo["KeyReleased"] = False

def keyReleased(event) :
    global KeyInfo
    KeyInfo["KeyReleased"] = True
def mouseReleased():
    KlikGeluid.play()


# def mouseWheel(event):
#     global MouseScroll
#     MouseScroll = event.getCount()