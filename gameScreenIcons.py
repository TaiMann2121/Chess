from cmu_graphics import *

def drawIcons(player1 , player2, message):
    # draws menu button
    drawLabel("Press 'm' to go back to menu", 2, 6, align = 'left', size = 12, fill = 'black')
    # draw player 1 label
    drawLabel(player1.name, 25, 360, align = 'left', size = 16, fill = 'white' if player1.color == 'white' else 'black')
    # draw Player 2 Label
    drawLabel(player2.name, 25, 90, align = 'left', size = 16, fill = 'black' if player2.color  == 'black' else 'white')
    # message Box
    drawRect(100, 370, 200, 30, fill = 'white')
    drawLabel(message, 200, 385, align = 'center', fill = 'red', size = 30)

def pawnPromotion():
    pass

