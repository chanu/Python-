#TUPLE-EXERCISE-1:------------------------------------------------------------------------------------------------------
#Reverse the tuple
#Given:


tuple1 = (10, 20, 30, 40, 50)
#CODE:-
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

#OUTPUT:-(50,40,30,20,10)
#TUPLE-EXERCISE-2:------------------------------------------------------------------------------------------------------
#Access value 20 from the tuple
#The given tuple is a nested tuple. write a Python program to print the value 20.

#Given:

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
#CODE:-
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20

print(tuple1[1][1])
#OUTPUT:-
20
#TUPLE-EXERCISE-3:------------------------------------------------------------------------------------------------------
#Create a tuple with single item 50
#CODE:-
tuple1= (50, )
print(tuple1)
#OUTPUT:-
(50,)
#TUPLE-EXERCISE-4:-----------------------------------------------------------------------------------------------------
#Unpack the tuple into 4 variables
##Write a program to unpack the following tuple into four variables and display each variable.

#Given:

tuple1 = (10, 20, 30, 40)
#Expected output:

tuple1 = (10, 20, 30, 40)
#Your code
#print(a) # should print 10
#print(b) # should print 20
#print(c) # should print 30
#print(d) # should print 40
##CODE:---
tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
#OUTPUT:-
10
20
30
40
#TUPLE-EXERCISE-5:-----------------------------------------------------------------------------------------------------
#Swap two tuples in Python
#Given:

tuple1 = (11, 22)
tuple2 = (99, 88)
#Expected output:

tuple1: (99, 88)
tuple2: (11, 22)
#CODE:--
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)
#OUTPUT:-
(11, 22)
(99, 88)
#TUPLE-EXERCISE-6:-----------------------------------------------------------------------------------------------------
#Copy specific elements from one tuple to a new tuple
#Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

#Given:

tuple1 = (11, 22, 33, 44, 55, 66)
#Expected output:

tuple2: (44, 55)
#CODE:-
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)
#OUTPUT:-
(44, 55)
#TUPLE-EXERCISE-7:-----------------------------------------------------------------------------------------------------
#Modify the tuple
#Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

#Given:
tuple1 = (11, [22, 33], 44, 55)
#Expected output:

tuple1: (11, [222, 33], 44, 55)
#CODE:-
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
#OUTPUT:-
(11, [222, 33], 44, 55)
#TUPLE-EXERCISE-8:-----------------------------------------------------------------------------------------------------
#Sort a tuple of tuples by 2nd item
#Given:

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))
#CODE:-
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
#OUTPUT:-(('c', 11), ('a', 23), ('d', 29), ('b', 37))
#TUPLE-EXERCISE-9:-----------------------------------------------------------------------------------------------------
#Counts the number of occurrences of item 50 from a tuple
#Given:
tuple1 = (50, 10, 60, 70, 50)
#Expected output:

2
#CODE:-
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
#OUTPUT:-
2
#TUPLE-EXERCISE-10:-----------------------------------------------------------------------------------------------------
#Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
#Expected output:

True

#CODE:-
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))
#OUTPUT:-True






















