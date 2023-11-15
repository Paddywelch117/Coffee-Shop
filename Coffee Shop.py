# This is a new coffee shop programme that allows you to order as much coffee as you wish
# The programme works by asking your name, what coffee you want, how many coffees and calculates the total.
import math

prices = {
    1: 3.00,
    2: 3.20,
    3: 3.50,
    4: 3.70,
    5: 4.20
}

class CoffeeShop:
    global data
    data = {}

    def promptUser(self):
        print("\nHello, Welcome to Paddy's Coffee Shop!\n" "What is your Name?")
        name = input("")
        print("\nHello " + name + ", What would you like from the Menu?\n\n")

        print("\n\tMENU\n\n\t1) Black Coffee\n\t2) Espresso\n\t3) Latte\n\t4) Cappuccino\n\t5) Frappuccino")
        order = int(input("\t"))

        print("\nQuantity: ")
        quantity = int(input())

        if order == 1: # black coffee
            total = prices[1] * quantity
            data['name'] = name
            data['type'] = 'Black Coffee'
            data['total'] = str(math.floor(total))

        elif order == 2:
            total = prices[2] * quantity
            data['name'] = name
            data['type'] = 'Espresso'
            data['total'] = str(math.floor(total))

        elif order == 3:
            total = prices[3] * quantity
            data['name'] = name
            data['type'] = 'Latte'
            data['total'] = str(math.floor(total))

        elif order == 4:
            total = prices[4] * quantity
            data['name'] = name
            data['type'] = 'Cappuccino'
            data['total'] = str(math.floor(total))

        elif order == 5:
            total = prices[5] * quantity
            data['name'] = name
            data['type'] = 'Frappuccino'
            data['total'] = str(math.floor(total))

        return data

    def receipt(self, promptUser):

        print("Receipt for customer")

        name = promptUser['name']
        type = promptUser['type']
        total = promptUser ['total']

        print("Name: " + name
              +"\nCoffee type: " + type
              +"\nTotal: £" + total + "\n")

coffee = CoffeeShop()
coffee.receipt(coffee.promptUser())

print("\n Would you like another drink?")
choice = input("")

if choice != "No":
    coffee.receipt(coffee.promptUser())
else:
    print("\nHave a lovely day!")
    exit()