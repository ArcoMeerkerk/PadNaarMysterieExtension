soundPlayed = False
def Show(victoryPlayer, soundFiles):
    global soundPlayed
    SoundFiles = soundFiles
    background(37)
    if soundPlayed == False:
        SoundFiles['VictorySound'].play()
        SoundFiles['VictoryMusic'].play()
        soundPlayed = True
    textAlign(CENTER)
    textSize(86)
    text('Victory', 400, 150)
    fill(255)
    textSize(55)
    text('Speler ' + str(victoryPlayer) + ' heeft gewonnen', 402, 284)
    fill('#808080')
    # Terug knop
    rectMode(CORNER)  
    rect(298, 419, 206, 55)
    fill(255)
    textSize(16)
    textAlign(CENTER)
    text("Terug naar Homescreen", 400, 448)
    if mousePressed and mouseX > 298 and mouseX < (298 + 206) and mouseY > 419 and mouseY < (419 + 55):
        soundPlayed = False
        SoundFiles['VictoryMusic'].stop()
        return False
    return True