def create_user(user_details):
    students.append(user_details)


def display_users():
    for std in students:
        subjects = ", ".join(std["subjects"])
        print(
            f"\nStudent ID: {std['id']} | Name: {std['name']} | Age: {std['age']} | Grade: {std['grade']} | Subjects: {subjects}"
        )


def update_user(id):
    std_details = ["name", "age", "grade", "dob", "subjects"]
    fields = input(
        "\nPlease enter the fields you want to update(comma-separated): "
    ).split(",")
    for std in students:
        if std["id"] == id:
            for field in fields:
                if field in std_details:
                    fieldName = input(f"\nEnter the new {field} of {std['name']}: ")
                    if field == "subjects":
                        std[field] = fieldName.split(",")
                    else:
                        std[field] = fieldName


def delete_user(id):
    for std in students:
        if std["id"] == id:
            students.remove(std)


def display_offered_student(id):
    for std in students:
        if std["id"] == id:
            print(" ,".join(std["subjects"]))


print("Welcome to student Data Organizer!")
students = []
while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")
    choice = int(input("\nEnter Your Choice: "))

    if choice == 6:
        print("\nThank You!")
        break
    elif choice == 1:
        print("\nEnter student details: \n")
        student = {
            "id": int(input("Student Id: ")),
            "name": input("Name: "),
            "age": int(input("Age:")),
            "grade": (input("Grade:")),
            "dob": (input("Date of Birth(YYYY-MM-DD):")),
            "subjects": ((input("Subjects (comma-separated):")).split(",")),
        }
        create_user(student)
        print("\nStudent Added Successfully!\n")
    elif choice == 2:
        if len(students) == 0:
            print("\nNo student found!\n")
        else:
            display_users()
    elif choice == 3:
        std_id = int(input("\nPlease enter the id of student: "))
        update_user(std_id)

    elif choice == 4:
        std_id = int(input("\nPlease enter the id of student: "))
        delete_user(std_id)
        print("\nStudent Deleted Successfully!\n")
    elif choice == 5:
        std_id = int(input("\nPlease enter the id of student: "))
        display_offered_student(std_id)
    else:
        print("\nInvalid Choice!")
