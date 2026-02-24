def offer_initial_menu():
    print("\n========================================")
    print("Welcome to Multi-Utility Toolkit")
    print("========================================\n")
    print("Choose an option: ")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers.(UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("========================================")
    choice = int(input("Enter your choice: "))
    return choice


def calculate_factorial(number):
    if number in [0, 1]:
        return 1

    return number * calculate_factorial(number)
