from cmu_graphics import *
# board class
class Board:
    def __init__(self):
        self.rows, self.cols = 8, 8
        self.boardLeft, self.boardTop = 25, 100
        self.boardWidth, self.boardHeight = 250, 250
class PromotionBoard:
    def __init__(self, rows, cols, boardLeft,  boardTop, boardWidth, boardHeight):
        self.rows = rows
        self.cols = cols
        self.boardLeft = boardLeft
        self.boardTop = boardTop
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
# draws board border
def drawBorder(board):
    drawRect(board.boardLeft, board.boardTop,
             board.boardWidth, board.boardHeight, 
             fill = None, border = 'black', borderWidth = 2)   

