class SettingAndGetting:
    def __init__(self, product_name, item_number, location, cost, authentication, prod_desc):
        self.product_name = product_name
        self.item_number = item_number
        self.location = location
        self.cost = cost
        self.authentication = authentication
        self.product_description = prod_desc

    def GetProductDetails(self):
        array_of_details = [self.product_name, self.item_number, self.location, self.cost,
                            self.authentication, self.product_description]
        return array_of_details
