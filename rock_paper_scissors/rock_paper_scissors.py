'''rock_paper_scissors 2-st'''
from random import choice

MOVES = ('rock', 'paper', 'scissors')
WINNING_MOVES = {MOVES[i]: MOVES[(i + 1) % len(MOVES)]
                 for i, _ in enumerate(MOVES)}


def main():
    user_move = input("Your choice: ")
    computer_move = choice(MOVES)
    if computer_move == user_move:
        print(f'There is a draw {computer_move}')

    elif computer_move == WINNING_MOVES[user_move]:
        print(f'Sorry, but the computer chose {computer_move}')
    else:
        print(f'Well done. The computer chose {computer_move}',
              'and failed')


if __name__ == '__main__':
    main()

