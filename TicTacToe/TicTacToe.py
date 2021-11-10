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
# X wins = XXXOO__O_
# O wins = XOOOXOXXO
# Draw =   XOXOOXXXO
# Game not finished = XO_OOX_X_
# Impossible = XO_XO_XOX
while True:
    board = list(input('Enter cells: '))
    print('---------')
    print(f"""| {board[0]} {board[1]} {board[2]} |
| {board[3]} {board[4]} {board[5]} |
| {board[6]} {board[7]} {board[8]} |""")
    print('---------')
    a = 0
    condition = []
    for b in range(3):
        try:
            vert = [board[b], board[b + 3], board[b + 6]]
            diag_1 = [board[0], board[4], board[8]]
            diag_2 = [board[2], board[4], board[6]]
            horz = board[a:a + 3]
            if board.count('X') - board.count('O') > 1 or board.count('O') - board.count('X') > 1:
                condition.append('Impossible')
            if diag_1.count(board[0]) == 3 or diag_2.count(board[2]) == 3:
                condition.append(f'{board[0]} wins')
            if horz.count(board[a]) == 3:
                condition.append(f'{board[a]} wins')
            if vert.count(board[b]) == 3:
                condition.append(f'{board[b]} wins')
            a += 3
        except IndexError:
            continue
    if len(condition) == 0:
        if '_' in board:
            print('Game not finished')
        else:
            print('Draw')
    else:
        if condition.count(condition[0]) == len(condition):
            print(condition[0])
        else:
            print('Impossible')
            break


