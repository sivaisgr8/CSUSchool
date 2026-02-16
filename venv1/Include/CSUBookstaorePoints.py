# CSU Bookstore Rewards Point Calculator

import sys
import io
import os


def main():
    print("\n--- CSU Global Bookstore Book Club Rewards ---")
    # User Enters for the number of books purchased this month
    try:
        books_purchased = int(input("Enter the number of books purchased this month: "))

        # Points to be awarded based on the tiers specified
        #Loop breaks as soon as one logic is satisfied
        if books_purchased < 0:
            print("Please enter a valid number (0 or greater).")
            return
        elif books_purchased < 2:  # Covers 0      and 1 book
            points = 0
        elif books_purchased <= 3:  # Covers 2-3 books
            points = 5
        elif books_purchased <= 5:  # Covers 4-5 books
            points = 15
        elif books_purchased <= 7:  # Covers 6-7 books
            points = 30
        else:  # Covers 8 or more books
            points = 60

        # Display the result
        print(f"Purchases: {books_purchased} book(s)")
        print(f"Points Awarded: {points}")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


main()
