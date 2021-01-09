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

def Show(keyInfo, soundFiles, mainFont, buttonFont, backButton) :
    if SplashScreen.IsShowing :
        SplashScreen.Show(mainFont, buttonFont)
        if SplashScreen.IsShowing == False :
            PlayerAmount.IsShowing = True
    elif PlayerAmount.IsShowing :
        PlayerAmount.Show(mainFont, buttonFont)
        if PlayerAmount.IsShowing == False :
            PlayerSelection.IsShowing = True
            playerSelection.Setup(playerAmount.AmountofPlayers, soundFiles)
    elif PlayerSelection.IsShowing :
        PlayerSelection.Show()
        if PlayerSelection.IsShowing == False:
            HomeScreen.IsShowing = True
    elif HomeScreen.IsShowing :
        HomeScreen.Show(mainFont, buttonFont)
        event.TimerForEvent(backButton)
        if HomeScreen.IsShowing == False :
            KarakterSelection.IsShowing = True
            karakterSelection.Setup()
    elif KarakterSelection.IsShowing :  
        KarakterSelection.Show()
        if KarakterSelection.IsShowing == False :
            Fight.IsShowing = True
            fight.Setup(karakterSelection.GekozenKarakters)
    elif Fight.IsShowing == True :
        Fight.Show(keyInfo)
        if Fight.IsShowing == False:
            FightResult.IsShowing = True
    elif FightResult.IsShowing == True:
        FightResult.Show(fight.victoryPlayer)
        if FightResult.IsShowing == False:
            HomeScreen.IsShowing = True
    


