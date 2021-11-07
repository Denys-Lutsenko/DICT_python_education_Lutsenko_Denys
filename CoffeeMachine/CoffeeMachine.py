'''CoffeeMachine 1-st'''

# print('Starting to make a coffee\nGrinding coffee beans\nBoiling water\n'
#       'Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n'
#       'Pouring some milk into the cup\nCoffee is ready!')

'''CoffeeMachine 2-st'''


# numb_of_water = 200
# numb_of_milk = 50
# numb_of_beans = 15

# cup_counter = int(input("Write how many cups of coffee you will need: "))
# water = cup_counter*numb_of_water
# milk = cup_counter*numb_of_milk
# beans = cup_counter*numb_of_beans
#
# print("For " + str(cup_counter) + " cups of coffee you will need:")
# print(str(water) + "ml of water")
# print(str(milk) + "ml of milk")
# print(str(beans) + "g of coffee beans")

'''CoffeeMachine 3-st'''

# numb_of_water = 200
# numb_of_milk = 50
# numb_of_beans = 15

# water = int(input("Enter how much water: "))
# milk = int(input("Enter how much milk: "))
# beans = int(input("Enter how much beans: "))
# cup_counter = int(input("Write how many cups of coffee you will need: "))
# var_water = water // numb_of_water
# var_milk = milk // numb_of_milk
# var_beans = beans // numb_of_beans
# numb = min([var_water, var_milk, var_beans])
# print(numb)
# if numb == cup_counter:
#     print("Yes, I can make that amount of coffee")
# elif numb > cup_counter:
#     print("Yes, I can make that amount of coffee (and even " + str(numb - cup_counter) + " more than that)")
# else:
#     print("No, I can make only " + str(numb) + " cups of coffee")

'''CoffeeMachine 4-st'''

# water = 400
# milk = 540
# beans = 120
# cups = 9
# money = 550
#
#
# def content():
#         print('The coffee machine has:')
#         print(f'{water} of water')
#         print(f'{milk} of milk')
#         print(f'{beans} of coffee beans')
#         print(f'{cups} of disposable cups')
#         print(f'{money} of money')
#         print("============================")
#
# content()
#
# def select_coffe() -> int:
#     return int(input('What do you want to buy?'
#                      ' 1 - espresso, 2 - latte, 3 - cappuccino: '))
# def buy():
#         global water, milk, beans, money, cups
#         user_coffee = select_coffe()
#         if user_coffee == 1:
#             print('espresso')
#             water -= 250
#             beans -= 16
#             cups -= 1
#             money += 4
#         elif user_coffee == 2:
#             print('latte')
#             water -= 350
#             milk -= 75
#             beans -= 20
#             cups -= 1
#             money += 7
#         elif user_coffee == 3:
#             print('cappuccino')
#             water -= 200
#             milk -= 100
#             beans -= 12
#             cups -= 1
#             money += 6
#
#
# def fill():
#         global water, milk, beans, money, cups
#
#         add_water = int(input("Write how many ml of water you want to add: "))
#         water += add_water
#         add_milk = int(input("Write how many ml of milk you want to add: "))
#         milk += add_milk
#         add_beans = int(input("Write how many grams of coffee beans you want to add: "))
#         beans += add_beans
#         add_cups = int(input("Write how many disposable coffee cups you want to add: "))
#         cups += add_cups
#
#
# def take():
#         global money
#         print(f'I gave you "{money}')
#         money = 0
#
#
# def order():
#       choice_to_order = input('Write action (1.buy, 2.fill, 3.take): ')
#       if choice_to_order == "1":
#         buy()
#         content()
#       elif choice_to_order == "2":
#         fill()
#         content()
#       elif choice_to_order == "3":
#         take()
#         content()
#
# order()


'''CoffeeMachine 5-st'''

# water = 400
# milk = 540
# beans = 120
# cups = 9
# money = 550
# conjec = 0
#
#
# def order():
#     choice_to_order = input('Write action (buy, fill, take, remaining, exit): ')
#     if choice_to_order == "buy":
#         buy()
#         return 'buy'
#     elif choice_to_order == "fill":
#         fill()
#         return 'fill'
#     elif choice_to_order == "take":
#         take()
#         return 'take'
#     elif choice_to_order == 'remaining':
#         print('')
#         content()
#         return 'remaining'
#     elif choice_to_order == 'exit':
#         return 'exit'
#
#
# def content():
#         print('The coffee machine has:')
#         print(f'{water} of water')
#         print(f'{milk} of milk')
#         print(f'{beans} of coffee beans')
#         print(f'{cups} of disposable cups')
#         print(f'{money} of money')
#         print("============================")
#
# def select_coffe():
#     return str(input('What do you want to buy?\n'
#                      ' 1 - espresso, 2 - latte, 3 - cappuccino, '
#                      'back – to main menu: '))
#
# def check_ingredients():
#     global water, milk, beans, money, cups
#     if 0 > water:
#         return "Sorry, not enough water"
#     elif 0 > milk:
#         return "Sorry, not enough milk"
#     elif 0 > beans:
#         return "Sorry, not enough coffee_beans"
#     elif 0 > cups:
#         return "Sorry, not enough disposable cups"
#
# def buy():
#         global water, milk, beans, money, cups
#         user_coffee = select_coffe()
#         # content()
#         if user_coffee == '1':
#             print('You choosed the espresso')
#             water -= 250
#             beans -= 16
#             cups -= 1
#             money += 4
#             if check_ingredients() == None:
#                 print('I have enough resources, making you a coffee!')
#             else:
#                 print(check_ingredients())
#             return 'espresso'
#         elif user_coffee == '2':
#             print('You choosed the latte')
#             water -= 350
#             milk -= 75
#             beans -= 20
#             cups -= 1
#             money += 7
#             if check_ingredients() == None:
#                 print('I have enough resources, making you a coffee!')
#             else:
#                 print(check_ingredients())
#             return 'latte'
#         elif user_coffee == '3':
#             print('You choosed the cappuccino')
#             water -= 200
#             milk -= 100
#             beans -= 12
#             cups -= 1
#             money += 6
#             if check_ingredients() == None:
#                 print('I have enough resources, making you a coffee!')
#             else:
#                 print(check_ingredients())
#             return 'cappuccino'
#         elif user_coffee == 'back':
#             return order()
#
#
#
# def fill():
#         global water, milk, beans, money, cups
#         content()
#         add_water = int(input("Write how many ml of water you want to add: "))
#         water += add_water
#         add_milk = int(input("Write how many ml of milk you want to add: "))
#         milk += add_milk
#         add_beans = int(input("Write how many grams of coffee beans you want to add: "))
#         beans += add_beans
#         add_cups = int(input("Write how many disposable coffee cups you want to add: "))
#         cups += add_cups
#         content()
#
#
# def take():
#         global money
#         print(f'I gave you {money}')
#         money = 0
#         print(f'Money in the coffee machine {money}')
#
#
#
# while order() != "exit":
#     conjec = order()


'''CoffeeMachine 6-st'''

class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

        self.order()

    def order(self):
        self.choice_to_order = input("Write action (buy, fill, take, remaining, exit): ")
        if self.choice_to_order == "buy":
            self.buy()
        elif self.choice_to_order == "fill":
            self.fill()
        elif self.choice_to_order == "take":
            self.take()
        elif self.choice_to_order == "exit":
            exit()
        elif self.choice_to_order == "remaining":
            self.content()

    def content(self):
        print("============================")
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print("============================")
        self.return_()

    def check_ingredients(self):
        self.not_ingredients = ""
        if self.water - self.decrease[0] < 0:
            self.not_ingredients = "water"
        elif self.milk - self.decrease[1] < 0:
            self.not_ingredients = "milk"
        elif self.beans - self.decrease[2] < 0:
            self.not_ingredients = "coffee beans"
        elif self.cups - self.decrease[3] < 0:
            self.not_ingredients = "disposable cups"
        if self.not_ingredients != "":
            print(f"Sorry, not enough {self.not_ingredients}")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True

    def subtraction_of_ingredients(self):
        self.water -= self.decrease[0]
        self.milk -= self.decrease[1]
        self.beans -= self.decrease[2]
        self.cups -= self.decrease[3]
        self.money += self.decrease[4]

    def buy(self):
        self.user_coffee = input("What do you want to buy? "
                            "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.user_coffee == '1':
            self.decrease = [250, 0, 16, 1, 4]
            if self.check_ingredients():
                self.subtraction_of_ingredients()

        elif self.user_coffee == '2':
            self.decrease = [350, 75, 20, 1, 7]
            if self.check_ingredients():
                self.subtraction_of_ingredients()

        elif self.user_coffee == "3":
            self.decrease = [200, 100, 12, 1, 6]
            if self.check_ingredients():
                self.subtraction_of_ingredients()

        elif self.user_coffee == "back":
            self.return_()

        self.return_()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        self.content()
        self.return_()

    def take(self):
        print(f"I gave you {self.money}")
        self.money -= self.money
        self.return_()

    def return_(self):
        self.order()


CoffeeMachine(400, 540, 120, 9, 550)



