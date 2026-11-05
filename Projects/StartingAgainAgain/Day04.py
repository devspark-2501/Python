# The super() function in Python is used to call methods from a parent class inside a child class.

# It is especially useful in inheritance when you want a child class
#  to reuse the parent's code instead of writing everything again.

# class Student:
#     def __init__(self, name):
#         self.name = name


# def introduce(student):
#     print(f"My name is {student.name}")


# student1 = Student("Tanush")

# introduce(student1)

# # Without walrus operator
# number = len("Python")

# if number > 5:
#     print(number)


# # With walrus operator
# if (number := len("Python")) > 5:
#     print(number)

# A lambda function in Python is a small anonymous function created using the lambda keyword. 
# It can take multiple arguments but contains only one expression, 
# whose result is automatically returned. It is useful for writing short, 
# simple functions in a single line without using def.