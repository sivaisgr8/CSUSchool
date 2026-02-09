import sys
import io
import os

class ItemToPurchase: # Class to represent an item to purchase based on specification


    def __init__(self):
        #Default constructor -that initializes all attributes to default values as mentioned in specification
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        #Formating to match the specification: item quantity @ $price = $total
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:} = ${total:}")


def main():
    # Main function to get user input values and calculate total cost

    # Input for Item 1
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # Input for Item 2
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # Output total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculation Logic for Total value
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost:}")



main()