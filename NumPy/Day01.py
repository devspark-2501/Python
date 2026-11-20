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
# arrayZeroD = np.array(42)
# print(arrayZeroD.ndim)

# # 1D array
# arrayOneD = np.array([1, 2, 3, 4, 5])
# print(arrayOneD.ndim)

# # 2D array
# arrayTwoD = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arrayTwoD.ndim)

# # 3D array
# arrayThreeD = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])
# print(arrayThreeD.ndim)

# Indexing in Multidimensional Arrays
# indexing in 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Output: 1
print(arr[4])  # Output: 5
print(arr[-1])  # Output: 5

# indexing in 2D array
arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(arr2D[0, 0])  # Output: 1
print(arr2D[1, 2])  # Output: 6
print(arr2D[0, 2])  # Output: 3

#indexing in 3D array
arr3D = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print(arr3D[0, 0, 0])  # Output: 1
print(arr3D[1, 1, 2])  # Output: 12
print(arr3D[0, 1, 2])  # Output: 6
