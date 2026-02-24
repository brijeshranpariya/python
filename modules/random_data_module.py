import random
import string


def random_data_generation():
    print("\nRandom Data Generation:")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")
    print("5. Back to Main Menu")
    choice = int(input("Enter you choice: "))

    if choice == 5:
        return

    elif choice == 1:
        start_number = int(input("\nEnter the starting number of range: "))
        end_number = int(input("Enter the ending number of range: "))

        if start_number < end_number:
            print("\nStarting number should be greater than ending number.")
        else:
            print(f"\nRandom Number: {random.randint(start_number,end_number)}")

    elif choice == 2:
        l = []
        length = int(input("\nEnter the length of list: "))
        while length > 0:
            l.append(random.randint(1, 10))
            length = length - 1
        print(f"\nRandom list: {l}")
    elif choice == 3:
        l = []
        length = int(input("\nEnter the max length of password: "))
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k=length))
        print(f"Random alphanumeric string: {random_string}")

    elif choice == 4:
        l = []
        while len(l) < 6:
            l.append(str(random.randint(1, 9)))
        print(f"\nOTP: {"".join(l)}")
    else:
        print("Invalid choice. Please try again.")
