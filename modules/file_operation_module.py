def file_operations():
    print("\nFile Operations: ")
    print("\n1. Create a New File")
    print("2. Write to a File")
    print("3. Read from a File")
    print("4. Append to File")
    print("5. Back to Main Menu")

    choice = int(input("\nEnter your choice: "))
    if choice == 5:
        return
    elif choice == 1:
        filename = input("\nEnter file name(With Extension) to create: ")
        with open(f"./modules/{filename}", "w") as f:
            print(f"{filename} created successfully.")
    elif choice == 2:
        filename = input("\nEnter file name(With Extension) to write: ")
        data = input("Enter content to write: ")
        try:
            with open(f"./modules/{filename}", "w") as f:
                f.write(data)
            print("\nData written successfully.")
        except FileNotFoundError as e:
            print(f"File does not exist. Please enter valid file name!")
    elif choice == 3:
        filename = input("\nEnter file name(With Extension) to read: ")
        try:
            with open(f"./modules/{filename}", "r") as f:
                content = f.read()
                print("\nFile Content:")
                print(content)
        except FileNotFoundError:
            print("File does not exist.")
    elif choice == 4:
        filename = input("\nEnter file name(With Extension) to append: ")
        data = input("Enter content to append: ")
        try:
            with open(f"./modules/{filename}", "a") as f:
                f.write("\n" + data)
            print("\nData appended successfully.")
        except FileNotFoundError as e:
            print(f"File does not exist. Please enter valid file name!")
    else:
        print("Invalid choice. Please try again.")
