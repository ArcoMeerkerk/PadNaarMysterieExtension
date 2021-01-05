from modules.views import splashScreen, playerAmount, playerSelection, homescreen, event
from modules.vechtModules import vechtModule

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
VechtModule = Screen(vechtModule.Show, False)

def Show(mainFont, buttonFont, backButton) :
    # PlayerSelection.Show(mainFont, titleFont)

    if SplashScreen.IsShowing :
        SplashScreen.Show(mainFont, buttonFont)
        if SplashScreen.IsShowing == False :
            PlayerAmount.IsShowing = True
    elif PlayerAmount.IsShowing :
        PlayerAmount.Show(mainFont, buttonFont)
        if PlayerAmount.IsShowing == False :
            HomeScreen.IsShowing = True
    elif HomeScreen.IsShowing :
        HomeScreen.Show(mainFont, buttonFont)
        event.TimerForEvent(backButton)
        if HomeScreen.IsShowing == False :
            VechtModule.IsShowing = True
    elif VechtModule.IsShowing :
        VechtModule.Show()
        if VechtModule.IsShowing == False :
            HomeScreen.IsShowing = True
