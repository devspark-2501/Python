print( )
menu = {'pizza' : 3.00,
        'nachos' : 4.00,
        'burger' : 6.00,
        'fries' : 9.00,
        'soda' : 8.00,
        'chips' : 4.09
        }

cart = []
total = 0

print('-------------------MENU--------------------')
for key, value in menu.items():
    print(f'{key}: {value}')
print('-------------------------------------------')

while True:
    food = input('Select an item: ').lower
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food, end=' ')

print( )
print(f'Total is: {total:.2f}')
print( )