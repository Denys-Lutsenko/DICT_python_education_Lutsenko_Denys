'''DinnerParty 1-st'''
num_of_friends = int(input("Enter the number of friends joining (including you): \n"))
print()
friends_dictionary = {}

if num_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    while len(friends_dictionary) != num_of_friends:
        name = input("")
        friends_dictionary.update({name: 0})
    print("\n{}".format(friends_dictionary))
