from modules import audio, splashScreen
add_library("sound")

MouseScroll = 0
Start = True

def setup():
    global Font, Sf1, Sf2
    Sf1 = SoundFile(this, "./assets/audio/piano.wav")
    Sf2 = SoundFile(this, "./assets/audio/hertz.wav")
    # Font = loadFont("./assets/fonts/AventineRegular-64.vlw")
    Font = loadFont("./assets/fonts/Algerian-64.vlw")
    audio.SetVolume([Sf1, Sf2], [0.5, 0.5])

    background(255)
    size(800, 600)
    
    Sf1.play()
    
def draw():
    global MouseScroll, IsShowingSplashScreen

    background(255)

    if IsShowingSplashScreen :
        IsShowingSplashScreen = splashScreen.Show(Font)

    audio.MouseEffect([Sf1, Sf2])
    audio.SetVolumeMouseScroll([Sf1, Sf2], MouseScroll)

    MouseScroll = 0

# def keyPressed():
# def keyReleased():

def mouseWheel(event):
    global MouseScroll
    MouseScroll = event.getCount()