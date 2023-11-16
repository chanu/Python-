###COPY:
#Example-1---------------------------------------------------------------------------------

#Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)




###VIEW:
#Example-2------------------------------------------------------------------------------------
#Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


###Make Changes in the VIEW:
#Example-1------------------------------------------------------------------------------------------------------
#Make a view, change the view, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)




