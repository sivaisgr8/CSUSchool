import sys
import io
import os


def main():
    # Dictionary containing Course Number and Room Number
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # Dictionary containing Course Number and Instructor
    instructor_name = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # Dictionary containing Course Number and Meeting Time
    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # Get course number from user input
    course_number = input("Please input the course number (e.g., CSC101): ").strip().upper()

    # Validates the course if exists prints the information else provides list for available courses
    if course_number in room_numbers:
        print(f"\nInformation for the requested Course {course_number}:")
        print("-" * 30)
        print(f"Room Number:  {room_numbers[course_number]}")
        print(f"Instructor:   {instructor_name[course_number]}")
        print(f"Meeting Time: {course_times[course_number]}")
    else:
        print(f"\nError: Course {course_number} was not found in our system.")
        print('Please select from these Available courses:', ', '.join(room_numbers.keys()))

if __name__ == "__main__":
    main()