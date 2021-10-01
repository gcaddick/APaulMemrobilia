import csv
from SettingAndGetting import SettingAndGetting
from tabulate import tabulate


class ReadCSV:
    def __init__(self, product_name, item_number, location, cost, authentication, prod_desc):
        self.product_name = product_name
        self.item_number = item_number
        self.location = location
        self.cost = cost
        self.authentication = authentication
        self.product_description = prod_desc

    # Creates the stock list using a dictionary of dictionaries
    # the key for each item in the stock is the item number
    # then within the second dictionary, the keys are the names of the product details
    # product name, item number and so on
    def creating_stock_list(self, stock_list):
        stock_list[str(self.item_number)] = self
        return stock_list

    # Creates a table to print the inventory list
    # self is the temporary item variable
    def tabling_stock_list(self, stock_keys):
        list_of_stock = []
        for keys in self:
            # Setting and Getting, changes the attributes into a list of the details
            list_of_stock.append(SettingAndGetting.GetProductDetails(self[keys]))
        print("\n")
        # Prints the stock list using function tabulate, with the column headers being the stock keys
        print(tabulate(list_of_stock, headers=stock_keys))
        print("\n")

    @staticmethod
    def user_search_stock(search_input, stock_keys):
        stock_list = ReadCSV.readingCSV(stock_keys)  # creates the stock list
        item_keys = list(stock_list.keys())  # creates list of the keys
        list_of_stock = []
        searched_stock = []
        item_in_inventory = False
        for key in item_keys:
            list_of_stock.append(SettingAndGetting.GetProductDetails(stock_list[key]))  # Gets product details and
            # stores as a list
        for item in list_of_stock:
            if search_input in item:  # compares the search input with each item
                searched_stock.append(item)  # Appends the found item to the stock to print
                item_in_inventory = True
        if item_in_inventory:
            print(tabulate(searched_stock, headers=stock_keys))

    def duplicate_search_stock(self,stock_keys):
        stock_list = ReadCSV.readingCSV(stock_keys)  # retrieves stock list
        item_keys = list(stock_list.keys())
        if self.item_number in item_keys:  # checks keys of dict for the same item number
            print("This is a duplicate ID")
            overwrite = input("Do you want to overwrite? (y/n): ").lower()
            while not overwrite.isalpha():
                overwrite = input("Do you want to overwrite? (y/n): ").lower()
            if "y" in overwrite:
                return True
            else:
                return False
        else:
            return True

    @staticmethod
    def readingCSV(stock_keys):
        stock_list = {}
        with open("InventoryList.csv", mode='r', newline='') as inventory_list:
            line_as_dict = csv.DictReader(inventory_list, fieldnames=stock_keys)
            for line in line_as_dict:
                temp_item = ReadCSV(line[stock_keys[0]], line[stock_keys[1]], line[stock_keys[2]],
                                    line[stock_keys[3]], line[stock_keys[4]], line[stock_keys[5]])
                stock_list = ReadCSV.creating_stock_list(temp_item, stock_list)
        return stock_list

    def writing_to_csv(self):
        with open("InventoryList.csv", mode='a', newline='') as inventory_list:
            writer = csv.writer(inventory_list)
            add_item = SettingAndGetting.GetProductDetails(self)
            writer.writerow(add_item)




