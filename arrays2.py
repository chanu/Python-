import numpy as np
import array
class myArray(array.array):
    arraymember1 = np.array((1,3,4,5))
    arraymember2 = np.array([2,4,5,3])
    def array_addition(self):
        resultArray = self.arraymember1+self.arraymember2
        print("This array_addition function returns the result Array")
        return resultArray

arrayObj = myArray('u')
arrayObj.arraymember1 = np.array([[1,2,3,4],[34,54,3,4]])
arrayObj.arraymember2 = np.array([[2,34,0,23],[32,23,34,23]])
resultArray = arrayObj.array_addition()
print("Arrays after addition : /n",resultArray)
