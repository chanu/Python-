#1.EXAMPLE-1:-------------------------------------------------------------------------
# Create a 4X2 integer array and Prints its attributes?


#1.The shape of an array?
#2.Array dimensions?
#3.The Length of each element of the array?
#ANSWER:-
import numpy

firstArray = numpy.empty([4,2], dtype = numpy.uint16) 
print("Printing Array")
print(firstArray)

print("Printing numpy array Attributes")
print("1> Array Shape is: ", firstArray.shape)
print("2>. Array dimensions are ", firstArray.ndim)
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)


#Output:-Printing Array
#[[64757 19267]
 #[45868 33230]
 #[16280   144]
 #[    0     0]]
#*Printing numpy array Attributes
#1> Array Shape is:  (4, 2)
#2>. Array dimensions are  2
#3>. Length of each element of array in bytes 

#2.EXAMPLE-2:------------------------------------------------------------------------------------------------------------------------
#Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10?
#ANSWER:-
import numpy

print("Creating 5X2 array using numpy.arange")
sampleArray = numpy.arange(100, 200, 10)
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)
#OUTPUT:-Creating 5X2 array using numpy.arange
#[[100 110]
# [120 130]
 #[140 150]
 #[160 170]
 #[180 190]]

#3.EXAMPLE-EXERCISE-3:---------------------------------------------------------------------------------------------------------------------
 #Following is the provided numPy array. Return array of items by taking the third column from all rows?

sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
#ANSWERE:-
import numpy

sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of items in the third column from all rows")
newArray = sampleArray[...,2]
print(newArray)

#OUTPUT:-
#Printing Input Array
#[[11 22 33]
 #[44 55 66]
 #[77 88 99]]

#Printing array of items in the third column from all rows [33 66 99]

 #EXERCISE-EXAMPLE-4:-------------------------------------------------------------------------------------------------------------------------------
 #Return array of odd rows and even columns from below numpy array
sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
#ANSWER:-
import numpy

sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of odd rows and even columns")
newArray = sampleArray[::2, 1::2]
print(newArray)

#OUTPUT:-
#Printing Input Array
 #[[ 3  6  9 12]
 #[15 18 21 24]
 #[27 30 33 36]
 #[39 42 45 48]
 #[51 54 57 60]]

 #Printing array of odd rows and even columns
 # [[ 6 12]
 #[30 36]
 #[54 60]].

  #EXERCISE-EXAMPLE-5:---------------------------------------------------------------------------------------------------------------------------------
  #Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
#arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
#rrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

#ANSWER:-
import numpy

arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

resultArray  = arrayOne + arrayTwo
print("addition of two arrays is \n")
print(resultArray)

for num in numpy.nditer(resultArray, op_flags = ['readwrite']):
   num[...] = num*num
print("\nResult array after calculating the square root of all elements\n")
print(resultArray)

#OUTPUT:-
#addition of two arrays is 

#[[20 39 33]
# [25 25 28]]

#Result array after calculating the square root of all elements

#[[ 400 1521 1089]
# [ 625  625  784]].

 #EXERCISE-EXAMPLE-6:-----------------------------------------------------------------------------------------------------
#Split the array into four equal-sized sub-arrays


#Expected Output:

#Creating 8X3 array using numpy.arange
#[[10 11 12]
 #[13 14 15]
 #[16 17 18]
 #[19 20 21]
 #[22 23 24]
 #[25 26 27]
 #[28 29 30]
 #[31 32 33]]

#Dividing 8X3 array into 4 sub array

#[array([[10, 11, 12],[13, 14, 15]]),
#array([[16, 17, 18],[19, 20, 21]]),
#array([[22, 23, 24],[25, 26, 27]]),
#array([[28, 29, 30],[31, 32, 33]])]

#answer in code:-
import numpy

print("Creating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4)
print(subArrays)
#o/p:-
#Creating 8X3 array using numpy.arange
#[[10 11 12]
 #[13 14 15]
 #[16 17 18]
 #[19 20 21]
 #[22 23 24]
 #[25 26 27]
 #[28 29 30]
 #[31 32 33]]

#Dividing 8X3 array into 4 sub array

#[array([[10, 11, 12],
 #      [13, 14, 15]]), array([[16, 17, 18],
 #      [19, 20, 21]]), array([[22, 23, 24],
 #      [25, 26, 27]]), array([[28, 29, 30],
 #     [31, 32, 33]])]
#EXERCISE-EXAMPLE:-7------------------------------------------------------------------------------------------------------------
#Sort following NumPy array
#Case 1: Sort array by the second row
#Case 2: Sort the array by the second column
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
#code :-
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)

sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
print("Sorting Original array by secoond row")
print(sortArrayByRow)

print("Sorting Original array by secoond column")
sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)

#o/p:-
#Printing Original array
#[[34 43 73]
 #[82 22 12]
 #[53 94 66]]
#Sorting Original array by secoond row
#[[73 43 34]
 #[12 22 82]
 #[66 94 53]]
#Sorting Original array by secoond column
#[[82 22 12]
 #[34 43 73]
 #[53 94 66]]

#EXERCISE-EXAMPLE-8:-----------------------------------------------------------------------------------------------
#Print max from axis 0 and min from axis 1 from the following 2-D array.

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

#code:-
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)

minOfAxisOne = numpy.amin(sampleArray, 1)
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = numpy.amax(sampleArray, 0)
print("Printing amax Of Axis 0")
print(maxOfAxisOne)
#o/p:-
#Printing Original array
#[[34 43 73]
 #[82 22 12]
 #[53 94 66]]
#Printing amin Of Axis 1
#[34 12 53]
#Printing amax Of Axis 0
#[82 94 73]

#EXERCISE-EXAMPLE-9:-----------------------------------------------------------------------------------------------------
#Delete the second column from a given array and insert the following new column in its place.

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = numpy.array([[10,10,10]])

#CODE:-
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray , 1, axis = 1)
print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1)
print (sampleArray)

#OUTPUT:-
#Printing Original array
#[[34 43 73]
 #[82 22 12]
 #[53 94 66]]
#Array after deleting column 2 on axis 1
#[[34 73]
 #[82 12]
 #[53 66]]
#Array after inserting column 2 on axis 1
#[[34 10 73]
 #[82 10 12]
 #[53 10 66]]
#EXERCISE-EXAMPLE-10:----------------------------------------------------------------------------------------
#Create two 2-D arrays and Plot them using matplotlib
#CODE:-
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray , 1, axis = 1)
print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1)
print (sampleArray)
#OUTPUT:-
#Printing Original array
#[[34 43 73]
 #[82 22 12]
 #[53 94 66]]
#Array after deleting column 2 on axis 1
#[[34 73]
 #[82 12]
 #[53 66]]
#Array after inserting column 2 on axis 1
#[[34 10 73]
 #[82 10 12]
 #[53 10 66]]














