#functions in python!

# def hello(name):
#     print("Hello "+ name)
#     print("Have a nice day!")

# hello("Tanush")

# def hello(first_name, last_name, age):
#     print("Hello, " +first_name + " " + last_name)
#     print("You are " + str(age) + " years old.")
#     print("Have a nice day!")

# hello("Tanush", "Mathur", 16)

# Details = {
#     "first_name": "Tanush",
#     "last_name": "Mathur",
#     "age": 16,
# }

# def greet_user(first_name, last_name, age):
#     print("Hello, " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old.")
#     print("Have a nice day!")

# greet_user(**Details)

# def multiply(num1, num2):
#     return num1 * num2

# multiply(5, 10)
# print("hello")

try:
    numerator=int(input("Enter a number: "))
    denominator=int(input("Enter a number: "))
    result = numerator / denominator
    print(result)
except Exception:
    print("Please enter a valid number!")
