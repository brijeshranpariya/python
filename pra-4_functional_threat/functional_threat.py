def calculate_factorial(number):
    if number in [0, 1]:
        return 1
    return number * calculate_factorial(number - 1)


print("Welcome to the Data Analyzer and Transformer Program\n")
parsed_elements = []
while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistic (Return Multiple Values)")
    print("7. Exit Program\n")
    choice = int(input("Please enter your choice:"))

    if choice == 7:
        print("\n Thank you!")
        break
    elif choice == 1:
        elements = input("\nEnter data for a 1D array(separated by space):").split(" ")

        for elem in elements:
            parsed_elements.append(int(elem))
        print("\nData has been stored successfully!")
    elif choice == 2:
        print("\nData Summary:")
        print("- Total elements: ", len(parsed_elements))
        print("- Minimum value: ", min(parsed_elements))
        print("- Maximum value: ", max(parsed_elements))
        print("- Sum of all value: ", sum(parsed_elements))

    elif choice == 3:
        number = int(input("\nEnter a number to calculate its factorial:"))
        factorial = calculate_factorial(number)
        print(f"\nFactorial of {number} is: {factorial}")
    elif choice == 4:
        threshold = int(
            input("\nEnter a threshold value to filter out data above this value: ")
        )
        filtered_data = filter(lambda e: e > threshold, parsed_elements)
        print(f"\nFiltered Data (values >= {threshold})")
        for elem in filtered_data:
            print(elem, end=" ")
    elif choice == 5:
        print("\nChoose sorting option:\n1.Ascending\n2.Descending ")
        sort_type = int(input("\nEnter your choice: "))
        if sort_type == 1:
            print("Sorted Data in Ascending Order: ")
            parsed_elements.sort()
            for elem in parsed_elements:
                print(elem, end=" ")
        elif sort_type == 2:
            print("Sorted Data in Ascending Order: ")
            parsed_elements.sort(reverse=True)
            for elem in parsed_elements:
                print(elem, end=" ")
    elif choice == 6:
        print("\nData Statistics:")
        print("- Average value: ", (sum(parsed_elements) / len(parsed_elements)))
