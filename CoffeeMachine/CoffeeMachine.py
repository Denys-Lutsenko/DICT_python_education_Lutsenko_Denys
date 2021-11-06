# CoffeeMachine 1-st

print('Starting to make a coffee\nGrinding coffee beans\nBoiling water\n'
      'Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n'
      'Pouring some milk into the cup\nCoffee is ready!')

# CoffeeMachine 2-st

numb_of_water = 200
numb_of_milk = 50
numb_of_beans = 15

cup_counter = int(input("Write how many cups of coffee you will need: "))
water = cup_counter*numb_of_water
milk = cup_counter*numb_of_milk
beans = cup_counter*numb_of_beans

print("For " + str(cup_counter) + " cups of coffee you will need:")
print(str(water) + "ml of water")
print(str(milk) + "ml of milk")
print(str(beans) + "g of coffee beans")
