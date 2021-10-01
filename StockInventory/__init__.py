from ReadCSV import ReadCSV
from UserMenu import UserMenu

stock_keys = ["Product Name", "Item Number", "Location", "Cost", "Authentication", "Product Description"]
user_quit = False
while not user_quit:
    user_menu_choice = UserMenu.user_menu()

    ##################################
    # user_menu_choice can be one of #
    # (1) check/search stock         #
    # (2) Add item to stock          #
    # (4) Quit system                #
    ##################################

    if user_menu_choice == 1:
        stock_list = ReadCSV.readingCSV(stock_keys)  # Creates a inventory list as a dictionary
        ReadCSV.tabling_stock_list(stock_list, stock_keys)  # Prints the inventory for the user
        user_search_choice = UserMenu.user_wants_search_stock()  # finds out if the user wants to search for a
        # specific item
        if user_search_choice:
            search = True
            search_input = input("\nWhat would you like to search?: ")
            while search:
                ReadCSV.user_search_stock(search_input, stock_keys)  # Creates a list of the results and prints table
                # of list
                user_search_choice = UserMenu.user_wants_search_stock()  # Asks if they want to search again
                if user_search_choice:
                    search_input = input("\nWhat would you like to search?: ")
                else:
                    search = False
    elif user_menu_choice == 2:
        # Add item to stock
        name, item_number, location, cost, authenticated, product_description = UserMenu.user_adding_item()  # Gets
        # the details from the user for the new item to add
        item_to_add = ReadCSV(name, item_number, location, cost, authenticated, product_description)  # creates an
        # instance of that item
        overwrite = ReadCSV.duplicate_search_stock(item_to_add, stock_keys)  # Checks to see if ID has already been used
        if overwrite:  # If the user wants to overwrite or is not a duplicate
            ReadCSV.writing_to_csv(item_to_add)  # Writes to the csv file
            stock_list = ReadCSV.readingCSV(stock_keys)  # re-reads the file and prints it
            ReadCSV.tabling_stock_list(stock_list, stock_keys)
        else:
            print("Item not added")
            stock_list = ReadCSV.readingCSV(stock_keys)  # reads the file and prints it
            ReadCSV.tabling_stock_list(stock_list, stock_keys)

    # elif user_menu_choice == 3:
    #     # Remove item from stock
    #     pass
    else:
        quit()
