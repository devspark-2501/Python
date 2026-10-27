# Project Idea: Temperature-Conversion

unit = input('Select (C / F): ')
temp = float(input('Enter The Temperature: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32)
    print(f'The Temperature Is: {temp}')
elif unit == 'F':
    temp = round(temp - 32) * 5 / 9
    print(f'The Temperature Is: {temp}')
else:
    print(f'{unit} Is Invalid Unit')
