from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating objects from the classes imported
keurig = CoffeeMaker()
coffee_menu = Menu()
register = MoneyMachine()

machine_powered = True

while machine_powered:
    options = coffee_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off'.lower():
        machine_powered = False
    elif choice == 'report'.lower():
        keurig.report()
        register.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if keurig.is_resource_sufficient(drink):
            if register.make_payment(drink.cost):
                keurig.make_coffee(drink)
