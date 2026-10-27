# Conditionals Expression:

# num = 8
# print('Positive' if num > 0 else 'Negative')

# num = 4
# print('Even' if num % 2 == 0 else 'Odd')

# String Methods:
# name = input('Enter Your Name: ')
# lenght = len(name)
# print(lenght)

# name = input('Enter Your Name: ')
# find = name.find('T')
# print(find)

# name = input('Enter Your Name: ')
# rfind = name.rfind('t')
# print(rfind)

# name = input('Enter Your Name: ')
# capital = name.capitalize()
# print(capital)

# name = input('Enter Your Name: ')
# upper = name.upper()
# print(upper)

# name = input('Enter Your Name: ')
# lower = name.lower()
# print(lower)

# name = input('Enter Your Name: ')
# isdigit = name.isdigit()
# print(isdigit)

# Name = input('Enter Your Name: ')

# if len(Name) > 12 or ' ' in Name or not Name.isalpha():
#     print('Invalid Input')
# else:
#     print(Name)

# While Loops

# Name = input('Enter Your Name: ')
# while Name == '':
#     print('You Did Not Enter Your Name')
#     Name = input('Enter Your Name: ')
# print(f'Hello {Name}')

# age = int(input('Enter Your Age: '))
# while age == '':
#     print('Please Enter Your Name: ')
#     age = int(input('Enter Your Age'))

# if age >= 18:
#     print('You Are Adult!')
# else:
#     print('Sorry You Are A Kid!')

food = input('Enter a food you like (t to quit): ')
while not food == 't':
    print(f'You like {food}')
    food = input('Enter another food you like: ')
print('bye')