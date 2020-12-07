gedrukt = False
def knop():
    global gedrukt
    if gedrukt == False:
        # Rechthoek
        fill(255)
        rect(300, 500, 200, 50)
        # Vecht
        fill(0)
        textSize(32)
        textAlign(CENTER)
        text("VECHT", 400, 540)
        if mousePressed:
            if (mouseX > 300 and mouseX < (300 + 200) and mouseY > 500 and mouseY < (500 + 50)):
                background(0)
                gedrukt = True