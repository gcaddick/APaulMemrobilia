class UserMenu:
    def __init__(self):
        pass

    @staticmethod
    def user_menu():
        choice = input("What would you like to do? Please indicate with the corresponding number\n"
                       "\t(1) Check Stock\n"
                       "\t(2) Add item to inventory\n"
                       # "\t(3) Remove item from inventory\n"
                       "\t(4) Quit\n")
        while len(choice) != 1 or not choice.isnumeric():
            choice = input("What would you like to do? Please indicate with the corresponding number\n"
                           "\t(1) Check Stock\n"
                           "\t(2) Add item to inventory\n"
                           # "\t(3) Remove item from inventory\n"
                           "\t(4) Quit\n")
        choice = int(choice)
        return choice

    @staticmethod
    def user_wants_search_stock():
        searching_stock = input("Do you want to search the inventory? (y/n): ").lower()
        while not searching_stock.isalpha():  # Only accepts the alphabet
            searching_stock = input("Do you want to search the inventory? (y/n): ").lower()
        if "y" in searching_stock:  # Accepts any answer with "y" in
            return True
        return False

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
            while not cost.isnumeric():
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
            print(f"Product description: {product_description}\n")

            user_answer = input("Are these details correct? (y/n)").lower()
            while not user_answer.isalpha():  # Only accepts the alphabet
                user_answer = input("Are these details correct? (y/n)").lower()
            if "y" in user_answer:  # Accepts any answer with "y" in
                completed = True
            else:
                completed = False
        return name, item_number, location, cost, authenticated, product_description