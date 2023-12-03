# main piece class
class Piece:
    def __init__(self, image):
        self.image = image

# individual pieces inherited from piece class

# black pieces
class Pawn(Piece):
    def __init__(self, image):
        super().__init__(image)
class Rook(Piece):
    def __init__(self, image):
        super().__init__(image)
class Knight(Piece):
    def __init__(self, image):
        super().__init__(image)
class Bishop(Piece):
    def __init__(self, image):
        super().__init__(image)
class Queen(Piece):
    def __init__(self, image):
        super().__init__(image)
class King(Piece):
    def __init__(self, image):
        super().__init__(image)
