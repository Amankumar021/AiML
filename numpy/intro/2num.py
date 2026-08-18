#pip3 install numpy in terminal

import numpy as np 


# handle large amount if data using array 
# feature
# => speed 
# => easy math operation
# => 



temp = np.array([32,45,12,22,35,61,23.6])

average = np.mean(temp)

# print(average)

# declare array with default size
# np.zeros(shape)  #=> np.zeros(3) for id

#example
# zeroes_array = np.zeros(3)
# print(zeroes_array)

#to intialise array with one(1);

one_array = np.ones((2,3))
print(one_array)



# to intilise with any value

filled_array = np.full((2,5),7)
print(filled_array)

