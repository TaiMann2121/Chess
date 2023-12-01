from cmu_graphics import *
from piece import *
from board import *
from menus import *
from player import *
from gameScreenIcons import *
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
    app.sqaures = []
    # initializes players
    app.player1 = Player('white', True, False, 'player 1')
    app.player2  = Player('black', False, False, 'player 2')
# redrawAll function
def redrawAll(app):
    # background and title
    drawRect(0, 0, app.width, app.height, fill = 'burlyWood')
    drawLabel('112 Chess!', 200, 50, size = 50, font = 'ariel', fill = 'black')
    if app.showMenu: # if we are in menu
        drawMenu()
    elif app.showAIMenuScreen:
        drawAIMenuScreen()
    else: # we are in Game
        # Icons
        drawIcons(app.player1, app.player2)
        # draws border
        drawBorder(app.board)
        # draws all the squares
        for square in app.squares:
            drawSquare(app.board, square)
def onMousePress(app, mouseX, mouseY):
    # we are in menu
    if app.showMenu:
        if mouseX <= 300 and mouseX >= 100:
            # two player
            if mouseY <= 225 and mouseY >= 125:
                # don't want to show menu anymore
                app.showMenu = False
                # black pieces (16 total)
                squareH1 = Square(BlackRook(app.blackRookImg), 0, 0, 'black')
                squareG1 = Square(BlackKnight(app.blackKnightImg), 0, 1, 'black')
                squareF1 = Square(BlackBishop(app.blackBishopImg), 0, 2, 'black')
                squareE1 = Square(BlackQueen(app.blackQueenImg), 0, 3, 'black')
                squareD1 = Square(BlackKing(app.blackKingImg), 0, 4, 'black')
                squareC1 = Square(BlackBishop(app.blackBishopImg), 0, 5, 'black')
                squareB1 = Square(BlackKnight(app.blackKnightImg), 0, 6, 'black')
                squareA1 = Square(BlackRook(app.blackRookImg), 0, 7, 'black')
                squareH2 = Square(BlackPawn(app.blackPawnImg), 1, 0, 'black')
                squareG2 = Square(BlackPawn(app.blackPawnImg), 1, 1, 'black')
                squareF2 = Square(BlackPawn(app.blackPawnImg), 1, 2, 'black')
                squareE2 = Square(BlackPawn(app.blackPawnImg), 1, 3, 'black')
                squareD2 = Square(BlackPawn(app.blackPawnImg), 1, 4, 'black')
                squareC2 = Square(BlackPawn(app.blackPawnImg), 1, 5, 'black')
                squareB2 = Square(BlackPawn(app.blackPawnImg), 1, 6, 'black')
                squareA2 = Square(BlackPawn(app.blackPawnImg), 1, 7, 'black')
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
                squareH7 = Square(WhitePawn(app.whitePawnImg), 6, 0, 'white')
                squareG7 = Square(WhitePawn(app.whitePawnImg), 6, 1, 'white')
                squareF7 = Square(WhitePawn(app.whitePawnImg), 6, 2, 'white')
                squareE7 = Square(WhitePawn(app.whitePawnImg), 6, 3, 'white')
                squareD7 = Square(WhitePawn(app.whitePawnImg), 6, 4, 'white')
                squareC7 = Square(WhitePawn(app.whitePawnImg), 6, 5, 'white')
                squareB7 = Square(WhitePawn(app.whitePawnImg), 6, 6, 'white')
                squareA7 = Square(WhitePawn(app.whitePawnImg), 6, 7, 'white')
                squareH8 = Square(WhiteRook(app.whiteRookImg), 7, 0, 'white')
                squareG8 = Square(WhiteKnight(app.whiteKnightImg), 7, 1, 'white')
                squareF8 = Square(WhiteBishop(app.whiteBishopImg), 7, 2, 'white')
                squareE8 = Square(WhiteQueen(app.whiteQueenImg), 7, 3, 'white')
                squareD8 = Square(WhiteKing(app.whiteKingImg), 7, 4 , 'white')
                squareC8 = Square(WhiteBishop(app.whiteBishopImg), 7, 5, 'white')
                squareB8 = Square(WhiteKnight(app.whiteKnightImg), 7, 6, 'white')
                squareA8 = Square(WhiteRook(app.whiteRookImg), 7, 7, 'white')
                app.squares = [squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1,
                               squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2,
                               squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3,
                               squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4,
                               squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5,
                               squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6,
                               squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7,
                               squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]
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
                app.player1 = Player('white', True, False, 'player 1')
                app.player2 = Player('black', False, True, 'Bob')
                # black pieces (16 total)
                squareH1 = Square(BlackRook(app.blackRookImg), 0, 0, 'black')
                squareG1 = Square(BlackKnight(app.blackKnightImg), 0, 1, 'black')
                squareF1 = Square(BlackBishop(app.blackBishopImg), 0, 2, 'black')
                squareE1 = Square(BlackQueen(app.blackQueenImg), 0, 3, 'black')
                squareD1 = Square(BlackKing(app.blackKingImg), 0, 4, 'black')
                squareC1 = Square(BlackBishop(app.blackBishopImg), 0, 5, 'black')
                squareB1 = Square(BlackKnight(app.blackKnightImg), 0, 6, 'black')
                squareA1 = Square(BlackRook(app.blackRookImg), 0, 7, 'black')
                squareH2 = Square(BlackPawn(app.blackPawnImg), 1, 0, 'black')
                squareG2 = Square(BlackPawn(app.blackPawnImg), 1, 1, 'black')
                squareF2 = Square(BlackPawn(app.blackPawnImg), 1, 2, 'black')
                squareE2 = Square(BlackPawn(app.blackPawnImg), 1, 3, 'black')
                squareD2 = Square(BlackPawn(app.blackPawnImg), 1, 4, 'black')
                squareC2 = Square(BlackPawn(app.blackPawnImg), 1, 5, 'black')
                squareB2 = Square(BlackPawn(app.blackPawnImg), 1, 6, 'black')
                squareA2 = Square(BlackPawn(app.blackPawnImg), 1, 7, 'black')
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
                squareH7 = Square(WhitePawn(app.whitePawnImg), 6, 0, 'white')
                squareG7 = Square(WhitePawn(app.whitePawnImg), 6, 1, 'white')
                squareF7 = Square(WhitePawn(app.whitePawnImg), 6, 2, 'white')
                squareE7 = Square(WhitePawn(app.whitePawnImg), 6, 3, 'white')
                squareD7 = Square(WhitePawn(app.whitePawnImg), 6, 4, 'white')
                squareC7 = Square(WhitePawn(app.whitePawnImg), 6, 5, 'white')
                squareB7 = Square(WhitePawn(app.whitePawnImg), 6, 6, 'white')
                squareA7 = Square(WhitePawn(app.whitePawnImg), 6, 7, 'white')
                squareH8 = Square(WhiteRook(app.whiteRookImg), 7, 0, 'white')
                squareG8 = Square(WhiteKnight(app.whiteKnightImg), 7, 1, 'white')
                squareF8 = Square(WhiteBishop(app.whiteBishopImg), 7, 2, 'white')
                squareE8 = Square(WhiteQueen(app.whiteQueenImg), 7, 3, 'white')
                squareD8 = Square(WhiteKing(app.whiteKingImg), 7, 4 , 'white')
                squareC8 = Square(WhiteBishop(app.whiteBishopImg), 7, 5, 'white')
                squareB8 = Square(WhiteKnight(app.whiteKnightImg), 7, 6, 'white')
                squareA8 = Square(WhiteRook(app.whiteRookImg), 7, 7, 'white')
                app.squares = [squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1,
                               squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2,
                               squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3,
                               squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4,
                               squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5,
                               squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6,
                               squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7,
                               squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]
            # black
            elif mouseY <= 350 and mouseY >= 250:
                app.showAIMenuScreen = False
                app.player1 = Player('black', False, False, 'player 1')
                app.player2 = Player('white', True, True, 'Bob')
                # white pieces (16 total)
                squareH1 = Square(WhiteRook(app.whiteRookImg), 0, 0, 'white')
                squareG1 = Square(WhiteKnight(app.whiteKnightImg), 0, 1, 'white')
                squareF1 = Square(WhiteBishop(app.whiteBishopImg), 0, 2, 'white')
                squareE1 = Square(WhiteQueen(app.whiteQueenImg), 0, 3, 'white')
                squareD1 = Square(WhiteKing(app.whiteKingImg), 0, 4, 'white')
                squareC1 = Square(WhiteBishop(app.whiteBishopImg), 0, 5, 'white')
                squareB1 = Square(WhiteKnight(app.whiteKnightImg), 0, 6, 'white')
                squareA1 = Square(WhiteRook(app.whiteRookImg), 0, 7, 'white')
                squareH2 = Square(WhitePawn(app.whitePawnImg), 1, 0, 'white')
                squareG2 = Square(WhitePawn(app.whitePawnImg), 1, 1, 'white')
                squareF2 = Square(WhitePawn(app.whitePawnImg), 1, 2, 'white')
                squareE2 = Square(WhitePawn(app.whitePawnImg), 1, 3, 'white')
                squareD2 = Square(WhitePawn(app.whitePawnImg), 1, 4, 'white')
                squareC2 = Square(WhitePawn(app.whitePawnImg), 1, 5, 'white')
                squareB2 = Square(WhitePawn(app.whitePawnImg), 1, 6, 'white')
                squareA2 = Square(WhitePawn(app.whitePawnImg), 1, 7, 'white')
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
                squareH7 = Square(BlackPawn(app.blackPawnImg), 6, 0, 'black')
                squareG7 = Square(BlackPawn(app.blackPawnImg), 6, 1, 'black')
                squareF7 = Square(BlackPawn(app.blackPawnImg), 6, 2, 'black')
                squareE7 = Square(BlackPawn(app.blackPawnImg), 6, 3, 'black')
                squareD7 = Square(BlackPawn(app.blackPawnImg), 6, 4, 'black')
                squareC7 = Square(BlackPawn(app.blackPawnImg), 6, 5, 'black')
                squareB7 = Square(BlackPawn(app.blackPawnImg), 6, 6, 'black')
                squareA7 = Square(BlackPawn(app.blackPawnImg), 6, 7, 'black')
                squareH8 = Square(BlackRook(app.blackRookImg), 7, 0, 'black')
                squareG8 = Square(BlackKnight(app.blackKnightImg), 7, 1, 'black')
                squareF8 = Square(BlackBishop(app.blackBishopImg), 7, 2, 'black')
                squareE8 = Square(BlackQueen(app.blackQueenImg), 7, 3, 'black')
                squareD8 = Square(BlackKing(app.blackKingImg), 7, 4 , 'black')
                squareC8 = Square(BlackBishop(app.blackBishopImg), 7, 5, 'black')
                squareB8 = Square(BlackKnight(app.blackKnightImg), 7, 6, 'black')
                squareA8 = Square(BlackRook(app.blackRookImg), 7, 7, 'black')
                app.squares = [squareH1, squareG1, squareF1, squareE1, squareD1, squareC1, squareB1, squareA1,
                               squareH2, squareG2, squareF2, squareE2, squareD2, squareC2, squareB2, squareA2,
                               squareH3, squareG3, squareF3, squareE3, squareD3, squareC3, squareB3, squareA3,
                               squareH4, squareG4, squareF4, squareE4, squareD4, squareC4, squareB4, squareA4,
                               squareH5, squareG5, squareF5, squareE5, squareD5, squareC5, squareB5, squareA5,
                               squareH6, squareG6, squareF6, squareE6, squareD6, squareC6, squareB6, squareA6,
                               squareH7, squareG7, squareF7, squareE7, squareD7, squareC7, squareB7, squareA7,
                               squareH8, squareG8, squareF8, squareE8, squareD8, squareC8, squareB8, squareA8]
# onKeyPress function
def onKeyPress(app, key):
    # go back to menu, reset everything
    if key == 'm':
        reset(app)
# main function
def main():
    runApp()
main()