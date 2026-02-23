
import sys
import io
import os

#Building on Previous Shopping Cart code from Module 4, using function with same names
class ItemToPurchase:
    # Updated to include item_description with a default value
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    # Step 4: ShoppingCart class definition as per defined specification
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

#Add Function
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

#Remove Function
    def remove_item(self, item_name: str):
        """Removes the first item whose name matches item_name."""
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

#Modify Function Updates an item's description, price, or quantity if they aren't the default values
    def modify_item(self, modified_item: ItemToPurchase):

        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

#Returns the total quantity of all items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

#Returns the total cost of everything in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

#Prints the entire shopping cart contents and total price.
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}\n")

        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart():.0f}")

#Prints descriptions of all items currently in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()

#Displaying a menu options as per specification
def print_menu(cart):
    # Step 5: Menu functionality and validation loop
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    input_choice = ''
    while input_choice != 'q':
        print(menu)
        input_choice = input("Choose an option:\n").strip()

        # Validation loop for valid commands
        valid_choice = ['a', 'r', 'c', 'i', 'o', 'q']
        while input_choice not in valid_choice:
            input_choice = input("Choose an option:\n").strip()

        # Execute chosen command
        if input_choice == 'o':
            # Step 6: Implement Output shopping cart
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif input_choice == 'i':
            # Step 6: Implement Output items' descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif input_choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_desc = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_qty = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_desc, item_price, item_qty)
            cart.add_item(new_item)

        elif input_choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif input_choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_qty = int(input("Enter the new quantity:\n"))
            # Passing default "none" and 0.0 to trigger modify logic properly
            mod_item = ItemToPurchase(item_name, "none", 0.0, item_qty)
            cart.modify_item(mod_item)

def main():
    # Getting user input to setup initial cart details
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    my_cart = ShoppingCart(customer_name, current_date)

    # Launch the menu
    print_menu(my_cart)

if __name__ == "__main__":
    main()