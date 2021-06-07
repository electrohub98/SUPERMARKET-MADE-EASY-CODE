###WELCOMING THE CUSTOMERS

print("   WELCOME TO ELECTROHUB STORE   ".center(100, "#"))
# CREATING THE DATA BASE FOR THE SUPERMARKET FOR EASY ACCESS BY CUSTOMERS
print("ITEMS IN THE STORE ARE:::::::::::::::::::::::::::::::::::::::::::::::::")
ITEM_IN_THE_STORE = ("{0},{1},{2}".format("SHIRT", "TROUSER", "BELT"))
print(ITEM_IN_THE_STORE)

import time

database = [
    {
        "shirt": "round neck",
        "price": 14
    },
    {
        'trouser': "jean",
        "price": 19
    },
    {
        "belt": "leather belt",
        "price": 98
    }

]

##MAKING THE PURCHASE AND THE TRANSACTIONS

profit = 0


def confirm_purchase(choice, store):
    for item in store:
        if item.get(choice):
            return item, store

    return f"{choice} not available in store!"


def is_transaction_succesful(money_received, good_cost):
    if money_received >= good_cost:
        global profit
        profit = good_cost
        change = round(money_received - good_cost, 2)
        return True, change
    else:
        print("Sorry that's not enough money")
        return False


machine_is_on = True

while machine_is_on:
    choice = input(f"Which item would you like to buy? ").lower().strip()
    order = confirm_purchase(choice, database)

    price = order[0]['price']
    print(order)
    print(f"Price of the {order[0][choice]} is #{price}")

    print("what is your payment medium")
    time.sleep(2)
    payment_card = str(input("enter card type(mastercard or verve):"))

    time.sleep(2)
    money_received = float(input("Please make payment: "))
    cleared = is_transaction_succesful(money_received, price)
    if cleared:
        print(f"Here's your order and a change of {cleared[1]} .Thanks for patronising our store Enjoy your day")
