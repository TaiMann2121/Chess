from cmu_graphics import *
from menu import *
from board import *
from gameScreenIcons import *
from players import Player
from PIL import Image

def onAppStart(app):
    # black pieces
    app.blackPawn = CMUImage(Image.open('Black_Pawn.png'))
    app.blackRook = CMUImage(Image.open('Black_Rook.png'))
    app.blackBishop = CMUImage(Image.open('Black_Bishop.png'))
    app.blackKnight = CMUImage(Image.open('Black_Knight.png'))
    app.blackQueen = CMUImage(Image.open('Black_Queen.png'))
    app.blackKing = CMUImage(Image.open('Black_King.png'))
    # white pieces
    app.whitePawn = CMUImage(Image.open('White_Pawn.png'))
    app.whiteRook = CMUImage(Image.open('White_Rook.png'))
    app.whiteBishop = CMUImage(Image.open('White_Bishop.png'))
    app.whiteKnight = CMUImage(Image.open('White_Knight.png'))
    app.whiteQueen = CMUImage(Image.open('White_Queen.png'))
    app.whiteKing = CMUImage(Image.open('White_King.png'))

    # player 1 -> white pieces
    app.whitePieces = {app.whitePawn: [(6,0),(6,1),(6,2),(6,3,),(6,4),(6,5),(6,6),(6,7)],
                       app.whiteRook: [(7,0), (7,7)],
                       app.whiteKnight: [(7,1),(7,6)],
                       app.whiteBishop: [(7,2),(7,5)],
                       app.whiteQueen: [(7,3)], app.whiteKing: [(7,4)]}
    app.player1 = Player(app.whitePieces)

    # player 2 -> black pieces
    app.blackPieces = {app.blackPawn: [(1,0),(1,1),(1,2),(1,3,),(1,4),(1,5),(1,6),(1,7)],
                       app.blackRook: [(0,0), (0,7)],
                       app.blackKnight: [(0,1),(0,6)],
                       app.blackBishop: [(0,2),(0,5)],
                       app.blackQueen: [(0,3)], app.blackKing: [(0,4)]}
    app.player2 = Player(app.blackPieces)

    app.showMenu = True
    app.gameMode = None
    app.board = Board()

def redrawAll(app):
    # background and title
    drawRect(0, 0, app.width, app.height, fill = 'burlyWood')
    drawLabel('112 Chess!', 200, 50, size = 50, font = 'ariel', fill = 'black')
    # draws menu
    if app.showMenu:
        drawMenu()
    # else, run game
    else:
        #draws board
        drawBoard(app.board)
        drawBorder(app, app.board)
        # Icons
        drawIcons()
        # draws pieces
        drawPieces(app.board, app.player1)
        drawPieces(app.board, app.player2)


# mousePress function
def onMousePress(app, mouseX, mouseY):
    # if we are in the menu
    if app.showMenu:
        if mouseX <= 300 and mouseX >= 100:
            # two player
            if mouseY <= 225 and mouseY >= 125:
                app.gameMode = 'Two'
                app.showMenu = False
            # single player
            elif mouseY <= 350 and mouseY >= 250:
                app.gameMode = 'Single'
                app.showMenu = False
    # we are in game
    else:
        pass

# keyPress function
def onKeyPress(app, key):
    if key == 'm':
        app.gameMode = None
        app.showMenu = True

# main function
def main():
    runApp()
main()
