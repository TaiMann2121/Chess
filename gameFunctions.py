from piece import *
# checks if a sqaure is a legal selection
def isLegalSelection(player, square):
    # a selection is legal as long as the player selects a square with the same color as their color
    return player.color == square.color
# makes a move 
def makeMove(selectedSquare, moveSquare, squares, player):
    # handle castling
    
    if player.canCastle == True and isinstance(selectedSquare.piece, King) and moveSquare == squares[selectedSquare.row][selectedSquare.col+2]:
        # row and col of king 
        row = selectedSquare.row
        col = selectedSquare.col
        # moves king
        squares[row][col+2].piece = selectedSquare.piece
        squares[row][col+2].color = selectedSquare.color
        selectedSquare.piece = None
        selectedSquare.color = None
        # moves rook
        squares[row][col+1].piece = squares[row][col+3].piece
        squares[row][col+1].color = squares[row][col+3].color
        squares[row][col+3].piece = None
        squares[row][col+3].color = None
        # player already castled so player.canCastle is now None
        player.canCastle = None 
    # normal move
    else:
        # we want the square we are moving the piece to to have the piece that 
        # the selected square originally contained, then we want to set the
        # selected sqaure's piece to None, since we moved the piece
        moveSquare.piece, selectedSquare.piece = selectedSquare.piece, None
        # same idea with the square's color's
        moveSquare.color, selectedSquare.color = selectedSquare.color, None
    
# given a selected square and a 2d list of sqaures(board), return a list of
# all the squares that the piece on the selected square can move to
def legalMoves(selectedSquare, squares, player):
    if isinstance(selectedSquare.piece, Pawn):
        return legalPawnMoves(selectedSquare, squares, player)
    elif isinstance(selectedSquare.piece, Rook):
        return legalRookMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Knight):
        return legalKnightMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Bishop):
        return legalBishopMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Queen):
        return legalQueenMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, King):
        return legalKingMoves(selectedSquare, squares, player.canCastle)
    
def legalPawnMoves(selectedSquare, squares, player):
    legalSquares = []
    row = selectedSquare.row
    col = selectedSquare.col
    # top of board
    if player.name == 'player 2' or player.name == 'AI':
        # if pawn is at starting position, we need to check if it can move up 2 rows
        if row == 1:
            rowCheck = row + 2
            if squares[rowCheck][col].piece == None:
                legalSquares.append(squares[rowCheck][col])
        # check if it can move up 1 row
        rowCheck = row + 1
        if squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
        # check if it can attack, rowCheck stays row + 1  and colCheck will either
        # be col + 1 or col - 1 
        directions = [-1, 1]
        for dcol in directions:
            colCheck = col + dcol
            if colCheck >= 0 and colCheck < len(squares[0]):
                if squares[rowCheck][colCheck].piece != None and squares[rowCheck][colCheck].color != selectedSquare.color:
                    legalSquares.append(squares[rowCheck][colCheck])
    # bottom of board
    else:
        # if pawn is at starting position, we need to check if it can move up 2 rows
        if row == 6:
            rowCheck = row - 2
            if squares[rowCheck][col].piece == None:
                legalSquares.append(squares[rowCheck][col])
        # check if it can move up 1 row
        rowCheck = row - 1
        if squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
        # check if it can attack, rowCheck stays row - 1  and colCheck will either
        # be col + 1 or col - 1 
        directions = [-1, 1]
        for dcol in directions:
            colCheck = col + dcol
            if colCheck >= 0 and colCheck < len(squares[0]):
                if squares[rowCheck][colCheck].piece != None and squares[rowCheck][colCheck].color != selectedSquare.color:
                    legalSquares.append(squares[rowCheck][colCheck])

    return legalSquares

def legalRookMoves(selectedSquare, squares):
    legalSquares = []
    row = selectedSquare.row
    col = selectedSquare.col

    # left/right directions
    
    # left
    colCheck = col - 1
    while colCheck >= 0:
        if squares[row][colCheck].piece == None:
            legalSquares.append(squares[row][colCheck])
            colCheck -= 1
        elif squares[row][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[row][colCheck])
            break
        else:
            break
    # right
    colCheck = col + 1
    while colCheck < len(squares[0]):
        if squares[row][colCheck].piece == None:
            legalSquares.append(squares[row][colCheck])
            colCheck += 1
        elif squares[row][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[row][colCheck])
            break
        else:
            break
    
    # up/down directions

    # down the board
    rowCheck = row + 1 
    while rowCheck < len(squares):
        if squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
            rowCheck += 1
        elif squares[rowCheck][col].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][col])
            break
        else:
            break
    # up the board
    rowCheck = row - 1
    while rowCheck >= 0:
        if squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
            rowCheck -= 1
        elif squares[rowCheck][col].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][col])
            break
        else:
            break
    return legalSquares

def legalKnightMoves(selectedSquare, squares):
    legalSquares = []
    row = selectedSquare.row
    col = selectedSquare.col
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    for drow, dcol in directions:
        rowCheck = row + drow
        colCheck = col + dcol
        if rowCheck >=0 and rowCheck < len(squares) and colCheck >= 0 and colCheck < len(squares[0]):
            if squares[rowCheck][colCheck].piece == None or squares[rowCheck][colCheck].color != selectedSquare.color:
                legalSquares.append(squares[rowCheck][colCheck])
    return legalSquares

def legalBishopMoves(selectedSquare, squares):
    legalSquares = []
    row = selectedSquare.row
    col = selectedSquare.col
    # up-right diagonal
    rowCheck = row - 1
    colCheck = col + 1
    while rowCheck >= 0 and colCheck < len(squares[0]):
        if squares[rowCheck][colCheck].piece == None:
            legalSquares.append(squares[rowCheck][colCheck])
            rowCheck -= 1 
            colCheck +=1
        elif squares[rowCheck][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][colCheck])
            break
        else:
            break
    # up-left diagonal
    rowCheck = row - 1
    colCheck = col - 1
    while rowCheck >= 0 and colCheck >= 0:
        if squares[rowCheck][colCheck].piece == None:
            legalSquares.append(squares[rowCheck][colCheck])
            rowCheck -= 1 
            colCheck -=1
        elif squares[rowCheck][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][colCheck])
            break
        else:
            break
    # down-right diagonal
    rowCheck = row + 1
    colCheck = col + 1
    while rowCheck < len(squares) and colCheck < len(squares[0]):
        if squares[rowCheck][colCheck].piece == None:
            legalSquares.append(squares[rowCheck][colCheck])
            rowCheck += 1 
            colCheck +=1
        elif squares[rowCheck][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][colCheck])
            break
        else:
            break
    # down-left diagonal
    rowCheck = row + 1
    colCheck = col - 1
    while rowCheck < len(squares) and colCheck >= 0:
        if squares[rowCheck][colCheck].piece == None:
            legalSquares.append(squares[rowCheck][colCheck])
            rowCheck += 1 
            colCheck -=1
        elif squares[rowCheck][colCheck].color != selectedSquare.color:
            legalSquares.append(squares[rowCheck][colCheck])
            break
        else:
            break
    return legalSquares

def legalQueenMoves(selectedSquare, squares):
    legalSquares = legalRookMoves(selectedSquare, squares) + legalBishopMoves(selectedSquare, squares)
    return legalSquares

def legalKingMoves(selectedSquare, squares, canCastle):
    legalSquares = []
    row = selectedSquare.row
    col = selectedSquare.col
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for drow, dcol in directions:
        rowCheck = row + drow
        colCheck = col + dcol
        if rowCheck >=0 and rowCheck < len(squares) and colCheck >= 0 and colCheck < len(squares[0]):
            if squares[rowCheck][colCheck].piece == None or squares[rowCheck][colCheck].color != selectedSquare.color:
                legalSquares.append(squares[rowCheck][colCheck])
    # castling
    if canCastle:
        legalSquares.append(squares[row][col+2])
    return legalSquares

# canCastle = False when player player can't castle now but still can
# canCastle = True when the player can castle
# canCastle = None when either the player has either already castled or made a move that made it illegal for them to castle
def updateCanCastle(player, squares):
    # top of the board
    if player.name == 'player 2' or player.name == 'AI':
        # if the player moved their king or their right rook, player can no longer castle
        if squares[0][4].piece == None or squares[0][7].piece == None:
            return None
        # if these one of these squares was already empty and the other was just moved
        # the player can now Castle
        elif squares[0][5].piece == None and squares[0][6].piece == None:
            return True
        else:
            return False
    # bottom of the board
    else:
        # if the player moved their king or their right rook, player can no longer castle
        if squares[7][4].piece == None or squares[7][7].piece == None:
            return None
        # if one of these squares was already empty and the other was just moved
        # the player can now Castle
        elif squares[7][5].piece == None and squares[7][6].piece == None:
            return True
        else:
            return False
    