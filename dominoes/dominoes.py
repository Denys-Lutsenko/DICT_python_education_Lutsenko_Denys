'''dominoes 3-st'''

import random

# выбирает случайные n элементов из набора и удаляет их из начального набора
def get_domino_pieces(n):
    domino_pieces = []
    for _ in range(n):
        rn = random.randint(0, len(domino_set) - 1)
        domino_pieces.append(domino_set[rn])
        del domino_set[rn]
    return domino_pieces


# возвращает наибольший дубль в наборе домино
def max_double(pieces_list):
    doubles_list = [piece for piece in pieces_list if piece[0] == piece[1]]
    if doubles_list:
        return max(doubles_list)
    else:
        return []


# возвращает сообщение о текущем статусе
def message(st):
    return {
        'computer': '\nStatus: Computer is about to make a move. Press Enter to continue...',
        'player': '\nStatus: It\'s your turn to make a move. Enter your command.',
        'player_win': '\nStatus: The game is over. You won!',
        'computer_win': '\nStatus: The game is over. The computer won!',
        'draw': '\nStatus: The game is over. It\'s a draw!'
        }[st]


# печатает игровое поле
def current_stage(stat):
    print('=' * 70)
    print('Stock size:', len(domino_set))
    print('Computer pieces:', str(len(computer_pieces)) + '\n')
    if len(domino_snake) <= 6:
        print("".join(domino_snake) + '\n')
    else:
        print("".join(domino_snake[:3]) + '...' + "".join(domino_snake[-3:]) + '\n')
    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(str(i + 1) + ':' + str(player_pieces[i]))
    print(message(stat))


# делает один ход
def make_a_move(m, pieces):
    if m > 0:
        domino_snake.append(str(pieces[m - 1]))
        del pieces[m - 1]
    if m < 0:
        domino_snake.insert(0, str(pieces[-m - 1]))
        del pieces[-m - 1]
    if m == 0:
        pieces.extend(get_domino_pieces(1))


# устанавливает первое домино
while True:
    # генерирует полный набор домино
    domino_set = [[a, b] for a in range(7) for b in range(7) if a <= b]
    computer_pieces = get_domino_pieces(7)
    player_pieces = get_domino_pieces(7)
    first_domino = max(max_double(computer_pieces), max_double(player_pieces))
    if first_domino:
        break
domino_snake = []
if first_domino in player_pieces:
    player_pieces.remove(first_domino)
    status = 'computer'
else:
    computer_pieces.remove(first_domino)
    status = 'player'
domino_snake.append(str(first_domino))

# игроки делают ходы до конца игры
while True:
    current_stage(status)
    if status in ['player_win', 'computer_win', 'draw']:
        break
    if status == 'player':
        while True:
            try:
                move = int(input())
            except ValueError:
                print('Invalid input. Please try again.')
                continue
            if int(move) <= len(player_pieces):
                break
            print('Invalid input. Please try again.')
        make_a_move(int(move), player_pieces)
        status = 'computer'
    elif status == 'computer':
        enter = input()
        move = random.randint(-len(computer_pieces), len(computer_pieces))
        make_a_move(move, computer_pieces)
        status = 'player'
    if len(player_pieces) == 0:
        status = 'player_win'
    if len(computer_pieces) == 0:
        status = 'computer_win'
    if domino_snake[0][1] == domino_snake[-1][4] and "".join(domino_snake).count(domino_snake[0][1]) == 8:
        status = 'draw'
