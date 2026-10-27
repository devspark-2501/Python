# 2D List:
# fruits = ['apple', 'orange', 'banana', 'coconut']
# vegetables = ['celary', 'carrots', 'potatoes']
# meats = ['chicken', 'fish', 'turkey']

# groceries = [fruits, vegetables, meats]
# print(groceries[2][0])

Groceries = [
    ['apple', 'orange', 'banana', 'watermelon'],
    ['celary', 'carrots', 'potatoes'],
    ['chicken', 'fish', 'turkey']
]

for collection in Groceries:
    print(collection[0])
    # for food in collection:
        # print(food[0]

# Key Program:
Key_Pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ('*',0,'#')
)
for collection in Key_Pad:
    for num in collection:
        print(num, end=' ')
    # print(collection, end=' ')