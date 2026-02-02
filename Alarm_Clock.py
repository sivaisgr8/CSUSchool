import sys
import io
import os
import datetime
import time


def get_alarm_time():#Input program for getting alarm time

    print("=" * 50)
    print("          ALARM CLOCK PROGRAM")
    print("=" * 50)

    # Get current time
    current_time = datetime.datetime.now()
    print(f"\nCurrent Date & Time: {current_time.strftime('%B %d, %Y %H:%M:%S')}") #using strftime function format date
    print(f"Current Time (24-hour): {current_time.strftime('%H:%M')}") #using strftime function format date

    # 1. Get basic time input for setting alarm
    try:
        hour = int(input("Enter the alarm hour: "))
        minute = int(input("Enter the alarm minute: "))

        # 2. Validating for 12 hour vs 24 hours
        if 1 <= hour <= 12:
            input_time = input("Is this a 12-hour format? (y/n): ").lower().strip()
            if input_time == 'y':
                period = input("AM or PM?: ").upper().strip()
                if period == "PM" and hour != 12:
                    hour += 12
                elif period == "AM" and hour == 12:
                    hour = 0

        return hour, minute
    except ValueError:
        print("Invalid input. Please enter numbers.") #Validating for numbers in alarm
        return get_alarm_time()


def calculate_alarm():#Calculating Alarm
    # Get user inputs
    target_h, target_m = get_alarm_time()

    try:
        delay_input = input("Enter delay in hours (press Enter for 0): ")
        delay_hours = float(delay_input) if delay_input else 0
    except ValueError:
        delay_hours = 0

    # Get current time to calculate alarm
    now = datetime.datetime.now()
    print(f"\n--- Current System Time: {now.strftime('%Y-%m-%d %H:%M:%S')} ---")

    # Step 1: Add delay to the current time to get the "Search Start" point
    reference_time = now + datetime.timedelta(hours=delay_hours)

    # Step 2: Set the alarm to the target hour/min on the reference date
    alarm_time = reference_time.replace(hour=target_h, minute=target_m, second=0, microsecond=0)

    # Step 3: If the calculated time is in the past (relative to our reference),
    # it means the next matching time is tomorrow7
    if alarm_time < reference_time:
        alarm_time += datetime.timedelta(days=1)

    print(f"Alarm successfully set for: {alarm_time.strftime('%Y-%m-%d %H:%M:%S')} (24h format)")
    # Calculate time until alarm
    time_until = alarm_time - now
    total_seconds = int(time_until.total_seconds())
    hours_until = total_seconds // 3600
    minutes_until = (total_seconds % 3600) // 60
    seconds_until = total_seconds % 60

    print(f"\nTime until alarm: {hours_until} hours, {minutes_until} minutes, {seconds_until} seconds")
    print("=" * 50)

    return alarm_time


target = calculate_alarm()
