###Searching Arrays:
#*You can search an array for a certain value, and return the indexes that get a match.
#*To search an array, use the where() method.

#EXAMPLE:-----------------------------------------------------------------------------
#Find the indexes where the value is 4:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
#O/P:-(array([3, 5, 6]),).

###The example above will return a tuple: (array([3, 5, 6],)
#Which means that the value 4 is present at index 3, 5, and 6.###

#EXAMPLE:-------------------------------------------------------------------------------

#Find the indexes where the values are even:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
#O/P:-(array([1, 3, 5, 7]),).
##EXAMPLE:--------------------------------------------------------------------------------
#Find the indexes where the values are odd:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)
#O/P:-(array([0, 2, 4, 6]),).

##-Search Sorted:-
#There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#The searchsorted() method is assumed to be used on sorted arrays.
#EXAMPLE:--------------------------------------------------------------------------------------

##Find the indexes where the value 7 should be inserted:

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
#O/P:- 1.



