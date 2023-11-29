from cmu_graphics import *

# function that draws the menu
def drawMenu():
    # draws the two player button
    drawRect(100, 125, 200, 100, fill = 'saddleBrown')
    drawLabel('Two Player', 200, 175, size = 30, fill = 'black')
    # draws single player button
    drawRect(100, 250, 200, 100, fill = 'saddleBrown')
    drawLabel('Single Player', 200, 300, size = 30, fill = 'black')
