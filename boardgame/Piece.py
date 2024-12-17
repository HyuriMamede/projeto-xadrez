class Piece:
    def __init__(self, position: 'Position', board: 'Board'):
        self._position = position #tem o efeito do '#protected" do java
        self.__board = board # efeito do "private"

