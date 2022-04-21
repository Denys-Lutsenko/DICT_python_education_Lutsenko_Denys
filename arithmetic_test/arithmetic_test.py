import random


def input_answer():
    while True:
        try:
            return int(input())
            break
        except ValueError:
            print("Incorrect format.")


count = 0
for i in range(5):
    inp_string = f'{random.randrange(2, 10)} {random.choice(["+", "-", "*"])} {random.randrange(2, 9)}'
    print(inp_string)
    if input_answer() == eval(inp_string):
        print("Right!")
        count += 1
    else:
        print("Wrong!")
print(f"Your mark is {count}/5.")
