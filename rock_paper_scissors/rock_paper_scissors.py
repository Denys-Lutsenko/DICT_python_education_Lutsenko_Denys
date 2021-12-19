'''rock_paper_scissors 3-st'''
from random import choice
MOVES = {'scissors': 'rock', 'paper': 'scissors',
            'rock': 'paper'}


def main():
    while True:
        user_move = input()
        random_choice = choice(list(MOVES))
        if user_move == '!exit':
            print('Bye!')
            break
        if user_move not in list(MOVES):
            print('Invalid input')
            continue
        if user_move == random_choice:
            print(f'There is a draw ({random_choice})')
        elif random_choice == MOVES[user_move]:
            print(f'Sorry, but the computer chose {random_choice}')
        else:
            print(f'Well done. The computer chose {random_choice} and failed')


if __name__ == '__main__':
    main()