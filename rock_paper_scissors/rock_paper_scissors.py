'''rock_paper_scissors 5-st'''
from random import choice


class RockPaperScissors:

    def __init__(self):
        """Initialize the game."""
        self.username = None
        self.rating = 0
        self.moves = None
        self._user_move = None
        self._computer_move = None

    def get_rating(self):
       # Получает рейтинг польховотеля из 'rating.txt'

        with open('rating.txt', mode='r', encoding='utf_8') as file:
            for line in file:
                name, score = line.strip().split(' ')
                if name == self.username:
                    self.rating = int(score)

    def get_options(self, csv: str):
        # получает параметыры игры из строки

        if csv:
            moves = csv.split(',')
        else:
            moves = ['rock', 'paper', 'scissors']

        if len(moves) % 2:
            self.moves = {move: i for i, move in enumerate(moves)}
        else:
            raise ValueError('Expected an odd number of options.')

    def get_winner(self) -> str:
        #определяет птобедителя  или объявляет ничью

        delta = (self.moves[self._computer_move] -
                 self.moves[self._user_move]) % len(self.moves)
        threshold = len(self.moves) // 2
        if delta == 0:
            return 'draw'
        elif delta <= threshold:
            return 'computer'
        else:
            return 'player'

    def play(self):
        #это основной игровой цикл
        # запрашиваеться имя пользователя, параметры,
        # получиается рейтинг и начнинаеться игра
        self.username = input('Enter your name: ')
        print(f'Hello, {self.username}')
        self.get_rating()
        self.get_options(input())
        print("Okay, let's start")

        while True:
            self._user_move = input()

            if self._user_move == '!exit':
                print('Bye!')
                break
            elif self._user_move == '!rating':
                print(f'Your rating: {self.rating}')
            elif self._user_move not in self.moves:
                print('Invalid input')
            else:
                self._computer_move = choice(list(self.moves))
                winner = self.get_winner()
                if winner == 'draw':
                    self.rating += 50
                    print(f'There is a draw {self._computer_move}')
                elif winner == 'computer':
                    print(
                        f'Sorry, but the computer chose {self._computer_move}')
                else:
                    self.rating += 100
                    print(
                        f'Well done. The computer chose {self._computer_move}',
                        'and failed')


if __name__ == '__main__':
    game = RockPaperScissors()
    game.play()
