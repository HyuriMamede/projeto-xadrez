class Board:
    def __init__(self, rows:int, columns:int): 
        '''Inicializa o tabuleiro com as dimensões passadas'''
        self.__rows = rows
        self.__columns = columns
        self._pieces = [[None for _ in range(columns)] for _ in range(rows)] # matriz vazia, feita com lista aninhadas


    @property
    def rows(self) -> int:
        '''é tipo um get do java, retorna o número de linhas do tabuleiro'''
        return self.__rows
    
    @property
    def columns(self) -> int:
        '''mesma coisa, retorna o número de colunas'''
        return self.__columns
    
    def _validando_posicao(self, row: int, column: int):
        '''garantir que os valores da linha e coluna estejam
        dos limites do tabuleiro'''
        if not (0<= row < self.__rows and 0 <=column < self.__columns):
            raise ValueError(f'Posição inválida: ({row}, {column})')
    
    def get_piece(self, row: int, column: int):

        self._validando_posicao(row, column) # ver se é valido
        return self._pieces[row][column] # retorna na posição indicada

    def get_piece_by_position(self, position):
        if not hasattr(position, 'row') or not hasattr(position, 'column'):
            raise ValueError("A 'position' não tem os atributos certos (row e column)")
        return  self.get_piece(position.row, position.column)   
    
    def __str__(self):
        '''represetação em string do tabuleiro'''
        return '\n'.join(
            ' '.join(str(piece) if piece else '-' for piece in row)
            for row in self._pieces
        ) # '\n.join' todas as linhas do tabuleiro com a devida quebra de linhas
          # " ".join -> para cada linha do tabuleiro, separa os espaços com ' '
          
    

    

    

    