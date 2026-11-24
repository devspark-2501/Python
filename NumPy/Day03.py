import numpy as np

arr = np.array([ #I
    [ #II
        [ #III
            [1,  2,  3], #IV
            [4,  5,  6]
        ],
        [
            [7,  8,  9],
            [10, 11, 12]
        ]
    ],
    [
        [
            [13, 14, 15],
            [16, 17, 18]
        ],
        [
            [19, 20, 21],
            [22, 23, 24]
        ]
    ]
])

# print(arr.ndim)
# print(arr.shape)

# print(arr[0, 2, 0, 1])


arr = np.array([
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        [
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    ],
    [
        [

            [17, 18, 19, 20],
            [21, 22, 23, 24],
        ],
        [
            [25, 26, 27, 28],
            [29, 30, 31, 32],
        ]
    ]
])

# num = np.array([0, 0, 0, 0])
# print(num[::-1])


#arithmetic operations
array = np.array([1, 2, 3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)


#   Function	                     Purpose

# np.add(a, b)	                    Addition
# np.subtract(a, b)	               Subtraction
# np.multiply(a, b)	              Multiplication
# np.divide(a, b)	                 Division
# np.power(a, b)	              Exponentiation
# np.sqrt(a)	                   Square root
# np.abs(a)	                     Absolute values
# np.round(a)	                   Round values
# np.floor(a)	                    Round down
# np.ceil(a)	                     Round up