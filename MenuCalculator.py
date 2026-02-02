import sys
import io
import os

def menu_calculator():
    # Two Arrays/lists  to store menu and prices
    menu_items = []
    menu_item_prices = []

    print("--- Restaurant Bill Calculator ---")
    print("Please enter 'done' when you are finished adding items.\n")

    while True:
        item_name = input("Enter menu item name: ")
        if item_name.lower() == 'done':#Breaking the loop to enter menu items when done is entered
            break

        try:
            price = float(input(f"Enter price for '{item_name}': ")) #Float so that price can be in decimals
            # Adding menu and prices to the arrays
            menu_items.append(item_name)
            menu_item_prices.append(price)
        except ValueError:#Validating if entered amount is an number
            print("Invalid price. Please enter a number.")

    # 1. Calculating Total Menu Price
    # using built-in sum()  function
    menu_total = sum(menu_item_prices)

    # 2. Calculate 7% Sales Tax for the total menu price
    sales_tax = menu_total * 0.07

    # 3. Calculate 18% Tip on the "Total + Tax" amount
    total_plus_tax = menu_total + sales_tax
    tip_amount = total_plus_tax * 0.18

    # 4. Sum Total-Total including Menu+Tax+Tip
    sum_total = total_plus_tax + tip_amount

    # Displaying the Results
    print("\n" + "=" * 30)
    print("        FINAL RECEIPT")
    print("=" * 30)

    # Printing all the items entered with price for validating
    for i in range(len(menu_items)):
        print(f"{menu_items[i]:<20} ${menu_item_prices[i]:>7.2f}")

    print("-" * 30)
    print(f"{'Total Menu Price:':<20} ${menu_total:>7.2f}")
    print(f"{'Sales Tax (7%):':<20} ${sales_tax:>7.2f}")
    print(f"{'Tip (18%):':<20} ${tip_amount:>7.2f}")
    print("-" * 30)
    print(f"{'SUM TOTAL:':<20} ${sum_total:>7.2f}")
    print("=" * 30)


menu_calculator()