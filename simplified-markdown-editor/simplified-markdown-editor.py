def get_accepted_values(prompt, accepted_values, failure_prompt='Invalid Input!'):
    while True:
        value = input(prompt)
        if value in accepted_values:
            return value
        print(failure_prompt)


class BaseFormatter:
    def __init__(self):
        pass

    def __call__(self):
        inputs = self.get_input()
        return self.make_output(inputs)

    def get_input(self):
        raise NotImplemented("A formatter must implement get_input!")

    def make_output(self, inputs):
        raise NotImplemented("A formatter must implement make_output!")


class TextInputFormatter(BaseFormatter):
    @staticmethod
    def get_input():
        text = input('Text: ')
        return {'text': text}


class HeaderFormatter(TextInputFormatter):
    accepted_levels = [str(i) for i in range(1, 7)]

    def get_input(self):
        failure_prompt = 'The level should be within the range of 1 to 6'
        level = get_accepted_values('Level: ', self.accepted_levels, failure_prompt)
        inputs = super().get_input()
        inputs['level'] = level
        return inputs

    @staticmethod
    def make_output(inputs):
        return '#' * int(inputs.get('level')) + f" {inputs.get('text')}\n"


class TextFormatFormatter(TextInputFormatter):
    format_string = None

    def make_output(self, inputs):
        if not isinstance(self.format_string, str):
            raise ValueError('format_string must be a string!')
        return self.format_string % inputs


class PlainFormatter(TextFormatFormatter):
    format_string = '%(text)s'


class BoldFormatter(TextFormatFormatter):
    format_string = '**%(text)s**'


class ItalicFormatter(TextFormatFormatter):
    format_string = '*%(text)s*'


class InlineCodeFormatter(TextFormatFormatter):
    format_string = '`%(text)s`'


class LinkFormatter(TextFormatFormatter):
    format_string = '[%(label)s](%(url)s)'

    @staticmethod
    def get_input():
        label = input('Label: ')
        url = input('URL: ')
        return {'label': label, 'url': url}


class NewLineFormatter(BaseFormatter):
    @staticmethod
    def get_input():
        return {}

    @staticmethod
    def make_output(inputs):
        return '\n'


class BaseListFormatter(BaseFormatter):

    def get_row_prefix(self, row_num):
        raise NotImplemented('A List Formatter must implement get_row_prefix!')

    @staticmethod
    def get_input():
        while True:
            no_rows = int(input('Number of rows: '))
            if int(no_rows) > 0:
                break
            print('The number of rows should be greater than zero')
        rows = []
        for i in range(no_rows):
            rows.append(input(f'Row #{i + 1}: '))
        return {'rows': rows}

    def make_output(self, inputs):
        rows = inputs.get('rows')
        output = []
        for index, row in enumerate(rows, start=1):
            output.append(f'{self.get_row_prefix(index)} {row}')
        return '\n'.join(output) + '\n'


class OrderedListFormatter(BaseListFormatter):
    def get_row_prefix(self, row_num):
        return f'{row_num}.'


class UnorderedListFormatter(BaseListFormatter):
    def get_row_prefix(self, row_num):
        return '*'


class MarkdownFormatter:
    formatters = (
        'plain',
        'bold',
        'italic',
        'header',
        'ordered-list',
        'unordered-list',
        'link',
        'inline-code',
        'new-line',
    )

    format_callable_map = {
        'plain': PlainFormatter(),
        'bold': BoldFormatter(),
        'italic': ItalicFormatter(),
        'header': HeaderFormatter(),
        'ordered-list': OrderedListFormatter(),
        'unordered-list': UnorderedListFormatter(),
        'link': LinkFormatter(),
        'inline-code': InlineCodeFormatter(),
        'new-line': NewLineFormatter(),
    }

    commands = (
        '!help',
        '!done',
    )

    accepted_menu_inputs = formatters + commands

    output = []

    def handle_command(self, command):
        if command == '!help':
            print("Available formatters:", ' '.join(self.formatters))
            print("Available commands: ", ' '.join(self.commands))
            return True
        if command == '!done':
            output_string = ''.join(self.output)
           

    def handle_formatter(self, formatter_key):
        formatter = self.format_callable_map.get(formatter_key)
        self.output.append(formatter())
        print(''.join(self.output))
        return True

    def handle_input(self, user_input):
        if user_input.startswith('!'):
            return self.handle_command(user_input)
        return self.handle_formatter(user_input)

    def run(self):
        prompt = '- Choose a formatter: '
        failure_prompt = 'Unknown formatting type or command'
        while True:
            user_input = get_accepted_values(prompt, self.accepted_menu_inputs, failure_prompt)
            is_okay = self.handle_input(user_input)
            if not is_okay:
                break


if __name__ == '__main__':
    MarkdownFormatter().run()