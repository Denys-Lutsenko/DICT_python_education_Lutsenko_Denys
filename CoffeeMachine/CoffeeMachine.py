# CoffeeMachine 1-st

print('Starting to make a coffee\nGrinding coffee beans\nBoiling water\n'
      'Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n'
      'Pouring some milk into the cup\nCoffee is ready!')

# CoffeeMachine 2-st

numb_of_water = 200
numb_of_milk = 50
numb_of_beans = 15

# cup_counter = int(input("Write how many cups of coffee you will need: "))
# water = cup_counter*numb_of_water
# milk = cup_counter*numb_of_milk
# beans = cup_counter*numb_of_beans
#
# print("For " + str(cup_counter) + " cups of coffee you will need:")
# print(str(water) + "ml of water")
# print(str(milk) + "ml of milk")
# print(str(beans) + "g of coffee beans")

# CoffeeMachine 3-st

water = int(input("Enter how much water: "))
milk = int(input("Enter how much milk: "))
beans = int(input("Enter how much beans: "))
cup_counter = int(input("Write how many cups of coffee you will need: "))
var_water = water // numb_of_water
var_milk = milk // numb_of_milk
var_beans = beans // numb_of_beans
numb = min([var_water, var_milk, var_beans])
print(numb)
if numb == cup_counter:
    print("Yes, I can make that amount of coffee")
if numb > cup_counter:
    print("Yes, I can make that amount of coffee (and even " + str(numb - cup_counter) + " more than that)")
else:
    print("No, I can make only " + str(numb) + " cups of coffee")
