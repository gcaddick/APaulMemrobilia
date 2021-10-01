import csv
from tabulate import tabulate


class Inventory:
    def __init__(self, product_name, item_number, location, cost, authentication, prod_desc):
        self.product_name = product_name
        self.item_number = item_number
        self.location = location
        self.cost = cost
        self.authentication = authentication
        self.product_description = prod_desc

    def add_item(self):
        with open("InventoryList.csv", mode='a', newline='') as inventory_list:
            new_item = [self.product_name, self.item_number, self.location, self.cost,
                        self.authentication, self.product_description]
            writer = csv.writer(inventory_list)
            writer.writerow(new_item)
        return "Item Added"

    @staticmethod
    def checking_the_stock():
        stock_keys = ["Product Name", "Item Number", "Location", "Cost", "Authentication", "Product Description"]
        stock_list = []
        with open("InventoryList.csv", mode='r', newline='') as inventory_list:
            reader = csv.reader(inventory_list)
            stock_list.append(stock_keys)
            for row in reader:
                stock_list.append(row)
            print(tabulate(stock_list, headers="firstrow"))
            print("\n")
        return stock_list


class Menu(Inventory):
    def __init__(self):
       pass

    def search_inventory(self):
        user_answer = self
        found_item = False
        stock_list = Inventory.checking_the_stock()
        specific_item = []
        specific_item.append(stock_list[0])
        for item in stock_list:
            if user_answer in item:
                specific_item.append(item)
                found_item = True
        if not found_item:
            return False
        else:
            return specific_item

    @staticmethod
    def user_menu():
        choice = input("\nWhat would you like to do? Please indicate with the corresponding number\n"
                       "\t(1) Check Stock\n"
                       "\t(2) Add item to inventory\n"
                       "\t(3) Remove item from inventory\n"
                       "\t(4) Quit\n")
        while len(choice) != 1 or not choice.isnumeric():
            choice = input("\nWhat would you like to do? Please indicate with the corresponding number\n"
                           "\t(1) Check Stock\n"
                           "\t(2) Add item to inventory\n"
                           "\t(3) Remove item from inventory\n"
                           "\t(4) Quit\n")
        choice = int(choice)
        if choice == 1:
            stock_list = Inventory.checking_the_stock()

            user_answer = input("Do you want to search the inventory? (y/n): ").lower()
            while not user_answer.isalpha():  # Only accepts the alphabet
                user_answer = input("Do you want to search the inventory? (y/n): ").lower()
            if "y" in user_answer:  # Accepts any answer with "y" in
                search = True
                while search:
                    user_answer = input("What would you like to search?: ")
                    results = Menu.search_inventory(user_answer)
                    if not results:
                        print("No results")
                        user_answer = input("Try again? (y/n): ").lower()
                        while not user_answer.isalpha():  # Only accepts the alphabet
                            user_answer = input("Try again? (y/n): ").lower()
                    else:
                        print("Results: ")
                        print(tabulate(results, headers="firstrow"))
                        print("\n")
                    user_answer = input("Do you want to search the inventory? (y/n): ").lower()
                    while not user_answer.isalpha():  # Only accepts the alphabet
                        user_answer = input("Do you want to search the inventory? (y/n): ").lower()
                    if "y" not in user_answer:  # Accepts any answer with "y" in
                        search = False

            else:
                return
        elif choice == 2:
            Menu.user_adding_item()
        elif choice == 3:
            remove_item = False
            while not remove_item:
                user_answer = input("What would you like to search?: ")
                specific_item = Menu.search_inventory(user_answer)
                print(tabulate(specific_item, headers="firstrow"))
                user_answer = input("Is this the result you want to remove?(y/n): ").lower()
                while not user_answer.isalpha():  # Only accepts the alphabet
                    user_answer = input("Is this the result you want to remove?(y/n): ").lower()
                if "y" in user_answer:
                    #user_removing_item(specific_item)
                    print("this would now delete the item")
                else:
                    user_answer = input("Do you still want to remove an item?(y/n): ").lower()
                    while not user_answer.isalpha():  # Only accepts the alphabet
                        user_answer = input("Do you still want to remove an item?(y/n): ").lower()
                    if "y" not in user_answer:
                        remove_item = True
            stock_list = Menu.checking_the_stock()
        else:
            quit()

        return

    # def user_removing_item(self):
    #     specific_item = self
    #     if len(specific_item) > 2:
    #
    #     else:
    #         specific_item = specific_item[1]






    @staticmethod
    def user_adding_item():
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

            print(f"\nProduct Name: {name}")
            print(f"Item Number: {item_number}")
            print(f"Location of Item: {location}")
            print(f"Cost of item: {cost}")
            print(f"The product is authenticated: {authenticated}")
            print(f"Product description: {product_description}")

            user_answer = input("Are these details correct? (y/n)").lower()
            while not user_answer.isalpha():  # Only accepts the alphabet
                user_answer = input("Are these details correct? (y/n)").lower()
            if "y" in user_answer:  # Accepts any answer with "y" in
                completed = True

                already_name = Menu.search_inventory(name)
                already_number = Menu.search_inventory(item_number)

                if (not already_number) and (not already_name):
                    item_to_add = Inventory(name, item_number, location, cost, authenticated, product_description)
                    Inventory.add_item(item_to_add)
                else:
                    print("The item is already in the inventory: ")
                    print(tabulate(already_name, headers="firstrow"))
            else:
                completed = False
        return

user_quit = False
while not user_quit:
    user1 = Menu()
    user1.user_menu()
    # Menu.user_menu()
