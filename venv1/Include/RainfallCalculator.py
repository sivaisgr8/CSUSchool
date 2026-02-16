# Rainfall Average Calculator

import sys
import io
import os


def main():
    # Get number of years from user
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            if num_years > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a whole number.")

    # Initialize variables to keep track of totals
    total_rainfall = 0.0
    total_months = 0
    # Month Names for easier tracking and reporting
    month_names = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    # Dictionary Variable to track rainfall totals for each month (across all years)
    monthly_totals = {month: 0.0 for month in month_names}

    # Outer loop for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        print("-" * 10)

        # Inner loop for each of the 12 months
        for month in range(1, 13):

            # Prompt input  for rainfall for each month
            while True:
                try:
                    rainfall = float(input(f"Enter rainfall (inches) for {month_names[month - 1]}: "))
                    if rainfall >= 0:
                        break
                    else:
                        print("Rainfall cannot be negative. Please try again.")
                except ValueError:
                    print("Please enter a number.")

            # Add monthly rainfall to the running total
            total_rainfall += rainfall
            # Increment the total month counter
            total_months += 1

            # Add to monthly total
            monthly_totals[month_names[month - 1]] += rainfall


    # Calculate the average rainfall per month
    average_rainfall = total_rainfall / total_months

    # Display the final report
    print("\n--- Rainfall Report ---")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

    # Display average rainfall for each calendar month
    print("\nAVERAGE RAINFALL BY MONTH (across all years)")

    for month_name in month_names:
        monthly_avg = monthly_totals[month_name] / num_years
        print(f"{month_name:12s}: {monthly_avg:6.2f} inches")
    print("=" * 50)

main()