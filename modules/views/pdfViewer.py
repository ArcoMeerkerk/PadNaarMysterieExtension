from modules import button, cursor

IsVisable = False

class PdfViewerWindow(PApplet):
    IsExited = False
    Pages = None
    CurrentPage = 0
    IconFont = None
    MouseReleased = False
    Margin = 25
        
    def __init__(self, pages, iconFont, logo, windowLocation):
        PApplet.runSketch(('--sketch-path=' + sketchPath(), ''), self)
        self.surface.setTitle("Handleiding")
        self.SetWindowLocation(windowLocation)
        self.surface.setIcon(logo)
        self.Pages = pages
        self.IconFont = iconFont
        self.IsVisable = True
        cursor.Setup()
        
    def settings(self):
        self.size(800, 1000)

    def draw(self):
        cursor.Show(self)
        if self != None and self.Pages != None and self.IconFont != None and len(self.Pages) != None and not self.IsExited :
            self.background(255)
            self.textFont(self.IconFont)

            self.image(self.Pages[self.CurrentPage], 0,0)

            # Left button
            if self.CurrentPage > 0 :
                if button.circleButton(self, self.Margin, self.height - self.Margin, self.Margin) : self.CurrentPage -= 1
                self.fill(255)
                self.textSize(50)
                self.text(u"\uf0d9", self.Margin - 6, self.height - self.Margin + 10)

            # Right button
            if self.CurrentPage < len(self.Pages) - 1:
                if button.circleButton(self, self.width - self.Margin, self.height - self.Margin, self.Margin) : self.CurrentPage += 1
                self.textFont(self.IconFont)
                self.fill(255)
                self.textSize(50)
                self.text(u"\uf0da", self.width - self.Margin - 2, self.height - self.Margin + 10)

            self.MouseReleased = False

    def SetWindowLocation(self, windowLocation) :
        posx = windowLocation[0][0] + windowLocation[1][0] - self.width - 14
        posy = 5 + windowLocation[1][1]
        self.surface.setLocation(posx, posy)

    def exit(self):
        self.IsVisable = False
        pass

    def mouseReleased(self, mouseEvent) :
        self.MouseReleased = True