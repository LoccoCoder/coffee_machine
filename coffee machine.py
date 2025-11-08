import index

Coffee_machine_resources = {
    'coffee': 300,
    'milk': 900,
    'water': 1000
}

Items = ['cost', 'water', 'milk', 'coffee']


def report():
    print("Resources available:")
    for item in range(1, 4):
        print(Items[item], ':', Coffee_machine_resources[Items[item]])


def refill():
    print("Enter the amount of coffee to be refilled in grams")
    Coffee_machine_resources['coffee'] = int(input())
    print("Enter the amount of milk to be refilled in ml")
    Coffee_machine_resources['milk'] = int(input())
    print("Enter the amount of water to be refilled in ml")
    Coffee_machine_resources['water'] = int(input())


def selection():
    print("Choose your coffee:")
    a = 1
    for coffee in index.coffee_list:
        print(a)
        print(f"{coffee['name']} ${coffee['cost']}")
        a = a + 1
    user_choice = int(input("Choose the option by the corresponding number: ")) - 1
    return user_choice


def transaction():
    choice = selection()
    if (Coffee_machine_resources['coffee'] < index.coffee_list[choice]['coffee'] or
        Coffee_machine_resources['water'] < index.coffee_list[choice]['water'] or
        Coffee_machine_resources['milk'] < index.coffee_list[choice]['milk']):
        print("Sorry, you do not have enough material to make that request. Please consider refilling the coffee machine.")
        report()
        if input("If you want to refill the coffee machine, press 'y' to continue: ") == 'y':
            refill()
    else:
        print('''Your request is noted.
Please pay the requested amount to the coffee machine.''')
        print(index.coffee_list[choice]['cost'])
        if input("Press 'y' to continue: ") == 'y':
            for k in Items:
                if k == 'cost':
                    pass
                else:
                    Coffee_machine_resources[k] = Coffee_machine_resources[k] - index.coffee_list[choice][k]
            print("Thank you, here is your coffee.")


while True:
    print("Welcome to Coffee Machine")
    print('''1. Report the resources available
2. Refill the coffee machine
3. Make a coffee
4. Exit the coffee machine''')
    value = input()
    if value == '1':
        report()
    elif value == '2':
        refill()
    elif value == '3':
        transaction()
    elif value == '4':
        break
