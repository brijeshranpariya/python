from helper import offer_initial_menu
from date_time_module import date_time_operations
from math_module import mathematical_operations
from random_data_module import random_data_generation
from unique_identifier_module import generate_unique_identifier
from file_operation_module import file_operations
from module_attributes import explore_module_attributes

while True:
    choice = offer_initial_menu()

    if choice == 7:
        print("\n========================================")
        print("Thank you for using Multi-Utility Toolkit!")
        print("========================================\n")
        break
    elif choice == 1:
        date_time_operations()
    elif choice == 2:
        mathematical_operations()
    elif choice == 3:
        random_data_generation()
    elif choice == 4:
        generate_unique_identifier()
    elif choice == 5:
        file_operations()
    elif choice == 6:
        explore_module_attributes()
    else:
        print("\nInvalid Choice!\n")
