from datetime import datetime
from time import time
from time import perf_counter, sleep, time


def date_time_operations():
    print("\nDatetime and Time Operations:")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates/times")
    print("3. Format date into custom format")
    print("4. Stopwatch")
    print("5. Countdown Timer")
    print("6. Back to Main Menu")
    choice = int(input("Enter you choice: "))

    if choice == 6:
        return
    elif choice == 1:
        print(f"\nCurrent Date & Time: {datetime.now()}")
    elif choice == 2:
        first_date = input("Enter the first date (YYYY-MM-DD): ")
        second_date = input("Enter the second date (YYYY-MM-DD): ")
        d1 = datetime.strptime(first_date, "%Y-%m-%d")
        d2 = datetime.strptime(second_date, "%Y-%m-%d")

        difference = abs(d2 - d1)
        print("\nDifference:", difference.days)
    elif choice == 3:
        date_input = input("\nEnter date (YYYY-MM-DD): ")
        date_obj = datetime.strptime(date_input, "%Y-%m-%d")
        format_input = input("Enter desired format (Ex. %d-%m-%Y): ")
        print(f"\nFormatted Date: {date_obj.strftime(format_input)}")
    elif choice == 4:
        print("\nPress ENTER to start the stopwatch, and then again to stop it:")
        input()
        print("Stopwatch started")
        start_time = perf_counter()
        input()
        print("Stopwatch stopped")
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
    elif choice == 5:
        start_time = int(input("\nEnter start time(In Minutes) for countdown: "))
        seconds = start_time * 60
        current_time = datetime.now()
        print("\nCount down starts at", current_time)
        sleep(seconds)
        current_time = datetime.now()
        print("\nTime Up at ", current_time)
    else:
        print("Invalid choice. Please try again.")
