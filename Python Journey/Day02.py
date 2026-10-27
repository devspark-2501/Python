# a = 10
# b = '5'
# print(a + b)

# Type Casting:
# a = 10
# b = '10'
# print(a + int(b))

# b = 10
# print(type(b))

# a = '3'
# c = True
# d = 2.99
# print(type(a))
# print(type(c))
# print(type(d))

# p = 424

# age = '16'
# print(int(age))

# arr = ['tanush', 'joe', 'alex', 'sam']
# print(type(arr))

# inputList = ['3', '4', '5', '6', '7', '8']
# a = (list(inputList))
# print(int(a))

# age = 16
# age = float(age)
# print(age)

# age = '16'

# if int(age) >= 18:
#     print('adult')
# else:
#     print('kid')

# age = 17.8

# if float(age) >= 18:
#     print('Adult')
# else:
#     print('Kid')

# age = 17
# age = float(age)

# if age >= 18:
#     print(f'{age}')
# else: 
#     print(f'{age}')

# Input()
# name = input('What is your name? : ')
# print(f'Hello {name}!')

# age = int(input(f'How old are you {name}? '))

# if age >= 18:
#     print(f'You are {age} so You are an Adult')
# else:
#     print(f'Ooo You are just {age}, You are not an Adult')


# Exercise 1
# Find Area Of Rectangle
# length = int(input('Whats the Length of Rectangle: '))
# Width = int(input('Whats the Width of Rectangle: '))

# Sol = (length * Width)
# print(f'Answer Is {Sol}')

# Exercise 2
# Create an Shopping Cart Program
# item = input('What Would You Like To Buy: ')
# price = float(input(f'Price Of The {item} You Buy: '))
# Quantity = int(input(f'Whats The Quantity Of {item} You Bought: '))

# TotalBill = price * Quantity
# print(TotalBill)


# IF ELSE
marks = int(input('Marks You Obtained: '))

if marks == 100:
    print('Topper')
elif marks == 0:
    print('Failed')
elif marks >= 40:
    print('Pass')
else:
    print('Good')
