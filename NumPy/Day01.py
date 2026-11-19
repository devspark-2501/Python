import numpy as np

# print(np.__version__)
# my_list = [1, 2, 3, 4, 5]
# my_list = my_list * 2
# print(my_list)

# array = np.array([1, 2, 3, 4, 5])
# array = array * 2
# print(array)

# Multidimensional Arrays
# 0D array
arrayZeroD = np.array(42)
print(arrayZeroD.ndim)

# 1D array
arrayOneD = np.array([1, 2, 3, 4, 5])
print(arrayOneD.ndim)

# 2D array
arrayTwoD = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arrayTwoD.ndim)

# 3D array
arrayThreeD = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print(arrayThreeD.ndim)