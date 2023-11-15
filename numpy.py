import numpy as np
arr_1=np.array([[1,2,3],[4,5,6]])
print(arr_1)

arr=([[12,23,45],[13,14,15]])
b=np.asarray(arr,dtype=float)
print(b)

c=np.asarray(arr,order='C')
for i in np.nditer(c):
    print(i)

arr2 = np.array([[[[[2,3,4,7,7],[2,5,6,7,9],[2,3,4,7,7],[2,5,6,7,9]]]]])
print(arr2)
print("the length of the array is:",arr2.size)
print("the shape  of the array is :", arr2.shape)
print("the datatype of the array is :", arr2.dtype)
print("the dimension of the arrays is:", arr2.ndim)

arr3 = np.array([[[[[[8,9],[5,7],[8,9]]]]]])
print(arr3.shape)