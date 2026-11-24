import numpy as np

arrays = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16],
])

# array[start:stop:step]




print(arrays[0:2])
# [[1 2 3 4], [5 6 7 8]]

print(arrays[:, 0:2])
# [[ 1  2], [ 5  6], [ 9 10], [13 14]]

print(arrays[0:2, 1:3])
# [[2 3], [6 7]]

print(arrays[::2, ::2])
# [[ 1  3], [ 9 11]]

print(arrays[1, 2])
# 7