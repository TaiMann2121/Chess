from cmu_graphics import *

# function that draws the menu
def drawMenu():
    drawLabel('112 Chess!', app.width/2 , 40, size = 50, font = 'ariel', fill = 'black')
    # draws the two player button
    drawRect(100, 125, 200, 100, fill = 'saddleBrown')
    drawLabel('Two Player', 200, 175, size = 30, fill = 'black')
    # draws single player button
    drawRect(100, 250, 200, 100, fill = 'saddleBrown')
    drawLabel('Single Player', 200, 300, size = 30, fill = 'black')
def drawAIMenuScreen():
    drawLabel('112 Chess!', app.width/2 , 40, size = 50, font = 'ariel', fill = 'black')
    # play/or
    drawLabel('Play', 200, 113, size = 20, fill = 'black')
    drawLabel('Or', 200, 238, size = 20, fill = 'black')
    # white
    drawRect(100, 125, 200, 100, fill = 'white')
    drawLabel('White', 200, 175, size = 30, fill = 'black', bold = True)
    # black
    drawRect(100, 250, 200, 100, fill = 'black')
    drawLabel('Black', 200, 300, size = 30, fill = 'white', bold = True)
