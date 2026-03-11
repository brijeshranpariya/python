import numpy as np

from helper import *

while True:
    print("\n==============================")
    print("      NUMPY ANALYZER")
    print("==============================")
    print("Choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    print("==============================")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("\nThank you!!")
        break

    elif choice == 1:
        create_numpy_array()

    elif choice == 2:
        perform_math_ops()

    elif choice == 3:
        combine_split_array()

    elif choice == 4:
        search_sort_filter_array()

    elif choice == 5:
        perform_agg_statistical_ops()
