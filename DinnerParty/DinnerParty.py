'''DinnerParty 2-st'''

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
    bill = int(input("\nEnter the total bill: "))
    if bill / num_of_friends % 10 == 0:
        for i in friends_dictionary:
            friends_dictionary[i] = int(bill / num_of_friends)
    else:
        for i in friends_dictionary:
            friends_dictionary[i] = round(bill / num_of_friends, 2)
    print("\n{}".format(friends_dictionary))
