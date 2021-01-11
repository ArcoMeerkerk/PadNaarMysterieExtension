from modules import audio, cursor
from modules.views import viewsModel, splashScreen, playerAmount, homescreen
from modules.vechtModules import vechtModule
add_library("sound")

MouseScroll = 0
Fonts = {
    "MainFont": loadFont("./assets/fonts/Algerian-64.vlw"),
    "ButtonFont": loadFont("./assets/fonts/ArialMT-32.vlw"),
    "IconFont": loadFont("./assets/fonts/FontAwesome/FontAwesome5Free-Solid-128.vlw")
}

def setup():
    background(255)
    size(800, 600)
    this.surface.setTitle("Pad naar Mysterie uitbreiding")
    frameRate(60)
    
    cursor.Setup()
    vechtModule.Setup()
    
def draw():
    global MouseScroll

    background(255)
    cursor.Show()
    viewsModel.Show(Fonts)          

    # audio.MouseEffect([Sf1, Sf2])
    # audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)

    MouseScroll = 0

# def keyPressed():
# def keyReleased():

def mouseWheel(event):
    global MouseScroll
    MouseScroll = event.getCount()
