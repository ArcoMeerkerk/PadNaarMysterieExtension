def ShowStartingPos():
    #[(570, 147, 50, 50), (570, 315, 50, 50), (275, 315, 50, 50), (275, 142, 50, 50), (425, 65, 50, 50), (425, 399.0, 50, 50), None]
    #[(processing.core.PImage@cd16430, 3), (processing.core.PImage@66dda403, 4), (processing.core.PImage@5f304d3b, 6), (processing.core.PImage@592ad14c, 5), (processing.core.PImage@5e5ddebd, 1)]
    for i in range(len(CharacterImages)):
        image(CharacterImages[i][0],CharacterCoordinates[CharacterImages[i][1]][0],CharacterCoordinates[CharacterImages[i][1]][1],CharacterCoordinates[CharacterImages[i][1]][2],CharacterCoordinates[CharacterImages[i][1]][3])

