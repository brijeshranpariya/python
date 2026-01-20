print("Welcome to Pattern Generator and Number Analyzer")
while True:
    print("Select an option: ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("Exiting the program. Good bye!")
        break

    elif choice == 1:
        number_of_row = int(input("Enter the number of rows for the pattern: "))

        print("Pattern:")

        for i in range(1, number_of_row + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of range: "))
        end = int(input("Enter the end of range: "))
        sum = 0

        for i in range(start, end + 1):
            sum += i
            if i % 2 == 0:
                print("Number ", i, "is Even")
            else:
                print("Number ", i, "is Odd")

        print("Sum of all numbers from ", start, "to", end, "is: ", sum)
