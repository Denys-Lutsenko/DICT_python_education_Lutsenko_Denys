'''rock_paper_scissors 1-st'''
MOVES = ('rock', 'paper', 'scissors')
WINNING_MOVES = {MOVES[i]: MOVES[(i + 1) % len(MOVES)]
                 for i, _ in enumerate(MOVES)}
print(f'Sorry, but the computer chose {WINNING_MOVES[input()]}')
