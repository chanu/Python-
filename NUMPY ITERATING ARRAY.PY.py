###Iterating Arrays:
#Iterating means going through elements one by one.

#*As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

#*If we iterate on a 1-D array it will go through each element one by one.

#Example:------------------------------------------------------------------------------------------------
##Iterate on the element of the following 1-D array:

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
##Iterating 2-D Arrays:
#In a 2-D array it will go through all the rows.

#Example------------------------------------------------------------------------------------------------------
#Iterate on the elements of the following 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


#Example:----------------------------------------------------------------------------------------
#Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
#ADVERTISEMENT

#Iterating 3-D Arrays:
#In a 3-D array it will go through all the 2-D arrays.

#Example:---------------------------------------------------------------------------------
#Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
#To return the actual values, the scalars, we have to iterate the arrays in each dimension.

#Example:-------------------------------------------------------------------------------------------
#Iterate down to the scalars:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
