#LIST EXERCISE-1:-----------------------------------------------------------------------------------------------------
#Reverse a list in Python

list1 = [100, 200, 300, 400, 500]
#Expected output: [500, 400, 300, 200, 100]
#CODE:-
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#OUTPUT:-
[500,400,300,200,100]
#LIST EXERCISE-2:-----------------------------------------------------------------------------------------------------
#Concatenate two lists index-wise
#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#Expected output: ['My', 'name', 'is', 'Kelly']
#CODE:-
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
#OUTPUT:-
['My', 'name', 'is', 'Kelly']

#LIST EXERCISE-3:-----------------------------------------------------------------------------------------------------
#Turn every item of a list into its square
#Given a list of numbers. write a program to turn every item of a list into its square.

#Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
#Expected output:[1, 4, 9, 16, 25, 36, 49]

#Solution 1: Using loop and list method

#Create an empty result list
#Iterate a numbers list using a loop
#In each iteration, calculate the square of a current number and add it to the result list using the append() method.
numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
res = []
for i in numbers:
    # calculate square and add to the result list
    res.append(i * i)
print(res)
#OUTPUT:-
[1, 4, 9, 16, 25, 36, 49]
#Solution 2: Use list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)
#OUTPUT:-
[1, 4, 9, 16, 25, 36, 49]

#LIST EXERCISE-4:-----------------------------------------------------------------------------------------------------
#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
#Expected output:['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#CODE:-
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)
#OUTPUT:-
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

#LIST EXERCISE-5:-----------------------------------------------------------------------------------------------------
#Iterate both lists simultaneously
#Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

#Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
#CODE:-
#The zip() function can take two or more lists, aggregate them in a tuple, and returns it.
#Pass the first argument as a list1 and seconds argument as a list2[::-1] (reverse list using list slicing)
#Iterate the result using a for loop
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
#OUTPUT:-
# 10 400
# 20 300
# 30 200
# 40 100
#LIST EXERCISE-6:-----------------------------------------------------------------------------------------------------
#Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

#Expected output:

["Mike", "Emma", "Kelly", "Brad"]
#CODE:-
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)
#OUTPUT:-
['Mike', 'Emma', 'Kelly', 'Brad']

#LIST EXERCISE-7:-----------------------------------------------------------------------------------------------------
 #Add new item to list after a specified item
#Write a program to add item 7000 after 6000 in the following Python List

#Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#CODE:-
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# solution
list1[2][2].append(7000)
print(list1)
#OUTPUT:-
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

##LIST EXERCISE-8:-----------------------------------------------------------------------------------------------------
#Extend nested list by adding the sublist
#You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
#Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
#Expected Output:

['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

# solution
list1[2][1][2].extend(sub_list)
print(list1)
#OUTPUT:-
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


#LIST EXERCISE-9:----------------------------------------------------------------------------------------------------
#Replace list’s item with new value if found
#You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

#Given:

list1 = [5, 10, 15, 20, 25, 50, 20]
#Expected output: [5, 10, 15, 200, 25, 50, 20]
#CODE:-
list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)
#OUTPUT:-
[5, 10, 15, 200, 25, 50, 20]

#LIST EXERCISE-10:----------------------------------------------------------------------------------------------------
#Remove all occurrences of a specific item from a list.
#Given a Python list, write a program to remove all occurrences of item 20.
#CODE:-
#Solution 1: Use the list comprehension

list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)
        #OUTPUT:-  [5, 15, 25, 50]

#Solution 2: while loop (slow solution)

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)
                 #OUTPUT:-[5, 15, 25, 50]
