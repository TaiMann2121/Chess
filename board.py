from cmu_graphics import *
# board class
class Board:
    def __init__(self):
        self.rows, self.cols = 8, 8
        self.boardLeft, self.boardTop = 25, 100
        self.boardWidth, self.boardHeight = 250, 250
        self.cellBorderWidth = 1
# draw board
def drawBoard(board):
    for row in range(board.rows):
        for col in range(board.cols):
            drawCell(board, row, col)
# draws each cell
def drawCell(board, row, col):
    cellLeft, cellTop = getCellLeftTop(board, row, col)
    cellWidth, cellHeight = getCellSize(board, row, col)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight, fill = 'gainsboro' if (row-col)%2 == 0 else 'lightSkyBlue', 
            border = 'black', borderWidth = board.cellBorderWidth)
# gets a cell's top left coordinate
def getCellLeftTop(board, row, col):
    cellWidth, cellHeight = getCellSize(board, row, col)
    cellLeft = board.boardLeft + col * cellWidth
    cellTop = board.boardTop + row * cellHeight
    return (cellLeft, cellTop)
# gets a cell's size
def getCellSize(board, row, col):
    cellWidth = board.boardWidth / board.cols
    cellHeight = board.boardHeight / board.rows
    return (cellWidth, cellHeight)
# draws border
def drawBorder(app, board):
    drawRect(board.boardLeft, board.boardTop,
             board.boardWidth, board.boardHeight, 
             fill = None, border = 'black', borderWidth = 2*board.cellBorderWidth)
# gets cells center
def getCellCenter(board, row, col):
    cellLeft, cellTop = getCellLeftTop(board, row, col)
    cellCx = cellLeft + ((board.boardWidth / board.cols) / 2)
    cellCy = cellTop + ((board.boardHeight / board.rows) / 2)
    return (cellCx, cellCy)
    

