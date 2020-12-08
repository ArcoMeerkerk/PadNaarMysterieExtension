from modules.vechtModules import vechtModule
def setup():
    # The size of the canvas
    size(800, 600)
    # Zet Achtergrond zwart
    background(35)
def draw():
    vechtModule.showVechtModule()                               