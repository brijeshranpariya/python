print("Welcome to the Interactive Personal Data Collector!")
print()
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = int(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favorite number: "))

print("Thank you! Here is the information we collected: ")
print()
print("Name: ", name, f"(Type: {type(name)}, Memory Address: {id(name)})")
print("Age: ", age, f"(Type: {type(age)}, Memory Address: {id(age)})")
print("Height: ", height, f"(Type: {type(height)}, Memory Address: {id(height)})")
print(
    "Favorite Number: ", height, f"(Type: {type(height)}, Memory Address: {id(height)})"
)
print()
current_year = 2026
birth_year = current_year - age
print("Your birth year is approximately:", birth_year, "based on your age of ", age)
print()
print("Thank you for using the Personal Data Collector. Good bye!")
