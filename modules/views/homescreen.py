import glob
from modules.screen import SetScreenLocation
from modules.screen import GetWindowLocation
from modules.views import pdfViewer

IconFont = None
PdfViewerWindowScreen = None

def Show(fonts) :
    global PdfViewerWindowScreen
    textFont(fonts["MainFont"])
    fill(0)
    textAlign(CENTER)               
    text("Homescreen", width//2, 150)
    
    if ShowButton(fonts["IconFont"], u"\uf02d", fonts["ButtonFont"], "Handleiding", 300, 50, 300) :
        # print(PdfViewerWindowScreen.IsVisable)
        if PdfViewerWindowScreen == None :
            PdfViewerWindowScreen = pdfViewer.PdfViewerWindow([loadImage(pageFile) for pageFile in glob.glob("./assets/pdf/handleiding/Page-*.png")],
            fonts["IconFont"],
            loadImage("./assets/images/icons/document.png"),
            GetWindowLocation(this))
            SetScreenLocation(this)
        elif PdfViewerWindowScreen.IsVisable == False :
            PdfViewerWindowScreen.getSurface().setVisible(True)
            PdfViewerWindowScreen.SetWindowLocation(SetScreenLocation(this))

    return not ShowButton(fonts["IconFont"], u"\uf441", fonts["ButtonFont"], "VECHT", 75, 50, 300)

def ShowButton(iconFont, icon, buttonFont, buttonText, bottomMargin, buttonHeight, buttonWidth) :
    fill(0)
    rectMode(CENTER)
    rect(width//2, height-bottomMargin, buttonWidth, buttonHeight)
    fill(255)
    textSize(32)
    textFont(buttonFont)
    text(buttonText, width//2, height-bottomMargin+10)
    fill(200)
    textFont(iconFont)
    text(icon, width//2, height-bottomMargin+10)

    if mousePressed and mouseButton == LEFT and \
        mouseX > width//2 - buttonWidth//2 and mouseX < width//2 + buttonWidth//2 and \
        mouseY > height-bottomMargin - buttonHeight//2 and mouseY < height-bottomMargin + buttonHeight//2:
        return True
    else :
        return False
