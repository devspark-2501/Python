# Project Idea: Complex Shopping Cart Program

foods = []
prices = []
quantities = []
total = 0

while True:
    food = input('Enter Food You Buy (Q to quit): ')
    
    if food.lower() == 'q':
        break
    
    quantity = int(input('Enter Items Bought: '))
    price = float(input(f'Enter Price Of Each {food}: '))

    foods.append(food)
    quantities.append(quantity)
    prices.append(price)

print()
print('--- FOOD CART ---')

for i in range(len(foods)):
    item_total = prices[i] * quantities[i]
    total += item_total
    print(f'{food[i]} x {quantities[i]} = ${item_total}')

print()
print(f'Your Total Bill: ${total:.2f}')
