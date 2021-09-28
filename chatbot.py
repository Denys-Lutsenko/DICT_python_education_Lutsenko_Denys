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
        else:
            print( 'Completed, have a nice day!')
        break
