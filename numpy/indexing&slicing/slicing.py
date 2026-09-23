"""
array[start:stop:step]

arr[start:end], start to end-1

negative step, -1 last element 
"""

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[1:5]) # 1 to 5-1
print(arr[:5]) # 0 to 5-1

print(arr[::-1]) # reverse print

print(arr[::2])  