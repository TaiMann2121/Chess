from cmu_graphics import *
from piece import *
from board import *
from menus import *
from player import *
from gameScreenIcons import *
from square import *
from gameFunctions import *
from PIL import Image

def onAppStart(app):
    # importing piece images
    # black piece images
    app.blackPawnImg = CMUImage(Image.open('Black_Pawn.png'))
    app.blackRookImg = CMUImage(Image.open('Black_Rook.png'))
    app.blackBishopImg = CMUImage(Image.open('Black_Bishop.png'))
    app.blackKnightImg = CMUImage(Image.open('Black_Knight.png'))
    app.blackQueenImg = CMUImage(Image.open('Black_Queen.png'))
    app.blackKingImg = CMUImage(Image.open('Black_King.png'))
    # white piece images
    app.whitePawnImg = CMUImage(Image.open('White_Pawn.png'))
    app.whiteRookImg = CMUImage(Image.open('White_Rook.png'))
    app.whiteBishopImg = CMUImage(Image.open('White_Bishop.png'))
    app.whiteKnightImg = CMUImage(Image.open('White_Knight.png'))
    app.whiteQueenImg = CMUImage(Image.open('White_Queen.png'))
    app.whiteKingImg = CMUImage(Image.open('White_King.png'))
    # reset
    reset(app)
# reset function
def reset(app):
    # show menu starts off as true
    app.showMenu = True
    # show AI screen starts off as False
    app.showAIMenuScreen = False
    # creates board
    app.board = Board()
    app.squares = []
    # initializes players
    app.player1 = Player('white', True, False, 'player 1', False)
    app.player2  = Player('black', False, False, 'player 2', False)
    # selected square starts at None
    app.selectedSquare = None
    # current square starts at None
    app.currentSquare = None
    # message
    app.message = ''
    # prevous move (Square at inital position, square at final position)
    app.initialSquare = None
    app.finalSquare = None
    app.previousMove = (app.initialSquare, app.finalSquare)
    # show pawn promotion screen
    app.showPawnPromotion = False
    app.pawnPromotionBoard = None
    app.pawnPromotionSquares = []
    # gameOver starts as False
    app.gameOver = False
    # legalSquares
    app.semiLegalSquares = []
    app.fullyLegalSquares = []
# redrawAll function
def redrawAll(app):
    # background and title
    drawRect(0, 0, app.width, app.height, fill = 'burlyWood')
    if app.showMenu: # we are in menu
        drawMenu()
    elif app.showAIMenuScreen: # we are in AI menu
        drawAIMenuScreen()
    else: # we are in Game
        # Icons
        drawIcons(app.player1, app.player2, app.message)
        # draws border
        drawBorder(app.board)
        # draws all the squares
        for row in range(len(app.squares)):
            for col in range(len(app.squares[0])):
                drawSquare(app.board, app.squares[row][col], app.selectedSquare, app.fullyLegalSquares)
        if app.showPawnPromotion:
            drawPawnPromotion(app.pawnPromotionBoard, app.pawnPromotionSquares)
        ###### test code ######
        # if app.player1.isTurn == True:
        #     drawLabel('Player 1 turn: True', 330, 270)
        # else:
        #     drawLabel('Player 1 turn: False', 330, 270)
        # if app.player2.isTurn == True:
        #     drawLabel('Player 2 turn: True', 330, 280)
        # else:
        #     drawLabel('Player 2 turn: False', 330, 280)
        # if app.currentSquare == None:
        #     drawLabel('Current Square: None', 330, 300)
        # else:
        #     if app.currentSquare.piece != None:
        #         drawLabel('Current Square', 330, 300)
        #         drawImage(app.currentSquare.piece.image, 360, 300, align = 'center')
        #     else:
        #         drawLabel('Current Square: Empty Space', 330, 300)

        # if app.selectedSquare == None:
        #         drawLabel('Selected Square: None', 330, 330)
        # else:
        #     if app.selectedSquare.piece != None:
        #         drawLabel('Selected Square', 330, 330)
        #         drawImage(app.selectedSquare.piece.image, 360, 330, align = 'center')
        #     else:
        #         drawLabel('Selected Square: Empty Space', 330, 330)
        # drawLabel(f'player 1 canCastle: {app.player1.canCastle}', 330, 250)
        # drawLabel(f'player 2 canCastle: {app.player2.canCastle}', 330, 240)
        # if app.previousMove[0] != None and app.previousMove[1] != None:
        #     drawLabel('Previous moves', 330, 150)
        #     drawLabel(f'inital Square position: {app.previousMove[0].row}, {app.previousMove[0].col}', 330, 160)
        #     drawLabel('inital Square piece: ', 330, 175)
        #     if app.previousMove[0].piece != None:
        #         drawImage(app.previousMove[0].piece.image, 360, 175)
        #     else:
        #         drawLabel('None', 360, 175)
        #     drawLabel(f'final Square position: {app.previousMove[1].row}, {app.previousMove[1].col}', 330, 190)
        #     drawLabel('final Square piece', 330, 210)
        #     if app.previousMove[1].piece != None:
        #         drawImage(app.previousMove[1].piece.image, 360, 210)
        #     else:
        #         drawLabel('None', 360, 210)
        # drawLabel(f"player 1's king is at{findKing(app.player1, app.squares).row}, {findKing(app.player1, app.squares).col}", 330, 140)
        # drawLabel(f"player 2's king is at{findKing(app.player2, app.squares).row}, {findKing(app.player2, app.squares).col}", 330, 130)
        
        ###### test code ######
# onMousePress
def onMousePress(app, mouseX, mouseY):
    # we are in menu
    if app.showMenu:
        if mouseX <= 300 and mouseX >= 100:
            # two player
            if mouseY <= 225 and mouseY >= 125:
                # don't want to show menu anymore
                app.showMenu = False
                # black pieces (16 total)
                squareH1 = Square(Rook(app.blackRookImg), 0, 0, 'black')
                squareG1 = Square(Knight(app.blackKnightImg), 0, 1, 'black')
                squareF1 = Square(Bishop(app.blackBishopImg), 0, 2, 'black')
                squareE1 = Square(Queen(app.blackQueenImg), 0, 3, 'black')
                squareD1 = Square(King(app.blackKingImg), 0, 4, 'black')
                squareC1 = Square(Bishop(app.blackBishopImg), 0, 5, 'black')
                squareB1 = Square(Knight(app.blackKnightImg), 0, 6, 'black')
                squareA1 = Square(Rook(app.blackRookImg), 0, 7, 'black')
                squareH2 = Square(Pawn(app.blackPawnImg), 1, 0, 'black')
                squareG2 = Square(Pawn(app.blackPawnImg), 1, 1, 'black')
                squareF2 = Square(Pawn(app.blackPawnImg), 1, 2, 'black')
                squareE2 = Square(Pawn(app.blackPawnImg), 1, 3, 'black')
                squareD2 = Square(Pawn(app.blackPawnImg), 1, 4, 'black')
                squareC2 = Square(Pawn(app.blackPawnImg), 1, 5, 'black')
                squareB2 = Square(Pawn(app.blackPawnImg), 1, 6, 'black')
                squareA2 = Square(Pawn(app.blackPawnImg), 1, 7, 'black')
                # middle pieces (start blank) (32 total)
                squareH3 = Square(None, 2, 0, None)
                squareG3 = Square(None, 2, 1, None)
                squareF3 = Square(None, 2, 2, None)
                squareE3 = Square(None, 2, 3, None)
                squareD3 = Square(None, 2, 4, None)
                squareC3 = Square(None, 2, 5, None)
                squareB3 = Square(None, 2, 6, None)
                squareA3 = Square(None, 2, 7, None)
                squareH4 = Square(None, 3, 0, None)
                squareG4 = Square(None, 3, 1, None)
                squareF4 = Square(None, 3, 2, None)
                squareE4 = Square(None, 3, 3, None)
                squareD4 = Square(None, 3, 4, None)
                squareC4 = Square(None, 3, 5, None)
                squareB4 = Square(None, 3, 6, None)
                squareA4 = Square(None, 3, 7, None)
                squareH5 = Square(None, 4, 0, None)
                squareG5 = Square(None, 4, 1, None)
                squareF5 = Square(None, 4, 2, None)
                squareE5 = Square(None, 4, 3, None)
                squareD5 = Square(None, 4, 4, None)
                squareC5 = Square(None, 4, 5, None)
                squareB5 = Square(None, 4, 6, None)
                squareA5 = Square(None, 4, 7, None)
                squareH6 = Square(None, 5, 0, None)
                squareG6 = Square(None, 5, 1, None)
                squareF6 = Square(None, 5, 2, None)
                squareE6 = Square(None, 5, 3, None)
                squareD6 = Square(None, 5, 4, None)
                squareC6 = Square(None, 5, 5, None)
                squareB6 = Square(None, 5, 6, None)
                squareA6 = Square(None, 5, 7, None)
                # white pieces (16 total)
                squareH7 = Square(Pawn(app.whitePawnImg), 6, 0, 'white')
                squareG7 = Square(Pawn(app.whitePawnImg), 6, 1, 'white')
                squareF7 = Square(Pawn(app.whitePawnImg), 6, 2, 'white')
                squareE7 = Square(Pawn(app.whitePawnImg), 6, 3, 'white')
                squareD7 = Square(Pawn(app.whitePawnImg), 6, 4, 'white')
                squareC7 = Square(Pawn(app.whitePawnImg), 6, 5, 'white')
                squareB7 = Square(Pawn(app.whitePawnImg), 6, 6, 'white')
                squareA7 = Square(Pawn(app.whitePawnImg), 6, 7, 'white')
                squareH8 = Square(Rook(app.whiteRookImg), 7, 0, 'white')
                squareG8 = Square(Knight(app.whiteKnightImg), 7, 1, 'white')
                squareF8 = Square(Bishop(app.whiteBishopImg), 7, 2, 'white')
                squareE8 = Square(Queen(app.whiteQueenImg), 7, 3, 'white')
                squareD8 = Square(King(app.whiteKingImg), 7, 4 , 'white')
                squareC8 = Square(Bishop(app.whiteBishopImg), 7, 5, 'white')
                squareB8 = Square(Knight(app.whiteKnightImg), 7, 6, 'white')
                squareA8 = Square(Rook(app.whiteRookImg), 7, 7, 'white')
                app.squares = [[squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1],
                               [squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2],
                               [squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3],
                               [squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4],
                               [squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5],
                               [squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6],
                               [squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7],
                               [squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]]
            # single player
            elif mouseY <= 350 and mouseY >= 250:
                app.showMenu = False
                app.showAIMenuScreen = True
    # we are in AIMenuSceen
    elif app.showAIMenuScreen:
        if mouseX <= 300 and mouseX >= 100:
            # white
            if mouseY <= 225 and mouseY >= 125:
                app.showAIMenuScreen = False
                app.player1 = Player('white', True, False, 'player 1', False)
                app.player2 = Player('black', False, True, 'AI', False)
                # black pieces (16 total)
                squareH1 = Square(Rook(app.blackRookImg), 0, 0, 'black')
                squareG1 = Square(Knight(app.blackKnightImg), 0, 1, 'black')
                squareF1 = Square(Bishop(app.blackBishopImg), 0, 2, 'black')
                squareE1 = Square(Queen(app.blackQueenImg), 0, 3, 'black')
                squareD1 = Square(King(app.blackKingImg), 0, 4, 'black')
                squareC1 = Square(Bishop(app.blackBishopImg), 0, 5, 'black')
                squareB1 = Square(Knight(app.blackKnightImg), 0, 6, 'black')
                squareA1 = Square(Rook(app.blackRookImg), 0, 7, 'black')
                squareH2 = Square(Pawn(app.blackPawnImg), 1, 0, 'black')
                squareG2 = Square(Pawn(app.blackPawnImg), 1, 1, 'black')
                squareF2 = Square(Pawn(app.blackPawnImg), 1, 2, 'black')
                squareE2 = Square(Pawn(app.blackPawnImg), 1, 3, 'black')
                squareD2 = Square(Pawn(app.blackPawnImg), 1, 4, 'black')
                squareC2 = Square(Pawn(app.blackPawnImg), 1, 5, 'black')
                squareB2 = Square(Pawn(app.blackPawnImg), 1, 6, 'black')
                squareA2 = Square(Pawn(app.blackPawnImg), 1, 7, 'black')
                # middle pieces (start blank) (32 total)
                squareH3 = Square(None, 2, 0, None)
                squareG3 = Square(None, 2, 1, None)
                squareF3 = Square(None, 2, 2, None)
                squareE3 = Square(None, 2, 3, None)
                squareD3 = Square(None, 2, 4, None)
                squareC3 = Square(None, 2, 5, None)
                squareB3 = Square(None, 2, 6, None)
                squareA3 = Square(None, 2, 7, None)
                squareH4 = Square(None, 3, 0, None)
                squareG4 = Square(None, 3, 1, None)
                squareF4 = Square(None, 3, 2, None)
                squareE4 = Square(None, 3, 3, None)
                squareD4 = Square(None, 3, 4, None)
                squareC4 = Square(None, 3, 5, None)
                squareB4 = Square(None, 3, 6, None)
                squareA4 = Square(None, 3, 7, None)
                squareH5 = Square(None, 4, 0, None)
                squareG5 = Square(None, 4, 1, None)
                squareF5 = Square(None, 4, 2, None)
                squareE5 = Square(None, 4, 3, None)
                squareD5 = Square(None, 4, 4, None)
                squareC5 = Square(None, 4, 5, None)
                squareB5 = Square(None, 4, 6, None)
                squareA5 = Square(None, 4, 7, None)
                squareH6 = Square(None, 5, 0, None)
                squareG6 = Square(None, 5, 1, None)
                squareF6 = Square(None, 5, 2, None)
                squareE6 = Square(None, 5, 3, None)
                squareD6 = Square(None, 5, 4, None)
                squareC6 = Square(None, 5, 5, None)
                squareB6 = Square(None, 5, 6, None)
                squareA6 = Square(None, 5, 7, None)
                # white pieces (16 total)
                squareH7 = Square(Pawn(app.whitePawnImg), 6, 0, 'white')
                squareG7 = Square(Pawn(app.whitePawnImg), 6, 1, 'white')
                squareF7 = Square(Pawn(app.whitePawnImg), 6, 2, 'white')
                squareE7 = Square(Pawn(app.whitePawnImg), 6, 3, 'white')
                squareD7 = Square(Pawn(app.whitePawnImg), 6, 4, 'white')
                squareC7 = Square(Pawn(app.whitePawnImg), 6, 5, 'white')
                squareB7 = Square(Pawn(app.whitePawnImg), 6, 6, 'white')
                squareA7 = Square(Pawn(app.whitePawnImg), 6, 7, 'white')
                squareH8 = Square(Rook(app.whiteRookImg), 7, 0, 'white')
                squareG8 = Square(Knight(app.whiteKnightImg), 7, 1, 'white')
                squareF8 = Square(Bishop(app.whiteBishopImg), 7, 2, 'white')
                squareE8 = Square(Queen(app.whiteQueenImg), 7, 3, 'white')
                squareD8 = Square(King(app.whiteKingImg), 7, 4 , 'white')
                squareC8 = Square(Bishop(app.whiteBishopImg), 7, 5, 'white')
                squareB8 = Square(Knight(app.whiteKnightImg), 7, 6, 'white')
                squareA8 = Square(Rook(app.whiteRookImg), 7, 7, 'white')
                app.squares = [[squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1],
                               [squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2],
                               [squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3],
                               [squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4],
                               [squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5],
                               [squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6],
                               [squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7],
                               [squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]]
            # black
            elif mouseY <= 350 and mouseY >= 250:
                app.showAIMenuScreen = False
                app.player1 = Player('black', False, False, 'player 1', False)
                app.player2 = Player('white', True, True, 'AI', False)
                # white pieces (16 total)
                squareH1 = Square(Rook(app.whiteRookImg), 0, 0, 'white')
                squareG1 = Square(Knight(app.whiteKnightImg), 0, 1, 'white')
                squareF1 = Square(Bishop(app.whiteBishopImg), 0, 2, 'white')
                squareE1 = Square(Queen(app.whiteQueenImg), 0, 3, 'white')
                squareD1 = Square(King(app.whiteKingImg), 0, 4, 'white')
                squareC1 = Square(Bishop(app.whiteBishopImg), 0, 5, 'white')
                squareB1 = Square(Knight(app.whiteKnightImg), 0, 6, 'white')
                squareA1 = Square(Rook(app.whiteRookImg), 0, 7, 'white')
                squareH2 = Square(Pawn(app.whitePawnImg), 1, 0, 'white')
                squareG2 = Square(Pawn(app.whitePawnImg), 1, 1, 'white')
                squareF2 = Square(Pawn(app.whitePawnImg), 1, 2, 'white')
                squareE2 = Square(Pawn(app.whitePawnImg), 1, 3, 'white')
                squareD2 = Square(Pawn(app.whitePawnImg), 1, 4, 'white')
                squareC2 = Square(Pawn(app.whitePawnImg), 1, 5, 'white')
                squareB2 = Square(Pawn(app.whitePawnImg), 1, 6, 'white')
                squareA2 = Square(Pawn(app.whitePawnImg), 1, 7, 'white')
                # middle pieces (start blank) (32 total)
                squareH3 = Square(None, 2, 0, None)
                squareG3 = Square(None, 2, 1, None)
                squareF3 = Square(None, 2, 2, None)
                squareE3 = Square(None, 2, 3, None)
                squareD3 = Square(None, 2, 4, None)
                squareC3 = Square(None, 2, 5, None)
                squareB3 = Square(None, 2, 6, None)
                squareA3 = Square(None, 2, 7, None)
                squareH4 = Square(None, 3, 0, None)
                squareG4 = Square(None, 3, 1, None)
                squareF4 = Square(None, 3, 2, None)
                squareE4 = Square(None, 3, 3, None)
                squareD4 = Square(None, 3, 4, None)
                squareC4 = Square(None, 3, 5, None)
                squareB4 = Square(None, 3, 6, None)
                squareA4 = Square(None, 3, 7, None)
                squareH5 = Square(None, 4, 0, None)
                squareG5 = Square(None, 4, 1, None)
                squareF5 = Square(None, 4, 2, None)
                squareE5 = Square(None, 4, 3, None)
                squareD5 = Square(None, 4, 4, None)
                squareC5 = Square(None, 4, 5, None)
                squareB5 = Square(None, 4, 6, None)
                squareA5 = Square(None, 4, 7, None)
                squareH6 = Square(None, 5, 0, None)
                squareG6 = Square(None, 5, 1, None)
                squareF6 = Square(None, 5, 2, None)
                squareE6 = Square(None, 5, 3, None)
                squareD6 = Square(None, 5, 4, None)
                squareC6 = Square(None, 5, 5, None)
                squareB6 = Square(None, 5, 6, None)
                squareA6 = Square(None, 5, 7, None)
                # black pieces (16 total)
                squareH7 = Square(Pawn(app.blackPawnImg), 6, 0, 'black')
                squareG7 = Square(Pawn(app.blackPawnImg), 6, 1, 'black')
                squareF7 = Square(Pawn(app.blackPawnImg), 6, 2, 'black')
                squareE7 = Square(Pawn(app.blackPawnImg), 6, 3, 'black')
                squareD7 = Square(Pawn(app.blackPawnImg), 6, 4, 'black')
                squareC7 = Square(Pawn(app.blackPawnImg), 6, 5, 'black')
                squareB7 = Square(Pawn(app.blackPawnImg), 6, 6, 'black')
                squareA7 = Square(Pawn(app.blackPawnImg), 6, 7, 'black')
                squareH8 = Square(Rook(app.blackRookImg), 7, 0, 'black')
                squareG8 = Square(Knight(app.blackKnightImg), 7, 1, 'black')
                squareF8 = Square(Bishop(app.blackBishopImg), 7, 2, 'black')
                squareE8 = Square(Queen(app.blackQueenImg), 7, 3, 'black')
                squareD8 = Square(King(app.blackKingImg), 7, 4 , 'black')
                squareC8 = Square(Bishop(app.blackBishopImg), 7, 5, 'black')
                squareB8 = Square(Knight(app.blackKnightImg), 7, 6, 'black')
                squareA8 = Square(Rook(app.blackRookImg), 7, 7, 'black')
                app.squares = [[squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1],
                               [squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2],
                              [squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3],
                               [squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4],
                               [squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5],
                               [squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6],
                               [squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7],
                               [squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]]
    # we are promoting a pawn
    elif app.showPawnPromotion:
        promotedSquare = getPromotedSquare(app.pawnPromotionBoard, app.pawnPromotionSquares, mouseX, mouseY)
        if promotedSquare != None:
            app.currentSquare.piece = promotedSquare.piece
            app.showPawnPromotion = False
            if app.player1.isTurn == True:
                if inCheck(app.player1, app.squares, app.player2, app.previousMove):
                            app.message = 'Check'
                if inCheckmate(app.player1, app.squares, app.player2, app.previousMove):
                    app.message = f'Checkmate: {app.player2.name} wins'
                    app.gameOver = True
                elif staleMate(app.player1, app.squares, app.player2, app.previousMove):
                            app.message = f'Stalemate: {app.player1.name} wins'
                            app.gameOver = True
            else:
                if inCheck(app.player2, app.squares, app.player1, app.previousMove):
                            app.message = 'Check'
                if inCheckmate(app.player2, app.squares, app.player1, app.previousMove):
                    app.message = f'Checkmate: {app.player1.name} wins'
                    app.gameOver = True
                elif staleMate(app.player2, app.squares, app.player1, app.previousMove):
                            app.message = f'Stalemate: {app.player2.name} wins'
                            app.gameOver = True
    else: # we are in game
        app.currentSquare = getSquare(app.squares, app.board, mouseX, mouseY)
        # if user clicks on a square or the game isn't over
        if app.currentSquare != None and app.gameOver == False:
            # it's player 1's turn
            if app.player1.isTurn == True:
                # square is not selected, meaning that this mouse press should make a selection
                if app.selectedSquare == None:
                    # checks if currentSquare is a legal selection
                    if isLegalSelection(app.player1, app.currentSquare):
                        app.selectedSquare = app.currentSquare
                        app.semiLegalSquares = semiLegalMoves(app.selectedSquare, app.squares, app.player1, app.previousMove)
                        app.fullyLegalSquares = fullyLegalMoves(app.selectedSquare, app.squares, app.player1, app.previousMove, app.player2, app.semiLegalSquares)
                        ### still player 1's turn ###
                # A square is already selected, meaning we want to move the piece or change selection
                else:
                    # find the semi legal and fully legal squares of the piece on the selected square 
                    
                    #print(f'semi legal Squares: {semiLegalSquares}')
                    #print(f'fully legal Squares: {fullyLegalSquares}')
                    if app.currentSquare in app.fullyLegalSquares:
                        # make the move
                        makeMove(app.selectedSquare, app.currentSquare, app.squares, app.player1, app.previousMove)
                        app.message = ''
                        # checks for pawn promotion
                        if isinstance(app.currentSquare.piece, Pawn) and app.currentSquare.row == 0:
                            left, top = getSquareLeftTop(app.board, app.currentSquare.row, app.currentSquare.col)
                            width, height = getSquareSize(app.board)
                            app.pawnPromotionBoard = PromotionBoard(1, 4, app.width/2 - (2*width), top-height, width*4, height)
                            if app.player1.color == 'black':
                                blackQueen = Square(Queen(app.blackQueenImg), 0, 0, 'black')
                                blackRook = Square(Rook(app.blackRookImg), 0, 1, 'black')
                                blackBishop = Square(Bishop(app.blackBishopImg), 0, 2, 'black')
                                blackKnight = Square(Knight(app.blackKnightImg), 0, 3, 'black')
                                app.pawnPromotionSquares = [blackQueen, blackRook, blackBishop, blackKnight]
                            else:
                                whiteQueen = Square(Queen(app.whiteQueenImg), 0, 0, 'white')
                                whiteRook = Square(Rook(app.whiteRookImg), 0, 1, 'white')
                                whiteBishop = Square(Bishop(app.whiteBishopImg), 0, 2, 'white')
                                whiteKnight = Square(Knight(app.whiteKnightImg), 0, 3, 'white')
                                app.pawnPromotionSquares = [whiteQueen, whiteRook, whiteBishop, whiteKnight]
                            app.showPawnPromotion = True
                        # keep track of Previous move
                        app.initialSquare = app.selectedSquare
                        app.finalSquare = app.currentSquare
                        app.previousMove = (app.initialSquare, app.finalSquare)
                        # every time player makes a move, we want to update canCastle
                        if app.player1.canCastle != None:
                            app.player1.canCastle = updateCanCastle(app.player1, app.squares)
                        # every time player 1 make's a move we want to see if they put
                        # player 2 in check or checkmate
                        if inCheck(app.player2, app.squares, app.player1, app.previousMove):
                            app.message = 'Check'
                        if inCheckmate(app.player2, app.squares, app.player1, app.previousMove):
                            app.message = f'Checkmate: {app.player1.name} wins'
                            app.gameOver = True
                        elif staleMate(app.player2, app.squares, app.player1, app.previousMove):
                            app.message = f'Stalemate: {app.player2.name} wins'
                            app.gameOver = True
                        # it now becomes player 2's turn
                        app.player1.isTurn = False
                        app.player2.isTurn = True
                        # make selected square None
                        app.selectedSquare = None
                        app.fullyLegalSquares = []
                    # elif the current square is semiLegalSquares but is not in fullyLegalSquares, making
                    # it an illegal move
                    elif app.currentSquare in app.semiLegalSquares:
                        app.message = 'Illegal move'
                        app.semiLegalSquares = []
                    # elif we want to change selection
                    elif isLegalSelection(app.player1, app.currentSquare):
                        app.selectedSquare = app.currentSquare
                        app.semiLegalSquares = semiLegalMoves(app.selectedSquare, app.squares, app.player1, app.previousMove)
                        app.fullyLegalSquares = fullyLegalMoves(app.selectedSquare, app.squares, app.player1, app.previousMove, app.player2, app.semiLegalSquares)
                        ### still player 1's turn ###
            # it's player 2's turn
            else:
                # square is not selected, meaning that this mouse press should make a selection
                if app.selectedSquare == None:
                    # checks if currentSquare is a legal selection
                    if isLegalSelection(app.player2, app.currentSquare):
                        app.selectedSquare = app.currentSquare
                        app.semiLegalSquares = semiLegalMoves(app.selectedSquare, app.squares, app.player2, app.previousMove)
                        app.fullyLegalSquares = fullyLegalMoves(app.selectedSquare, app.squares, app.player2, app.previousMove, app.player1, app.semiLegalSquares)
                        ### still player 2's turn
                # A sqaure is selected, meaning we want to move the piece or change selection
                else:
                    # find the semi legal and fully legal squares of the piece on the selected square 
                    
                    # if the current square is a fully legal square, make the move
                    if app.currentSquare in app.fullyLegalSquares:
                        # make move
                        makeMove(app.selectedSquare, app.currentSquare, app.squares, app.player2, app.previousMove)
                        app.message = ''
                        # checks for pawn promotion
                        if isinstance(app.currentSquare.piece, Pawn) and app.currentSquare.row == 7:
                            left, top = getSquareLeftTop(app.board, app.currentSquare.row, app.currentSquare.col)
                            width, height = getSquareSize(app.board)
                            app.pawnPromotionBoard = PromotionBoard(1, 4, app.width/2 - (2*width), top+height, width*4, height)
                            if app.player2.color == 'white':
                                whiteQueen = Square(Queen(app.whiteQueenImg), 0, 0, 'white')
                                whiteRook = Square(Rook(app.whiteRookImg), 0, 1, 'white')
                                whiteBishop = Square(Bishop(app.whiteBishopImg), 0, 2, 'white')
                                whiteKnight = Square(Knight(app.whiteKnightImg), 0, 3, 'white')
                                app.pawnPromotionSquares = [whiteQueen, whiteRook, whiteBishop, whiteKnight]
                            else:
                                blackQueen = Square(Queen(app.blackQueenImg), 0, 0, 'black')
                                blackRook = Square(Rook(app.blackRookImg), 0, 1, 'black')
                                blackBishop = Square(Bishop(app.blackBishopImg), 0, 2, 'black')
                                blackKnight = Square(Knight(app.blackKnightImg), 0, 3, 'black')
                                app.pawnPromotionSquares = [blackQueen, blackRook, blackBishop, blackKnight]
                            app.showPawnPromotion = True
                        # keep track of Previous move
                        app.initialSquare = app.selectedSquare
                        app.finalSquare = app.currentSquare
                        app.previousMove = (app.initialSquare, app.finalSquare)
                        # every time player makes a move, we want to update canCastle
                        if app.player2.canCastle != None:
                            app.player2.canCastle = updateCanCastle(app.player2, app.squares)
                        # every time player 2 makes a move we want to see if they put
                        # player 1 in check or in checkMate
                        if inCheck(app.player1, app.squares, app.player2, app.previousMove):
                            app.message = 'Check'
                        if inCheckmate(app.player1, app.squares, app.player2, app.previousMove):
                            app.message = f'Checkmate: {app.player2.name} wins'
                            app.gameOver = True
                        elif staleMate(app.player1, app.squares, app.player2, app.previousMove):
                            app.message = f'Stalemate: {app.player1.name} wins'
                            app.gameOver = True
                        # it now becomes player 1's turn
                        app.player1.isTurn = True
                        app.player2.isTurn = False
                        # make selected square None
                        app.selectedSquare = None
                        app.fullyLegalSquares = []
                    # elif the square is in semiLegalSquares but not in fullyLegalSquares, making it an illegal move
                    elif app.currentSquare in app.semiLegalSquares:
                        app.message = 'Illegal move'
                        app.semiLegalSquares = []
                    # elif we want to change the selection
                    elif isLegalSelection(app.player2, app.currentSquare):
                        app.selectedSquare = app.currentSquare
                        app.semiLegalSquares = semiLegalMoves(app.selectedSquare, app.squares, app.player2, app.previousMove)
                        app.fullyLegalSquares = fullyLegalMoves(app.selectedSquare, app.squares, app.player2, app.previousMove, app.player1, app.semiLegalSquares)
                        ### still player 2's turn ###

# onKeyPress function
def onKeyPress(app, key):
    # go back to menu, reset everything
    if key == 'm':
        reset(app)
# main function
def main():
    runApp()
main()