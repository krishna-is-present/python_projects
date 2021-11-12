MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice = ""


def serve():
    global resources, choice
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ")
    if choice == "espresso":
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                return "repeat"
        return MENU["espresso"]["cost"]
    elif choice == "latte":
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                return "repeat"
        return MENU["latte"]["cost"]
    elif choice == "cappuccino":
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                return "repeat"
        return MENU["cappuccino"]["cost"]
    elif choice == "report":
        print(f" Water: {resources['water']} \n Coffee: {resources['coffee']} \n Milk: {resources['milk']}")
        return "repeat"
    elif choice == "off":
        return "off"


def add(a, b, c, d):
    sumof = float(a * .25 + b * .1 + c * .05 + d * .01)
    return sumof


def cal():
    if choice == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                choice == "repeat"
                coffee()
    elif choice == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                choice == "repeat"
                coffee()
    elif choice == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        for key,value in resources.items():
            if value < 0:
                print(f"Sorry there is not enough {key}.")
                choice == "repeat"
                coffee()


def coffee():
    isContinue = True
    while isContinue == True:
        selection = serve()
        if selection == "repeat":
            continue
        elif selection == "off":
            print("Machine turning off for maintainence")
            return
        else:
            print("Please insert coins: ")
            quarters = int(input("How many quaters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            cost = add(quarters, dimes, nickles, pennies)
            total = float(cost - selection)
            if cost - selection <= 0:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                cal()
                print(f"Here is ${total} in change.")
                print(f"Here is your {choice}. Enjoy!")
coffee()
