'''TicTacToe 1-st'''
# print("X O X")
# print("O X O")
# print("X X O")

'''TicTacToe 2-st'''
# # O_OXXO_XX
# # _XO__X___
# board = list(input('Enter cells: '))
#
# print("---------")
# print("| " + board[0] + " " + board[1] + " " + board[2] + " |")
# print("| " + board[3] + " " + board[4] + " " + board[5] + " |")
# print("| " + board[6] + " " + board[7] + " " + board[8] + " |")
# print("---------")
'''TicTacToe 3-st'''
# # X wins = XXXOO__O_
# # O wins = XOOOXOXXO
# # Draw =   XOXOOXXXO
# # Game not finished = XO_OOX_X_
# # Impossible = XO_XO_XOX
# while True:
#     board = list(input('Enter cells: '))
#     print('---------')
#     print(f"""| {board[0]} {board[1]} {board[2]} |
# | {board[3]} {board[4]} {board[5]} |
# | {board[6]} {board[7]} {board[8]} |""")
#     print('---------')
#     a = 0
#     condition = []
#     for b in range(3):
#         try:
#             vert = [board[b], board[b + 3], board[b + 6]]
#             diag_1 = [board[0], board[4], board[8]]
#             diag_2 = [board[2], board[4], board[6]]
#             horz = board[a:a + 3]
#             if board.count('X') - board.count('O') > 1 or board.count('O') - board.count('X') > 1:
#                 condition.append('Impossible')
#             if diag_1.count(board[0]) == 3 or diag_2.count(board[2]) == 3:
#                 condition.append(f'{board[0]} wins')
#             if horz.count(board[a]) == 3:
#                 condition.append(f'{board[a]} wins')
#             if vert.count(board[b]) == 3:
#                 condition.append(f'{board[b]} wins')
#             a += 3
#         except IndexError:
#             continue
#     if len(condition) == 0:
#         if '_' in board:
#             print('Game not finished')
#         else:
#             print('Draw')
#     else:
#         if condition.count(condition[0]) == len(condition):
#             print(condition[0])
#         else:
#             print('Impossible')
#             break
'''TicTacToe 4-st'''


def print_field(l):
    print("""
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
""".format(*l))
# g = '123456789'
cells = list("_________")
print_field(cells)
previous_move = "O"
while True:

    if cells.count("_") == 0:
        break
    coordinates = input("Enter the coordinates: ").split(" ")
    if not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print("You should enter numbers!")
        continue
    elif int(coordinates[0]) > 3 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    cords_1d = ((int(coordinates[0]) - 1) * 3) + (int(coordinates[1]) - 1)
    if cells[cords_1d] != "_":
        print("This cell is occupied! Choose another one!")

    else:
        if previous_move == "X":
            cells[cords_1d] = "O"
            previous_move = "O"
        else:
            cells[cords_1d] = "X"
            previous_move = "X"
        print_field(cells)


