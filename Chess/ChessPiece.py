from boardgame import Piece, Board
from Chess import Color

class ChessPiece(Piece):
    
    def __init__(self, board: Board ,color: Color):
        super().__init__(board) # chamando o construtor da classe pai
        self.__color = color
    
    @property
    def color(self):
        return self.__color
        
