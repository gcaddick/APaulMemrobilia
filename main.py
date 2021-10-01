from StockInventory.add_item import add_item
import csv
from tabulate import tabulate

"""
Plan for System

Sections
    - Product Inventory
        - Spreadsheet "Database"
            - Name of product
            - Product number
            - Cost of product
            - Authenticated or not
            - Product Description
        - Allows warehouse management to add to the inventory

    - Customer Database
        - Spreadsheet "Database"
            - Name of customer
            - Address of customer
            - Payment for customer
            - Products they have bought
        - can search for previous customers
            maybe edit previous customers
        - add new customers

    - Purchase Order
        - Formed by sales automatically
        - spreadsheet
            - customer details
            - product bought
            - Order Progress
                - Sends automated email to customer at checkpoints
        - Sends notification to warehouse of purchase request
        - sends notification to accounts of purchase request
"""

Item = add_item()
