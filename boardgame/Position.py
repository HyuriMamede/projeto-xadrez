class Position:
    def __init__(self, row:int, column:int):
        self.__row= row
        self.__column = column

    #funcionamento do getter
    @property
    def row(self) -> int:
        return self.__row
    #funcionamento do get para column
    @property
    def column(self) -> int:
        return self.__column
    

    @row.setter
    def row(self, value:int):
        self.__row = value
    @column.setter
    def column(self, value:int):
        self.__column = value

    
    # método semelhante ao toString do java
    def __str__(self) -> str:
        return f'{self.row}, {self.column}'
        #é apenas para imprimir a posição na tela
