'''DinnerParty 3-st'''
import random

num_of_friends = int(input("Enter the number of friends joining (including you):\n"))
print()
friends_dictionary = {}

if num_of_friends <= 0:
    print("No one is joining for the party")
else:

    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(num_of_friends):
        name = input()
        friends_dictionary.update({name: 0})
    bill = int(input("\nEnter the total amount:\n"))
    if bill / num_of_friends % 10 == 0:
        for i in friends_dictionary:
            friends_dictionary[i] = int(bill / num_of_friends)
    else:
        for i in friends_dictionary:
            friends_dictionary[i] = round(bill / num_of_friends, 2)
    choice = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if choice == 'Yes' or "yes":
        friends_list = list(friends_dictionary.keys())
        lucky_friend = random.choice(friends_list)
        print("\n{} is the lucky one!".format(lucky_friend))
    else:
        print("No one is going to be lucky")
