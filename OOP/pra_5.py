class Employee:
    def __init__(self, id, name, salary):
        self.__id = id
        self.name = name
        self.__salary = salary

    def display(self):
        print(
            f"\nEmployee ID: {self.__id}\nEmployee Name: {self.name}\nSalary: {self.__salary}"
        )

    def get_emp_id(self):
        return self.__id

    def get_emp_salary(self):
        return self.__salary

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, id, name, salary, dept):
        super().__init__(id, name, salary)
        self.dept = dept

    def get_manager_id(self):
        return super().get_emp_id()

    def get_manager_salary(self):
        return super().get_emp_salary()

    def display(self):
        manager_id = self.get_manager_id()
        manager_salary = self.get_manager_salary()
        print(
            f"\nManager ID: {manager_id}\nManager Name: {self.name}\nDepartment: {self.dept}\nSalary:{manager_salary}"
        )

    def __del__(self):
        return super().__del__()


class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language

    def get_developer_id(self):
        return super().get_emp_id()

    def get_developer_salary(self):
        return super().get_emp_salary()

    def display(self):
        developer_id = self.get_developer_id()
        developer_salary = self.get_developer_salary()
        print(
            f"\nDeveloper ID: {developer_id}\nDeveloper Name: {self.name}\nProgramming Language: {self.programming_language}\nSalary:{developer_salary}"
        )

    def __del__(self):
        return super().__del__()


devs = []
managers = []
other_employees = []


while True:
    print("\n--- Choose another operation ---\n")
    print("\n1.Create an Employee")
    print("2.Create a Manager")
    print("3.Create a Developer")
    print("4.Show Details")
    print("5.Exit:\n")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("\nThanks for visiting!\n")
        break
    elif choice == 1:
        id = int(input("\nPlease assign an id: "))
        name = input("Enter the name of employee: ")
        salary = int(input("Enter the salary of employee: "))
        e1 = Employee(id, name, salary)
        other_employees.append(e1)
    elif choice == 2:
        id = int(input("\nPlease assign an id: "))
        name = input("Enter the name of manager: ")
        salary = int(input("Enter the salary of manager: "))
        dept = input("Enter the department of manager: ")

        if issubclass(Manager, Employee):
            m1 = Manager(id, name, salary, dept)
            managers.append(m1)
    elif choice == 3:
        id = int(input("\nPlease assign an id: "))
        name = input("Enter the name of developer: ")
        salary = int(input("Enter the salary of manager: "))
        lang = input("Enter the programming_language: ")

        if issubclass(Developer, Employee):
            d1 = Developer(id, name, salary, lang)
            devs.append(d1)

    elif choice == 4:
        print("\nChoose details to show:")
        print("1.Employees")
        print("2.Managers")
        print("3.Developers")
        view_choice = int(input("Enter your choice: "))

        if view_choice == 1:
            for emp in other_employees:
                emp.display()
        elif view_choice == 2:
            for mng in managers:
                mng.display()
        elif view_choice == 3:
            for dev in devs:
                dev.display()
        else:
            print("\nInvalid Choice!")
    else:
        print("\nInvalid Choice!")
