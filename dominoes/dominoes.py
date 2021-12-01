'''dominoes 2-st'''

import random


# выбирает случайные n элементов из набора и удаляет их из начального набора
def get_domino_pieces(n):
    domino_pieces = []
    for i in range(n):
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


# повторяется пока не будет установлена стартовая костяшка
while True:
    # создает полный набор домино
    domino_set = [[a, b] for a in range(7) for b in range(7) if a <= b]
    computer_pieces = get_domino_pieces(7)
    player_pieces = get_domino_pieces(7)
    first_domino = max(max_double(computer_pieces), max_double(player_pieces))
    if first_domino:
        break


# печатает сообщение о текущем статусе
def message(st):
    return {
        'computer': '\nStatus: Computer is about to make a move. Press Enter to continue...',
        'player': '\nStatus: It\'s your turn to make a move. Enter your command.'}[st]


domino_snake = []
if first_domino in player_pieces:
    player_pieces.remove(first_domino)
    status = 'computer'
else:
    computer_pieces.remove(first_domino)
    status = 'player'
domino_snake.extend(first_domino)

print('=' * 70)
print('Stock size:', len(domino_set))
print('Computer pieces:', str(len(computer_pieces))+'\n')
print(str(domino_snake)+'\n')
print('Your pieces:')
for i in range(len(player_pieces)):
    print(str(i + 1) + ':' + str(player_pieces[i]))
print(message(status))

