gedrukt = False
from modules.vechtModules import karakter, vechtknop
def showVechtModule():
    global gedrukt
    if gedrukt == False:
        gedrukt = vechtknop.knop()
    if gedrukt == True:
        karakter.SelectieScherm()