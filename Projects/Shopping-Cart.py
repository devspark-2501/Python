# Project Idea: Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input('Enter Food To Buy (Q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter Price Of {food}: $'))
        foods.append(food)
        prices.append(price)

print()
print('--- YOUR CART ---')

for food in foods:
    print(food, end=' ')

print()

for price in prices:
    total += price

print(f'Your Total: ${total}')


# food = []
# price = []
# total = 0

# while True:
#     food = input('Enter food Name: ')
#     if food.lower == 'q':
#         break
#     else:
#         price = float(input(f'Enter Price of {food} :'))
#         foods.append(food)
#         prices.append(price)

# print()
# print('---Your Cart---')

# for food in foods:
#     print(food, end=' ')

# print()

# for price in prices:
#     total += prices

# print(f'Your Total: {total}')
