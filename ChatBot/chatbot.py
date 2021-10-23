print("Hello! My name is Alex")
print("I was created in 2021")
while True:
    a = input()
    g = 'hello' and 'hi'
    if a != g:
        print('And say hello or hi?!')
    if 'hello' and 'hi' in a:
        b = input("Please, remind me your name: ")
        print('What a great name you have, ', b, '!')
        print("Let me guess your age. ")
        print("Enter remainders of dividing your age by 3, 5 and 7:")
        remainder3 = int(input())
        remainder5 = int(input())
        remainder7 = int(input())
        age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        print("Your age is ", age, " that's a good time to start programming!")
        print('Now I will prove to you that I can count to any number you want. You want to test?')
        number = int(input())
        i = None
        for i in range(number + 1):
            print(i, "!")
        break
print("Let's test your programming knowledge.")
input()
ls = [
    ("def a(b, c, d): pass Что делает следующий код? ", "1"),
    ("print(type(1 / 2)) Что выведет следующий код, при его исполнении? ", "3"),
    ("Где правильно создана переменная?", "2"),
    ("Какая библиотека отвечает за время?", "4"),
]

var = [("1. Определяет функцию, которая ничего не делает. ", "2. Определяет список и инициализирует его. ",
        "3. Определяет функцию, которая передает параметры. ", "4. Определяет пустой класс.  "),
       ("1. class 'int' ", "2. class 'number' ", "3. class 'float' ", "4. class 'double' "),
       ("1. $num = 2", "2. num = float(2)", "3. var num = 2", "4. Нет подходящего варианта"),
       ("1. localtime", "2. clock", "3. Time", "4. time"),
       ]

question = 0
wrong_answer = 0

while True:
    print(ls[question][0])
    for j in range(len(var[question])):
        print(var[question][j])
    answer = input("Ответ: ")
    if answer == ls[question][1]:
        print("Completed, have a nice day!")
        question = question + 1
        if question == 1:
            break
        continue
    else:
        print("Please, try again.")
        #wrong_answer = wrong_answer + 1
        #print("Неправильных ответов", wrong_answer)
print('')
print("Congratulations, have a nice day!")
