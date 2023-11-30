from cmu_graphics import *
from menu import *
from board import *
from gameScreenIcons import *
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
        # menu Icon
        drawIcons()
        drawImage(app.whiteKing, 200, 200, align = 'center')

# mousePress function
def onMousePress(app, mouseX, mouseY):
    # if we are in the menu
    if app.showMenu:
        if mouseX <= 300 and mouseX >= 100:
            if mouseY <= 225 and mouseY >= 125:
                app.gameMode = 'Two'
                app.showMenu = False
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
