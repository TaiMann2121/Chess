from board import *
import math

# draws each piece
def drawPieces(board, player):
    for piece in player.pieces:
        for square in player.pieces[piece]:
            centerX, centerY = getCellCenter(board, square[0], square[1])
            drawImage(piece, centerX, centerY, align = 'center')

# gets square on board given mouseX and mouseY
def getSquare(board, mouseX, mouseY):
    if mouseX < board.boardLeft or mouseX > (board.boardLeft + board.boardWidth) or mouseY < board.boardTop or mouseY > (board.boardTop + board.boardHeight):
        return None
    else:
        cellWidth = board.boardWidth / board.cols
        cellHeight = board.boardHeight / board.rows
        print(cellWidth, cellHeight)
        col = math.floor((mouseX - board.boardLeft) / cellWidth)
        row = math.floor((mouseY - board.boardTop) / cellHeight)
        return (row, col)