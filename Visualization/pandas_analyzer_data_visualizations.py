import pandas as pd
from helper import *

df = None

while True:

    print("\n======== Data Analysis & Visualization Program ========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform Dataframe Operations")
    print("4. Handling Missing Data")
    print("5. Generate Descriptive statistics")
    print("6. Data Visualization")
    print("8. Exit")
    print("=======================================================")

    choice = int(input("\nEnter your choice: "))

    if choice == 8:
        print("\nThank you!")
        break

    elif choice == 1:
        load_dataset()

    elif choice == 2:

        explore_data()

    elif choice == 3:

        perform_dataframe_ops()

    elif choice == 4:

        handle_missing_data()

    elif choice == 5:

        describe_dataset()

    elif choice == 6:

        create_charts()

    else:
        print("\nInvalid choice!")
