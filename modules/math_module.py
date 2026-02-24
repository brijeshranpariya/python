from helper import calculate_factorial
import math


def mathematical_operations():
    print("\nMathematical Operations:")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")
    print("5. Back to Main Menu")
    choice = int(input("Enter you choice: "))

    if choice == 5:
        return

    elif choice == 1:
        number = int(input("\nEnter the number to calculate the factorial: "))

        fact = calculate_factorial(number)
        print(f"\nFactorial of {number} is {fact}.`")

    elif choice == 2:
        principal = float(input("\nEnter principal amount: "))
        rate = float(input("Enter annual interest rate (in %): "))
        rate = rate / 100
        time = float(input("Enter time (in years): "))
        n = int(input("Enter number of times interest compounded per year: "))

        amount = principal * (1 + rate / n) ** (n * time)
        compound_interest = amount - principal

        print(f"\nFinal Amount: {amount:.2f}")
        print(f"Compound Interest: {compound_interest:.2f}")

    elif choice == 3:
        print("\n--- Trigonometric Operations ---")
        print("1. sin")
        print("2. cos")
        print("3. tan")

        trig_choice = input("Select operation (1-3): ")
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        if trig_choice == "1":
            print("\nsin =", math.sin(radians))
        elif trig_choice == "2":
            print("\ncos =", math.cos(radians))
        elif trig_choice == "3":
            print("\ntan =", math.tan(radians))
        else:
            print("\nInvalid trigonometric choice.")

    elif choice == 4:
        print("\n------ Area of Geometric Shapes ------")
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Triangle")
        choice = int(input("\nEnter your choice (1-4): "))
        if choice == 1:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"\nArea of Rectangle: {area:.2f}")

        elif choice == 2:
            side = float(input("Enter side length: "))
            area = side**2
            print(f"\nArea of Square: {area:.2f}")

        elif choice == 3:
            radius = float(input("Enter radius: "))
            area = math.pi * radius**2
            print(f"\nArea of Circle: {area:.2f}")

        elif choice == 4:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"\nArea of Triangle: {area:.2f}")

        else:
            print("Invalid choice.")
    else:
        print("Invalid choice. Please try again.")
