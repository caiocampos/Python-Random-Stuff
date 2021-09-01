class Matrix(object):
    def __init__(self, matrix_string):
        self.__matrix = [[int(el) for el in line.split()]
                         for line in matrix_string.splitlines()]

    def row(self, index):
        return self.__matrix[index-1].copy()

    def column(self, index):
        return [el[index-1] for el in self.__matrix]
