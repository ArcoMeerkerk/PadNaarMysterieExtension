from modules import audio
from modules.vechtModules import vechtModule
from modules.views import splashScreen, playerAmount
# add_library("sound")

# MouseScroll = 0
# IsShowingSplashScreen = True
# IsShowingPlayerAmount = False

def setup():
    global Font, Sf1, Sf2
    # Sf1 = SoundFile(this, "./assets/audio/piano.wav")
    # Sf2 = SoundFile(this, "./assets/audio/hertz.wav")
    # Font = loadFont("./assets/fonts/AventineRegular-64.vlw")
    # Font = loadFont("./assets/fonts/Algerian-64.vlw") 
    # audio.SetVolume([Sf1, Sf2], [0.5, 0.5])
    background(35)
    size(800, 600)
    frameRate(60)               
    # Sf1.play()
    
def draw():
    global MouseScroll, IsShowingSplashScreen, IsShowingPlayerAmount
    # Disabled main screen
    # if IsShowingSplashScreen :                
    #     IsShowingSplashScreen = splashScreen.Show(Font)   

    #     if IsShowingSplashScreen == False :
    #         IsShowingPlayerAmount = True
    # elif IsShowingPlayerAmount :
    #     IsShowingPlayerAmount = playerAmount.Show(Font)         

    vechtModule.showVechtModule()               

    # audio.MouseEffect([Sf1, Sf2])
    # audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)

    # MouseScroll = 0

# def keyPressed():
# def keyReleased():

# def mouseWheel(event):
#     global MouseScroll
#     MouseScroll = event.getCount()    