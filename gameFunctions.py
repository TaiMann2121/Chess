
# checks if a sqaure is a legal selection
def isLegalSelection(player, square):
    # a selection is legal as long as the player selects a square with the same color as their color
    return player.color == square.color

# makes a move 
def makeMove(selectedSquare, moveSquare):
    # we want the square we are moving the piece to to have the piece that 
    # the selected square originally contained, then we want to set the
    # selected sqaure's piece to None, since we moved the piece
    moveSquare.piece, selectedSquare.piece = selectedSquare.piece, None
    # same idea with the square's color's
    moveSquare.color, selectedSquare.color = selectedSquare.color, None
    ### edge cases ###   #castling#

# given a selected square and a 2d list of sqaures(board), return a list of
# all the squares that the piece on the selected square can move to
def legalMoves(selectedSqaure, squares, player):
    #return [squares[5][0], squares[3][0]]
    legalSquares = []
    
    return legalSquares
