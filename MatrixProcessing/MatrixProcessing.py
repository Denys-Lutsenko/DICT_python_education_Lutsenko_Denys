'''MatrixProcessing 1-st'''
def reader_matrix():
    n, m = input().split()
    matrix = [list(map(int, input().split())) for _ in range(int(n))]
    return matrix


def sum_matrix(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        matrix_sub = []
        for j, k in zip(matrix1[i], matrix2[i]):
            matrix_sub.append(j + k)
        matrix.append(matrix_sub)
    return matrix


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'matrix {(len(self.matrix), len(self.matrix[0]))}'

    def __eq__(self, other):
        return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])


matrix_1 = Matrix(reader_matrix())
matrix_2 = Matrix(reader_matrix())
if matrix_1 == matrix_2:
    for n in sum_matrix(matrix_1.matrix, matrix_2.matrix):
        print(*n)
else:
    print('ERROR')

'''4 5
1 2 3 4 5
3 2 3 2 1
8 0 9 9 1
1 3 4 5 6
4 5
1 1 4 4 5
4 4 5 7 8
1 2 3 9 8
1 0 0 0 1'''