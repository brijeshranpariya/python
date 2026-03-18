from helper import LibraryDashboard

l1 = LibraryDashboard()

while True:
    print("\n======== E-Library Data Insights Dashboard ========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Generate statistics summary")
    print("3. Filter Transaction")
    print("4. Generic Report")
    print("5. Exit")
    print("=======================================================")

    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        print("\nThank You!")
        break
    elif choice == 1:

        try:
            l1.load_data("./practical_exam/library_transactions_500_rows.csv")
            print("Dataset Loaded Successfully!\n")
        except FileNotFoundError:
            print("File not found. Please check the file name.")

    elif choice == 2:
        l1.calculate_statistics()
    elif choice == 3:
        choice = int(
            input(
                "\n1.Date \n2.Genre \n3.User ID \nSelect the filed to filter the users: "
            )
        )
        if choice == 1:
            date_to_filter = input("\nEnter the date to filter(YYYY-MM-DD): ")
            l1.filter_transaction("Date", date_to_filter)
        elif choice == 2:
            genre = input("\nEnter the genre to filter:")
            l1.filter_transaction("Genre", genre)
        elif choice == 3:
            user_id = input("\nEnter the user id(Uxxxx) to filter:")
            l1.filter_transaction("User ID", user_id)
    elif choice == 4:
        l1.generate_report()
