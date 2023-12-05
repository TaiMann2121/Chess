from cmu_graphics import *
from square import *
def drawIcons(player1 , player2, message):
    # draws menu button
    drawLabel("Press 'm' to go back to menu", 2, 8, align = 'left', size = 16, fill = 'black')
    # turns
    if player1.isTurn == True:
        drawRect(50, 350, 60, 20, fill = 'lime')
    else:
        if player2.isAI == False:
            drawRect(50, 30, 60, 20, fill = 'lime')
        else:
            drawRect(50, 30, 20, 20, fill = 'lime')
    # draw player 1 label
    drawLabel(player1.name, 50, 360, align = 'left', size = 16, fill = 'white' if player1.color == 'white' else 'black', bold = True)
    # draw Player 2 Label
    drawLabel(player2.name, 50, 40, align = 'left', size = 16, fill = 'black' if player2.color  == 'black' else 'white', bold = True)
    
    # message Box
    drawRect(0, 375, 400, 30, fill = 'white')
    drawLabel(message, 200, 387, align = 'center', fill = 'red', size = 27)

def drawPawnPromotion(board, squares):
    for square in squares:
        drawSquare(board, square, None, None)
    
def getPromotedSquare(board, squares, mouseX, mouseY):
    return getSquare(squares, board, mouseX, mouseY)

