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
BellFont = loadFont("./assets/fonts/BellMTBold-48.vlw")
KeyInfo = {}
MouseInfo = {}
SoundFiles = {
    'ClickSound' : SoundFile(this, "./assets/audio/SelectionClickSound.wav"),
    'FightSound1' : SoundFile(this, "./assets/audio/Fight1.wav"),
    'FightSound2' : SoundFile(this, "./assets/audio/Fight2.wav"),
    'ClickSoundOrg' : SoundFile(this, "./assets/audio/SelectionClickSound.wav"),
    'FightSound1Org' : SoundFile(this, "./assets/audio/Fight1.wav"),
    'FightSound2Org' : SoundFile(this, "./assets/audio/Fight2.wav"),
    'KlikGeluidSecond' : SoundFile(this, "./assets/audio/KLIK.wav"),
    'FightSound1Second' : SoundFile(this, "./assets/audio/PEW.wav"),
    'FightSound2Second' : SoundFile(this, "./assets/audio/BOOM.wav"),
    'VictorySound' : SoundFile(this, "./assets/audio/Victory.wav"),
    'VictoryMusic' : SoundFile(this, "./assets/audio/VictoryMusic.wav")
}

def setup():
    global BackButton
    audio.SetVolume(SoundFiles.values(), 0.5)
    BackButton = loadImage('./assets/images/BackButton.png')    
    background(37)
    size(800, 600)
    frameRate(60)
    
def draw():
    global KeyInfo, MouseInfo, MouseScroll, SoundFiles
    background(37)
    viewsModel.Show(KeyInfo, MouseInfo, SoundFiles, MainFont, ButtonFont, BackButton, BellFont)          
    audio.SetVolumeMouseScroll(SoundFiles.values(), MouseScroll)
    MouseScroll = 0
    KeyInfo["KeyReleased"] = False
    MouseInfo["MouseReleased"] = False

def keyReleased(event) :
    global KeyInfo
    KeyInfo["KeyReleased"] = True
def mouseReleased():
    MouseInfo["MouseReleased"] = True
    SoundFiles['ClickSound'].play()


def mouseWheel(event):
    global MouseScroll
    MouseScroll = event.getCount()  