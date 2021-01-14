from modules.views import splashScreen, playerAmount, playerSelection, homescreen, event
from modules.vechtModules import karakterSelection, fight, fightResult

class Screen:
    def __init__(self, showFunction, isShowing):
        self.ShowFunction = showFunction
        self.IsShowing = isShowing

    def Show(self, *args, **kwargs) :
        if self.IsShowing == True :
            self.IsShowing = self.ShowFunction(*args, **kwargs)

SplashScreen = Screen(splashScreen.Show, True)
PlayerAmount = Screen(playerAmount.Show, False)
PlayerSelection = Screen(playerSelection.Show, False)
HomeScreen = Screen(homescreen.Show, False)
KarakterSelection = Screen(karakterSelection.Show, False)
Fight = Screen(fight.Show, False)
FightResult = Screen(fightResult.Show, False)

def Show(keyInfo, mouseInfo, soundFiles, mainFont, buttonFont, backButton, bellFont, iconFont) :
    if SplashScreen.IsShowing :
        SplashScreen.Show(mainFont, buttonFont, bellFont)
        if SplashScreen.IsShowing == False :
            PlayerAmount.IsShowing = True
    elif PlayerAmount.IsShowing :
        PlayerAmount.Show(mainFont, buttonFont, bellFont)
        if PlayerAmount.IsShowing == False :
            PlayerSelection.IsShowing = True
    elif PlayerSelection.IsShowing :
        PlayerSelection.Show(playerAmount.AmountofPlayers)
        if PlayerSelection.IsShowing == False:
            HomeScreen.IsShowing = True
            homescreen.Setup(playerSelection.GekozenKarakters)
    elif HomeScreen.IsShowing :
        HomeScreen.Show(mainFont, buttonFont, mouseInfo, soundFiles, iconFont, bellFont, fight.fightCounter)
        event.TimerForEvent(backButton, bellFont)
        if HomeScreen.IsShowing == False :
            KarakterSelection.IsShowing = True
    elif KarakterSelection.IsShowing :
        KarakterSelection.Show(bellFont)
        if KarakterSelection.IsShowing == False :
            Fight.IsShowing = True
    elif Fight.IsShowing == True :
        Fight.Show(keyInfo, karakterSelection.GekozenKarakters, soundFiles)
        if Fight.IsShowing == False:
            FightResult.IsShowing = True
    elif FightResult.IsShowing == True:
        FightResult.Show(fight.victoryPlayer, soundFiles)
        if FightResult.IsShowing == False:
            HomeScreen.IsShowing = True

def Setup() :
    playerSelection.Setup()
    karakterSelection.Setup()
    fight.Setup()