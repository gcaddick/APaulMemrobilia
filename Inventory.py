import csv
from tabulate import tabulate

import StockInventory.__init__
from StockInventory.__init__ import Inventory


def check_stock():
    # Function to check the inventory of the warehouse
    # Prints current stock selection

    inventory = {"Name of Product": [], "Item Number": [], "Location": [],
                 "Cost": [], "Authenticated": [], "Product Description": []}

    with open("InventoryList.csv", mode='r', newline='') as inventory_list:
        reader = csv.reader(inventory_list)
        for index, row in enumerate(reader):
            for i in range(len(row)):
                key = list(inventory.keys())
                key_name = str(key[i])
                inventory[key_name].append(row[i])
    print(tabulate(inventory, headers="keys"))

    user_answer = input("Do you want to search the inventory? (y/n): ").lower()
    while not user_answer.isalpha():  # Only accepts the alphabet
        user_answer = input("Do you want to search the inventory? (y/n): ").lower()
    if "y" in user_answer:  # Accepts any answer with "y" in
        search_stock(inventory)
    else:
        return

    return


def search_stock(inventory):
    user_answer = input("What would you like to search? Please indicate with the corresponding number\n"
                        "(1) Name of Product\n"
                        "(2) Item Number\n"
                        "(3) Location\n")
    while not user_answer.isnumeric():
        user_answer = input("What would you like to search? Please indicate with the corresponding number\n"
                            "(1) Name of Product\n"
                            "(2) Item Number\n"
                            "(3) Location\n")
    if user_answer == 1:
        nop = input("What is the name of the product: ")
        if nop in inventory["Name of Product"]:
            for index, item in enumerate(inventory["Name of Product"]):
                if item == nop:
                    for row in inventory:
                        print(row)
                        ########
                        # Finished here
                        # Need to print exact row
                        #######

    return


def add_item():
    # Function adds item to the stock list
    # Asks for name, item number, location of item, cost of item, whether its authenticated
    # and the product description

    completed = False

    while not completed:
        name = input("\nProduct Name: ")
        item_number = input("\nItem Number: ")
        location = input("\nLocation of Item: ")
        cost = input("\nCost of item: ")
        authenticated = input("\nThe product is authenticated (y/n): ").lower()
        if "y" in authenticated:
            authenticated = True
        else:
            authenticated = False
        product_description = input("\nProduct Description: ")

        user_answer = input("Are these details correct? (y/n)").lower()

        print(f"\nProduct Name: {name}")
        print(f"Item Number: {item_number}")
        print(f"Location of Item: {location}")
        print(f"Cost of item: {cost}")
        print(f"The product is authenticated: {authenticated}")
        print(f"Product description: {product_description}")

        while not user_answer.isalpha():  # Only accepts the alphabet
            user_answer = input("Are these details correct? (y/n)").lower()
        if "y" in user_answer:  # Accepts any answer with "y" in
            completed = True
        else:
            completed = False

    with open("InventoryList.csv", mode='a', newline='') as inventory_list:
        new_item = [name, item_number, location, cost, authenticated, product_description]
        writer = csv.writer(inventory_list)
        writer.writerow(new_item)
        #
        # new_item = {"Name of Product": name, "Item Number": item_number, "Location of Item": location,
        #             "Cost of item": cost, "The product is authenticated": authenticated,
        #             "Product description": product_description}
        # w = csv.DictWriter(inventory_list, new_item.keys())
        # w.writeheader()
        # w.writerow(new_item)

    return


def user_menu():
    choice = input("What would you like to do? Please indicate with the corresponding number\n"
                   "\t(1) Check Stock\n"
                   "\t(2) Add item to inventory\n"
                   "\t(3) Remove item from inventory\n"
                   "\t(4) Quit\n")
    while len(choice) != 1 or not choice.isnumeric():
        choice = input("What would you like to do? Please indicate with the corresponding number\n"
                       "\t(1) Check Stock\n"
                       "\t(2) Add item to inventory\n"
                       "\t(3) Remove item from inventory\n"
                       "\t(4) Quit\n")
    choice = int(choice)
    if choice == 1:
        check_stock()
    elif choice == 2:
        add_item()
    elif choice == 3:
        remove_item()
    else:
        quit()

    return


user_quit = False
while not user_quit:
    user_menu()
