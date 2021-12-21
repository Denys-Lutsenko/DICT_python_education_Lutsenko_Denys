'''rock_paper_scissors 4-st'''
from random import choice

MOVES = ('rock', 'paper', 'scissors')
WINNING_MOVES = {MOVES[i]: MOVES[(i + 1) % len(MOVES)]
                 for i, _ in enumerate(MOVES)}


def get_rating(username: str) -> int:
    with open('rating.txt', mode='r', encoding='utf_8') as file:
        for line in file:
            name, score = line.strip().split(' ')
            if name == username:
                return int(score)
    return 0


def main():
    username = input('Enter your name:')
    print(f'Hello, {username}')
    rating = get_rating(username)

    while True:
        user_move = input()

        if user_move == '!exit':
            print('Bye!')
            break
        elif user_move == '!rating':
            print(f'Your rating: {rating}')
        elif user_move not in MOVES:
            print('Invalid input')
        else:
            computer_move = choice(MOVES)
            if computer_move == user_move:
                rating += 50
                print(f'There is a draw {computer_move}')
            elif computer_move == WINNING_MOVES[user_move]:
                print(f'Sorry, but the computer chose {computer_move}')
            else:
                rating += 100
                print(f'Well done. The computer chose {computer_move}',
                      'and failed')


if __name__ == '__main__':
    main()




