from datetime import datetime

dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class File:
    def __init__(self, name):
        self.name = name
        with open(f"./File_handling/{self.name}", "w") as f:
            pass

    def add_new_entry(self, content):
        with open(f"./File_handling/{self.name}", "a") as f:
            f.write(content)

        print("\nEntry Added Successfully!")

    def read_all_entries(self):
        try:
            with open(f"./File_handling/{self.name}", "r") as f:
                file_content_list = f.readlines()

                if len(file_content_list) == 0:
                    print("\nNo journal entries found. start by adding a new entry!\n")

                else:
                    print("\nYour Journal Entries: ")
                    print("------------------------------------")

                    for line in file_content_list:
                        line_list = line.split(" ")
                        time = " ".join(line_list[:2])
                        entry = " ".join(line_list[2:])
                        print("[" + time + "]")
                        print(entry)

        except FileNotFoundError as e:
            print(
                "\nThe file you are looking for, does not exist! Please try again later."
            )

    def search_entry(self, keyword):
        try:
            with open(f"./File_handling/{self.name}", "r") as f:
                file_content_list = f.readlines()

                if len(file_content_list) == 0:
                    print(f"\nNo journal entries found for the keyword: {keyword}\n")

                else:
                    print("\nMatching Entries:")
                    print("------------------------------------")
                    for line in file_content_list:
                        if keyword in line:
                            line_list = line.split(" ")
                            time = " ".join(line_list[:2])
                            entry = " ".join(line_list[2:])
                            print("[" + time + "]")
                            print(entry)

        except FileNotFoundError as e:
            print(
                "\nThe file you are looking for, does not exist! Please try again later."
            )

    def delete_all_entries(self):
        try:
            with open(f"./File_handling/{self.name}", "w") as f:
                pass

            print("\nAll journal entries have been deleted.")

        except FileNotFoundError as e:
            print("\nNo journal entries to delete.")


file = File("journal.txt")

while True:
    print("\n----------------------------------------------")
    print("\nWelcome to Personal General Manager!\n")
    print("----------------------------------------------")
    print("\nPlease select an option:")
    print("\n1.Add a New Entry")
    print("2.View All Entries")
    print("3.Search for an Entry")
    print("4.Delete All Entries")
    print("5.Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        print("\nThank you for using Personal Journal Manager, Goodbye!")
        break

    elif choice == 1:
        entry = input("\nEnter your journal entry: ") + "\n"
        entry = dt + "  " + entry
        file.add_new_entry(entry)

    elif choice == 2:
        file.read_all_entries()

    elif choice == 3:
        keyword = input("\nEnter a keyword or date to search: ")
        file.search_entry(keyword)

    elif choice == 4:
        confirmation = input(
            "\nAre you sure you want to delete all entries? (yes/no): "
        )
        if confirmation == "yes":
            file.delete_all_entries()
        else:
            print("\nThank you for confirmation! your file won't be deleted.")
