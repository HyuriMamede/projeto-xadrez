from boardgame import Position, Board

class Piece:
    def __init__(self, position: Position, board: Board):
        self._position = position #tem o efeito do '#protected" do java
        self.__board = board # efeito do "private"
    
    @property
    def board(self):
        '''Só para as class e subclass, uso interno da camada de tabuleiro'''
        return self.__board
    
    #Não fiz o 'setter', não quero que o tabuleiro seja alterado

