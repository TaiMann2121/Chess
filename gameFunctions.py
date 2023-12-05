from piece import *
import copy
from square import *
from functools import cache
# @cache
# checks if a sqaure is a legal selection
def isLegalSelection(player, square):
    # a selection is legal as long as the player selects a square with the same color as their color
    return player.color == square.color
# makes a move 
def makeMove(selectedSquare, moveSquare, squares, player, previousMove):
    # en passent
    initialSquareDrow = 1 if (player.name == 'player 2' or player.name == 'AI') else -1
    if isinstance(selectedSquare.piece, Pawn) and previousMove[1] == squares[selectedSquare.row][moveSquare.col] and previousMove[0] == squares[selectedSquare.row+(2*initialSquareDrow)][moveSquare.col] and isinstance(previousMove[1].piece, Pawn):
        moveSquare.piece, selectedSquare.piece = selectedSquare.piece, None
        moveSquare.color, selectedSquare.color = selectedSquare.color, None
        squares[selectedSquare.row][moveSquare.col].piece = None
        squares[selectedSquare.row][moveSquare.col].color = None
    # handle castling
    elif player.canCastle == True and isinstance(selectedSquare.piece, King) and moveSquare == squares[selectedSquare.row][selectedSquare.col+2]:
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
    # normal move
    else:
        # we want the square we are moving the piece to to have the piece that 
        # the selected square originally contained, then we want to set the
        # selected sqaure's piece to None, since we moved the piece
        moveSquare.piece, selectedSquare.piece = selectedSquare.piece, None
        # same idea with the square's color's
        moveSquare.color, selectedSquare.color = selectedSquare.color, None
    
# returns a list of all the semi legal squares a piece on the selected square can move to
# a semi legal square is a square that the piece on the selected square can move to
# but might put the player in check
def semiLegalMoves(selectedSquare, squares, player, previousMove):
    semiLegalSquares = []
    if isinstance(selectedSquare.piece, Pawn):
        semiLegalSquares = semiLegalPawnMoves(selectedSquare, squares, player, previousMove)
    elif isinstance(selectedSquare.piece, Rook):
        semiLegalSquares = semiLegalRookMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Knight):
        semiLegalSquares = semiLegalKnightMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Bishop):
        semiLegalSquares = semiLegalBishopMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, Queen):
        semiLegalSquares = semiLegalQueenMoves(selectedSquare, squares)
    elif isinstance(selectedSquare.piece, King):
        semiLegalSquares = semiLegalKingMoves(selectedSquare, squares, player.canCastle)
    return semiLegalSquares

# returns a list of all the fully legal squares, a fully legal square is semi legal square that also will
# not put the given player in check is the piece on the selected square is moved to this square
def fullyLegalMoves(selectedSquare, squares, player, previousMove, otherPlayer, semiLegalSquares):
        fullyLegalSquares = []
        squaresCopy = []
        squareRows = []
        # go through every square in semiLegalSquares
        for square in semiLegalSquares:
            # WE DO NOT want to modify anything on our board, therefore we need to create a new selectedSquare object
            # a new semiLegalSquare object for each square in semiLegalSquares, and a new board, creating new
            # square objects for each row and col of the squares list, and inserting selectedSquareCopy and 
            # semiLegalSquare copy at it's respective row and column
            # We want to re initalize these copies for every iteration through semiLegalSquares, which is why we 
            # do this inside the for loop
            ###selectedSquareCopy = Square(selectedSquare.piece, selectedSquare.row, selectedSquare.col, selectedSquare.color)
            ###semiLegalSquareCopy = Square(square.piece, square.row, square.col, square.color)
            for row in range(len(squares)):
                for col in range(len(squares[0])):
                    squareRows.append(Square(squares[row][col].piece, squares[row][col].row, squares[row][col].col, squares[row][col].color))
                squaresCopy.append(squareRows)
                squareRows = []
            # make the move on this copied board
            makeMove(squaresCopy[selectedSquare.row][selectedSquare.col], squaresCopy[square.row][square.col], squaresCopy, player, previousMove)
            # if we make this move and the player is not in check, then this square is a fullyLegalSquare and 
            # therefore we append it to the fullyLegalSquares list
            if not inCheck(player, squaresCopy, otherPlayer, previousMove):
                fullyLegalSquares.append(square)
            # reset board
            squaresCopy = []
        return fullyLegalSquares

def semiLegalPawnMoves(selectedSquare, squares, player, previousMove):
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
        if rowCheck < len(squares) and squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
        # check if it can attack, rowCheck stays row + 1  and colCheck will either
        # be col + 1 or col - 1 
        directions = [-1, 1]
        for dcol in directions:
            colCheck = col + dcol
            if rowCheck < len(squares) and colCheck >= 0 and colCheck < len(squares[0]):
                if squares[rowCheck][colCheck].piece != None and squares[rowCheck][colCheck].color != selectedSquare.color:
                    legalSquares.append(squares[rowCheck][colCheck])
                # en passent
                if selectedSquare.row == 4:
                    if previousMove[0] == squares[row+2][colCheck] and previousMove[1] == squares[row][colCheck] and isinstance(previousMove[1].piece, Pawn) and squares[rowCheck][colCheck].piece == None:
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
        if rowCheck >= 0 and squares[rowCheck][col].piece == None:
            legalSquares.append(squares[rowCheck][col])
        # check if it can attack, rowCheck stays row - 1  and colCheck will either
        # be col + 1 or col - 1 
        directions = [-1, 1]
        for dcol in directions:
            colCheck = col + dcol
            if rowCheck >= 0 and colCheck >= 0 and colCheck < len(squares[0]):
                if squares[rowCheck][colCheck].piece != None and squares[rowCheck][colCheck].color != selectedSquare.color:
                    legalSquares.append(squares[rowCheck][colCheck])
                # en passent
                if selectedSquare.row == 3:
                    if previousMove[0] == squares[row-2][colCheck] and previousMove[1] == squares[row][colCheck] and isinstance(previousMove[1].piece, Pawn) and squares[rowCheck][colCheck].piece == None:
                        legalSquares.append(squares[rowCheck][colCheck])

    return legalSquares

def semiLegalRookMoves(selectedSquare, squares):
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

def semiLegalKnightMoves(selectedSquare, squares):
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

def semiLegalBishopMoves(selectedSquare, squares):
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

def semiLegalQueenMoves(selectedSquare, squares):
    legalSquares = semiLegalRookMoves(selectedSquare, squares) + semiLegalBishopMoves(selectedSquare, squares)
    return legalSquares

def semiLegalKingMoves(selectedSquare, squares, canCastle):
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
    
def inCheck(playerInQuestion, squares, playerAttacking, previousMove):
    kingSquare = findKing(playerInQuestion, squares)
    for row in range(len(squares)):
        for col in range(len(squares[0])):
            if squares[row][col].color == playerAttacking.color:
                if kingSquare in semiLegalMoves(squares[row][col], squares, playerAttacking, previousMove):
                    return True
    return False

def inCheckmate(playerInQuestion, squares, playerAttacking, previousMove):
    allFullyLegalSquares = []
    for row in range(len(squares)):
        for col in range(len(squares[0])):
            if squares[row][col].color == playerInQuestion.color:
                semiLegalSquares = semiLegalMoves(squares[row][col], squares, playerInQuestion, previousMove)
                fullyLegalSquares = fullyLegalMoves(squares[row][col], squares, playerInQuestion, previousMove, playerAttacking, semiLegalSquares)
                allFullyLegalSquares.extend(fullyLegalSquares)
    #if playerInQuestion.color == 'white':
        #print(f'allFullyLegalSquares: {allFullyLegalSquares}')
        #print(f'Is in check: {inCheck(playerInQuestion, squares, playerAttacking, previousMove)}')
    if len(allFullyLegalSquares) == 0 and inCheck(playerInQuestion, squares, playerAttacking, previousMove):
        return True 
    else:
        return False

def findKing(player, squares):
    for row in range(len(squares)):
        for col in range(len(squares[0])):
            if isinstance(squares[row][col].piece, King) and squares[row][col].color == player.color:
                return squares[row][col]