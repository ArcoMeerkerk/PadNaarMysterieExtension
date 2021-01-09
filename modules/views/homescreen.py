import glob
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
        if PdfViewerWindowScreen == None :
            this.surface.setLocation(displayWidth - width * 2 - 20, displayHeight // 2 - height // 2)
            PdfViewerWindowScreen = pdfViewer.PdfViewerWindow([loadImage(pageFile) for pageFile in glob.glob("./assets/pdf/handleiding/Page-*.png")], fonts["IconFont"])
        else :
            PdfViewerWindowScreen.getSurface().setVisible(True)

    return not ShowButton(fonts["IconFont"], u"\uf441", fonts["ButtonFont"], "VECHT", 75, 50, 300)

def ShowButton(iconFont, icon, buttonFont, buttonText, bottomMargin, buttonHeight, buttonWidth) :
    fill(0)
    rectMode(CENTER)
    rect(width//2, height-bottomMargin, buttonWidth, buttonHeight)
    fill(255)
    # textAlign(CENTER)
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