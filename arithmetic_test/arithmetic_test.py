import random


def input_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Wrong format! Try again.")


def input_level():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    while True:
        try:
            lev = int(input())
            if lev in {1, 2}:
                return lev
            else:
                raise ValueError
        except ValueError:
            print("Incorrect format.")


def task_1():
    c = 0
    for i in range(5):
        inp_string = f'{random.randrange(2, 10)} {random.choice(["+", "-", "*"])} {random.randrange(2, 10)}'
        print(inp_string)
        if input_answer() == eval(inp_string):
            print("Right!")
            c += 1
        else:
            print("Wrong!")
    return c


def task_2():
    c = 0
    for i in range(5):
        inp_num = random.randrange(11, 30)
        print(inp_num)
        if input_answer() == inp_num * inp_num:
            print("Right!")
            c += 1
        else:
            print("Wrong!")
    return c


level = input_level()
if level == 1:
    count = task_1()
else:
    count = task_2()
y_n = input(f"Your mark is {count}/5. Would you like to save the result? Enter yes or no.\n")
if y_n.lower() in {'yes', 'y'}:
    name = input("What is your name?\n")
    with open("results.txt", "a+") as file:
        file.write(f"{name}: {count}/5 in level {level}")
        file.write("(simple operations with numbers 2-9)" if level == 1 else "integral squares of 11-29")
    file.close()
    print('The results are saved in "results.txt".')

