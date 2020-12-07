from modules import vechtknop
def setup():
    # The size of the canvas
    size(800, 600)
    # Zet Achtergrond zwart
    background(0)
def draw():
    vechtknop.knop()
    print(mouseX, mouseY)
