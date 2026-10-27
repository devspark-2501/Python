# Project Idea: Weight Converter

weight = float(input('Enter Your Weight: '))
units = input('Select Unit (KG or lb): ').lower()

if units == "kg":
    converted = weight * 2.205
    print(f'Your Weight In Pounds Is: {converted}')
elif units == "lb":
    converted = weight / 2.205
    print(f'Your Weight In Kilograms Is: {converted}')
else:
    print(f'{units} Was Not Valid')
