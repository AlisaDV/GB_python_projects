class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
        matr = []
        for i in range(len(self.matrix)):
            matr.append([])
            for j in range(len(self.matrix[0])):
                matr[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join('\t'.join(map(str, row))
                         for row in matr)


list_of_list = [[3, 3, 3], [2, 5, 1], [6, 1, 0]]
list_of_list2 = [[9, 2, 1], [1, 1, 1], [0, 0, 0]]
matrix = Matrix(list_of_list)
matrix2 = Matrix(list_of_list2)
print(matrix.__str__())
print(matrix + matrix2)
