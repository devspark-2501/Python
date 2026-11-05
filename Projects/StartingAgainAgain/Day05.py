# Sort() with list

# numbers = [5, 4, 6, 3, 6, 2]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# sort() function with itterable
# Tuples
# numbers = (5, 4, 6, 3, 6, 2)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# # Strings
# name = "Tanush"
# sorted_name = sorted(name)
# print(sorted_name)

# # Set
# values = {5, 4, 6, 3, 6, 2}
# sorted_values = sorted(values)
# print(sorted_values)

# .map()
# the python map() function is used to apply a specific function to each item in an iterable (like a list, tuple, or set)
# and return a new iterable with the results.
# It takes two arguments: the function to apply and the iterable to process.

number = [1, 2, 3, 4, 5]

def Square(n):
    return n * n

result = map(Square, number)
print(result)  