def MouseEffect(sf) :
    if mousePressed  :
        sf[0].stop()
        if not sf[1].isPlaying() :
            sf[1].play()
    else :
        sf[1].stop()
        # if not sf[0].isPlaying() :
        #     sf[0].play()

def SetVolumeMouseScroll(sf, mouseScroll) :
    global SfGain
    # for i, sfGainItem in enumerate(sf) :
    if mouseScroll == 1 :
        if SfGain > 0.2 :
            SfGain -= 0.1
    elif mouseScroll == -1 :
        if SfGain <= 0.9 :
            SfGain += 0.1
    SetVolume(sf, SfGain)

def SetVolume(sf, sfGain) :
    global SfGain
    SfGain = sfGain

    for i, sfGainItem in enumerate(sf) :
        sfGainItem.amp(round(sfGain, 1))