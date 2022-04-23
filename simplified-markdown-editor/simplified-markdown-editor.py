formatters = (
    'plain',
    'bold',
    'italic',
    'header',
    'ordered-list',
    'unordered-list',
    'link',
    'inline-code',
    'new-line'
)

commands = (
    '!help',
    '!done',
)

while True:
    user_choice = input('- Choose a formatter: ')
    if user_choice == '!help':
        print("Available formatters:", ' '.join(formatters))
        print("Available commands: ", ' '.join(commands))
    elif user_choice == '!done':
        break
    elif user_choice not in formatters:
        print('Unknown formatting type or command')
