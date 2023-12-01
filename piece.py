# main piece class
class Piece:
    def __init__(self, image):
        self.image = image

# individual pieces inherited from piece class

# black pieces
class BlackPawn(Piece):
    def __init__(self, image):
        super().__init__(image)
class BlackRook(Piece):
    def __init__(self, image):
        super().__init__(image)
class BlackKnight(Piece):
    def __init__(self, image):
        super().__init__(image)
class BlackBishop(Piece):
    def __init__(self, image):
        super().__init__(image)
class BlackQueen(Piece):
    def __init__(self, image):
        super().__init__(image)
class BlackKing(Piece):
    def __init__(self, image):
        super().__init__(image)
# white pieces
class WhitePawn(Piece):
    def __init__(self, image):
        super().__init__(image)
class WhiteRook(Piece):
    def __init__(self, image):
        super().__init__(image)
class WhiteKnight(Piece):
    def __init__(self, image):
        super().__init__(image)
class WhiteBishop(Piece):
    def __init__(self, image):
        super().__init__(image)
class WhiteQueen(Piece):
    def __init__(self, image):
        super().__init__(image)
class WhiteKing(Piece):
    def __init__(self, image):
        super().__init__(image)