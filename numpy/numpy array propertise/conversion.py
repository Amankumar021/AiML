# .astype(dataType) > this is used to convert datatype of a array

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

# after conversion
float_arr = arr.astype(float);
print(float_arr)
print(float_arr.dtype) 