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
# square class
class Square:
    def __init__(self, piece, row, col, color):
        self.piece = piece
        self.row = row
        self.col = col
        self.color = color
# draw square
def drawSquare(board, square):
    squareLeft, squareTop = getSquareLeftTop(board, square.row, square.col)
    squareWidth, squareHeight = getSquareSize(board)
    drawRect(squareLeft, squareTop, squareWidth, squareHeight, 
             fill = 'gainsboro' if (square.row-square.col)%2 == 0 else 'lightSkyBlue',
             border = 'black', borderWidth = 1)
    if square.piece != None:
        centerX, centerY = getSquareCenter(board, square.row, square.col)
        drawImage(square.piece.image, centerX, centerY, align = 'center')
# get square left top
def getSquareLeftTop(board, row, col):
    squareWidth, squareHeight = getSquareSize(board)
    squareLeft = board.boardLeft + col * squareWidth
    squareTop = board.boardTop + row * squareHeight
    return (squareLeft, squareTop)
# get square size
def getSquareSize(board):
    squareWidth = board.boardWidth / board.cols
    squareHeight = board.boardHeight / board.rows
    return (squareWidth, squareHeight)
# get square center
def getSquareCenter(board, row, col):
    squareLeft, squareTop = getSquareLeftTop(board, row, col)
    squareCx = squareLeft + ((board.boardWidth / board.cols) / 2)
    squareCy = squareTop + ((board.boardHeight / board.rows) / 2)
    return (squareCx, squareCy)
    

