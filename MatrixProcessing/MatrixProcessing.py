'''MatrixProcessing 1-st'''
# def reader_matrix():
#     n, m = input().split()
#     matrix = [list(map(int, input().split())) for _ in range(int(n))]
#     return matrix
#
#
# def sum_matrix(matrix1, matrix2):
#     matrix = []
#     for i in range(len(matrix1)):
#         matrix_sub = []
#         for j, k in zip(matrix1[i], matrix2[i]):
#             matrix_sub.append(j + k)
#         matrix.append(matrix_sub)
#     return matrix
#
#
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return f'matrix {(len(self.matrix), len(self.matrix[0]))}'
#
#     def __eq__(self, other):
#         return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])
#
#
# matrix_1 = Matrix(reader_matrix())
# matrix_2 = Matrix(reader_matrix())
# if matrix_1 == matrix_2:
#     for n in sum_matrix(matrix_1.matrix, matrix_2.matrix):
#         print(*n)
# else:
#     print('ERROR')
#
# '''4 5
# 1 2 3 4 5
# 3 2 3 2 1
# 8 0 9 9 1
# 1 3 4 5 6
# 4 5
# 1 1 4 4 5
# 4 4 5 7 8
# 1 2 3 9 8
# 1 0 0 0 1'''

'''MatrixProcessing 2-st'''
# def reader_matrix():
#     n, m = input().split()
#     matrix = [list(map(int, input().split())) for _ in range(int(n))]
#     return matrix
#
#
# def sum_matrix(matrix1, matrix2):
#     matrix = []
#     for i in range(len(matrix1)):
#         matrix_sub = []
#         for j, k in zip(matrix1[i], matrix2[i]):
#             matrix_sub.append(j + k)
#         matrix.append(matrix_sub)
#     return matrix
#
#
# def mul_matrix(matrix, x):
#     matrix_out = []
#     for n in matrix:
#         matrix_out_sub = []
#         for m in n:
#             matrix_out_sub.append(m * x)
#         matrix_out.append(matrix_out_sub)
#     return matrix_out
#
#
# def print_matrix(matrix):
#     for n in matrix:
#         print(*n)
#
#
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return f'matrix {(len(self.matrix), len(self.matrix[0]))}'
#
#     def __eq__(self, other):
#         return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])
#
#
# matrix_1 = Matrix(reader_matrix())
# matrix_mul = mul_matrix(matrix_1.matrix, int(input()))
# print_matrix(matrix_mul)
#
# '''3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 3'''
#
# '''2 3
# 1 2 3
# 4 5 6
# 0'''

'''MatrixProcessing 3-st'''

def show_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


def print_matrix(matrix):
    if isinstance(matrix, str):
        print(matrix)
    print("The result is:")
    for row in matrix:
        print(*row)
    print()


def get_matrices():
    rows_1, columns_1 = [int(x) for x in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:")
    first_matrix = [[float(x) for x in input().split()] for _ in range(rows_1)]
    rows_2, columns_2 = [int(x) for x in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:")
    second_matrix = [[float(x) for x in input().split()] for _ in range(rows_2)]
    return first_matrix, second_matrix


def add_matrices():
    first_matrix, second_matrix = get_matrices()
    if len(first_matrix) == len(second_matrix) and len(first_matrix[0]) == len(second_matrix[0]):
        return [[x + y for x, y in zip(row_1, row_2)] for row_1, row_2 in zip(first_matrix, second_matrix)]
    return "The operation cannot be performed."


def scalar_multiplication():
    rows, columns = [int(x) for x in input("Enter size of matrix: ").split()]
    print("Enter matrix:")
    matrix = [[float(x) for x in input().split()] for _ in range(rows)]
    scalar = float(input("Enter constant: "))
    return [[scalar * x for x in row] for row in matrix]


def matrix_multiplication():
    first_matrix, second_matrix = get_matrices()
    if len(first_matrix[0]) == len(second_matrix):
        transposed = transpose_matrix(second_matrix)
        result = [[None for _ in range(len(second_matrix[0]))] for _ in range(len(first_matrix))]
        for i in range(len(first_matrix)):
            for j in range(len(second_matrix[0])):
                result[i][j] = sum(x * y for x, y in zip(first_matrix[i], transposed[j]))
        return result
    return "The operation cannot be performed."


def transpose_matrix(matrix):
    transpose = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]
    return transpose


def main():
    while True:
        show_menu()
        users_choice = input("Your choice: ")
        if users_choice == "0":
            break
        elif users_choice == "1":
            result = add_matrices()
        elif users_choice == "2":
            result = scalar_multiplication()
        elif users_choice == "3":
            result = matrix_multiplication()
        print_matrix(result)


if __name__ == "__main__":
    main()
'''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: 3
Enter size of first matrix: 3 3
Enter first matrix:
1 7 7
6 6 4
4 2 1
Enter size of second matrix: 3 3
Enter second matrix:
3 2 4
5 5 9
8 0 10
The result is:
94.0 37.0 137.0
80.0 42.0 118.0
30.0 18.0 44.0

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: 1
Enter size of first matrix: 4 5
Enter first matrix:
1 2 3 4 5
3 2 3 2 1
8 0 9 9 1
1 3 4 5 6
Enter size of second matrix: 4 5
Enter second matrix:
1 1 4 4 5
4 4 5 7 8
1 2 3 9 8
1 0 0 0 1
The result is:
2.0 3.0 7.0 8.0 10.0
7.0 6.0 8.0 9.0 9.0
9.0 2.0 12.0 18.0 9.0
2.0 3.0 4.0 5.0 7.0'''