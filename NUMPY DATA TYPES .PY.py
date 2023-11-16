#strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
#integer - used to represent integer numbers. e.g. -1, -2, -3
#float - used to represent real numbers. e.g. 1.2, 42.42
#boolean - used to represent True or False.
#complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

#EXAMPLE-1: --------------------------------------------------------------------------------------

##Checking the Data Type of an Array
#The NumPy array object has a property called dtype that returns the data type of the array:

#ExampleGet your own Python Server
#Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

#EXAMPLE-2:-------------------------------------------------------------------------------------------

#Get the data type of an array containing strings:

import numpy as np

arr = np.array(['chanu', 'sai', 'nani'])

print(arr.dtype)

##Creating Arrays With a Defined Data Type:
#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

#Example-3----------------------------------------------------------------------------------------
#Create an array with data type string:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#example-4------------------------------------------------------------------------------------------------------
#Create an array with data type 4 bytes integer:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


##Converting Data Type on Existing Arrays:
#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

#The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

#Example-1-------------------------------------------------------------------------------------------
#Change data type from float to integer by using 'i' as parameter value:

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
#Example-2----------------------------------------------------------------------------------------
#Change data type from float to integer by using int as parameter value:

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
#Example-3-------------------------------------------------------------------------------------------
#Change data type from integer to boolean:

import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)







