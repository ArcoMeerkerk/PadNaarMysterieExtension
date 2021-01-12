soundPlayed = False
def Show(victoryPlayer, soundFiles):
    global soundPlayed
    SoundFiles = soundFiles
    background(37)
    if soundPlayed == False:
        SoundFiles['VictorySound'].play()
        SoundFiles['VictoryMusic'].play()
        soundPlayed = True
    fill('#C69C6D')
    textAlign(CENTER)
    textSize(86)
    text('Victory', 400, 150)
    textSize(55)
    text('Speler ' + str(victoryPlayer) + ' heeft gewonnen', 402, 284)
    # Terug knop
    rectMode(CENTER)  
    rect(400, 442, 270, 44, 12)
    fill(255)
    textSize(24)
    textAlign(CENTER)
    text("Terug naar Homescreen", 400, 448)
    if mousePressed and mouseX > 298 and mouseX < (298 + 206) and mouseY > 419 and mouseY < (419 + 55):
        soundPlayed = False
        SoundFiles['VictoryMusic'].stop()
        return False
    return True