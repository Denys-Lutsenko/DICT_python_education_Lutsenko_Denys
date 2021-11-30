'''dominoes 1-st'''

import random

global domino_set


# выбирается n случайных элементов из набора
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
    domino_snake = max(max_double(computer_pieces), max_double(player_pieces))
    if domino_snake:
        break

if domino_snake in player_pieces:
    player_pieces.remove(domino_snake)
    status = 'computer'
else:
    computer_pieces.remove(domino_snake)
    status = 'player'
print('Stock pieces:', domino_set)
print('Computer pieces:', computer_pieces)
print('Player pieces:', player_pieces)
print('Domino snake:', [domino_snake])
print('Status:', status)
