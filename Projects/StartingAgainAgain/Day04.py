# The super() function in Python is used to call methods from a parent class inside a child class.

# It is especially useful in inheritance when you want a child class
#  to reuse the parent's code instead of writing everything again.

class Student:
    def __init__(self, name):
        self.name = name


def introduce(student):
    print(f"My name is {student.name}")


student1 = Student("Tanush")

introduce(student1)