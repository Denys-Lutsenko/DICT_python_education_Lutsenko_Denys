import random

inp_string = f'{random.randrange(2, 10)} {random.choice(["+", "-", "*"])} {random.randrange(2, 9)}'
print(inp_string)
print("Right!" if int(input()) == eval(inp_string) else "Wrong!")
