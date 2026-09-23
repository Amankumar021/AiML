# use of .ndim > to know the dimention of array

# 1 > 1d array
# 2 > 2d array
# 3 > 3d array

import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],[5,6,7]])
arr_3d = np.array([[[1,2,3],[5,6,7],[6,7,9]]])

print(arr_1d)
print(arr_1d.ndim)
print(arr_2d)
print(arr_2d.ndim)
print(arr_3d)
print(arr_3d.ndim)