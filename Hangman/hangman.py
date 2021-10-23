import random
import re
import string


"""слов минимум 6
de=len(x)
exit()
не прави буква
повторы 
не прав + повтор+несколько букв+ не символ а цифра 
"""

print("HANGMAN"  "\nThe game will be available soon.")
words = ['python', 'bask', "java", "javascript", "php"]
the_word = random.choice(words)
print("The word has", len(the_word), 'letters')
right = ['-'] * len(the_word)
wrong = []
health = 8
len_word = len(the_word)
used_letters = ""
char = ()
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'}

def update():
    for i in right:
        print(i, end='')
    print()
update()


while True:
    print('health', health)
    conjec = input("conjecture a lettre: ")
    conjec = conjec.lower()
    # print(bool(alphabet.intersection(set(conjec.lower()))))
    f = bool(alphabet.intersection(set(conjec.lower())))
    if f == False:
        print('Please enter a lowercase English letter.')
    if conjec in used_letters:
        print("You`ve already guessed this letter.")
    if len(conjec) > 1:
        print("You should input a single letter.")
    if conjec == len(wrong):
        health += 1


    else:

        used_letters += conjec

        if conjec in the_word:
            index = 0
            for i in the_word:
                if i == conjec:
                    right[index] = conjec
                index += 1
            update()
        else:
            if conjec not in wrong:
                wrong.append(conjec)

                print("You`ve already guessed this letter.")

            else:
                if conjec in wrong:
                    wrong.append(conjec)
                    health += 1
                print(wrong)
            health -= 1
            if health == 0:
                print("You lost!")
                break
            #if len(wrong) > health:
            continue
        if '-' not in right:
            print("You survived!")
            print('I conject', the_word)
            break
