# Dictonary:

capitals = {
            'France': 'Paris',
            'India': 'Delhi',
            'China': 'Bejing',
            'Russia': 'Moscow',
            'South Africa': [
                'Pretoria',
                'Cape Town',
                'Bloemfontein'
            ],
            'Big City': [
                'Mumbai',
                'Delhi',
                'Indore',
                'Bhopal'
            ] 
        }

# print(capitals)
# for capital in capitals['South Africa']:
#     print(capital) #other option of getting the output

# for Citys in capital['Big City']:
#     print(Citys)

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get('USA'))
# print(capitals.get('India')) 
# print(capitals.get('Big City', end=' '))

capitals = {
    'France': 'Paris',
    'India': 'Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow',
    'South Africa': [
        'Pretoria',
        'Cape Town',
        'Bloemfontein'
    ],
    'Big City': [
        'Mumbai',
        'Delhi',
        'Indore',
        'Bhopal'
    ] 
}

# country = input("Enter a Country Name: ")

# if country in capitals:
#     print("This Country Exists ✅")
#     print("Capital(s):", capitals[country])
# else:
#     print("This Country does not exist ❌")

# capitals.update({'Germany': 'Berlin'})
# print(capitals)

capitals.pop('China')
capitals.pop('France')
capitals.pop('India')
capitals.pop('Russia')
print(capitals)