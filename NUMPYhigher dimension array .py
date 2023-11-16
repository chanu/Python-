#Higher Dimensional Arrays
#An array can have any number of dimensions.

# eWhen the array is created, you can define the number of dimensions by using the ndmin argument.

#Exampl
#Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

import numpy as np

# 4D array (2x3x4x5)
four_dimensional_array = np.random.rand(2, 3, 4, 5)

# 5D array (3x2x4x3x2)
five_dimensional_array = np.ones((3, 2, 4, 3, 2))

# 6D array (2x2x2x2x2x2)
six_dimensional_array = np.zeros((2, 2, 2, 2, 2, 2))

# You can continue this pattern for even higher dimensions.


