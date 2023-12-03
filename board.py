from cmu_graphics import *
# board class
class Board:
    def __init__(self):
        self.rows, self.cols = 8, 8
        self.boardLeft, self.boardTop = 25, 100
        self.boardWidth, self.boardHeight = 250, 250
# draws board border
def drawBorder(board):
    drawRect(board.boardLeft, board.boardTop,
             board.boardWidth, board.boardHeight, 
             fill = None, border = 'black', borderWidth = 2)   

