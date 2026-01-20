# # practical-1
# marks = int(input("Enter your marks: "))
# print(marks)
# grade = None
# if marks < 33:
#     grade = "F"
# elif marks >= 33 and marks < 45:
#     grade = "D"
# elif marks >= 45 and marks < 65:
#     grade = "C"
# elif marks >= 65 and marks < 85:
#     grade = "B"
# elif marks >= 85 and marks <= 100:
#     grade = "A"
# else:
#     print("Invalid Result!")


# if grade == "F":
#     print("Sorry, you are failed! Please try again next year.")
# elif grade == "A":
#     print(f"Excellent! you are passed with {grade} grade.")
# elif grade == "B":
#     print(f"Congratulations! you are passed with {grade} grade.")
# elif grade == "C":
#     print(f"You are passed with {grade} grade.")
# elif grade == "D":
#     print(f"You are passed with {grade} grade.")

# # practical-2
# day_number = int(input("Enter the day number: "))
# if day_number == 1:
#     print("Monday")
# elif day_number == 2:
#     print("Tuesday")
# elif day_number == 3:
#     print("Wednesday")
# elif day_number == 4:
#     print("Thursday")
# elif day_number == 5:
#     print("Friday")
# elif day_number == 6:
#     print("Saturday")
# elif day_number == 7:
#     print("Sunday")
# else:
#     print("Invalid Day Number!")

# # practical-3
# temp = int(input("Enter the current temperature"))
# if temp < 0:
#     print("It's freezing!")
# elif temp >= 0 and temp < 10:
#     print("It's cold!")
# elif temp >= 10 and temp < 20:
#     print("It's cool!")
# elif temp >= 20 and temp < 30:
#     print("It's warm!")
# else:
#     print("It's hot!")

# # practical-4
# age = int(input("Enter your age: "))
# if age <= 12:
#     print("You are a child!")
# elif age <= 18:
#     print("You are a teenager!")
# elif age <= 35:
#     print("You are an adult!")
# elif age <= 60:
#     print("You are middle aged!")
# else:
#     print("You are a senior citizen!")


# practical-5
# a = 444400
# b = 7000000
# c = 999900

# if a > b:
#     if a > c:
#         print("A is greatest number.")
#     elif c > b:
#         print("C is greatest number.")
# elif b < c:
#     if c > a:
#         print("C is greatest number.")
# else:
#     print("B is greatest number.")

# Ternary
age = 17
valid = "Yes" if age > 18 else "No"
nested_valid = "Yes" if age > 18 else "May be" if age > 20 else "No"
print(valid)
