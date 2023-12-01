# DATA STRUCTURE EXERCISES-1:--------------------------------------------------------------------------------------------
#Create a list by picking an odd-index items from the first list and even index items from the second
#Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
#Expected Output:

#Element at odd-index positions from list one
[6, 12, 18]
#Element at even-index positions from list two
[4, 12, 20, 28]

#Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
#CODE:-
#*To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the slicing, end, and specify the step.

#*For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.

#8for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
#*for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
#OUTPUT:-
#Element at odd-index positions from list one
[6, 12, 18]
#Element at even-index positions from list two
[4, 12, 20, 28]
#Printing Final third list
[6, 12, 18, 4, 12, 20, 28]

#EXERCISE-2:-----------------------------------------------------------------------------------------------------------
 #Remove and add item in a list
#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list1 = [54, 44, 27, 79, 91, 41]
#Expected Output:

#List After removing element at index 4  [34, 54, 67, 89, 43, 94]
#List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
#List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

#CODE:-
#*pop(index): Removes and returns the item at the given index from the list.
#*insert(index, item): Add the item at the specified position(index) in the list
#*append(item): Add item at the end of the list.
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
#OUTPUT:-
#Original list  [34, 54, 67, 89, 11, 43, 94]
#List After removing element at index 4  [34, 54, 67, 89, 43, 94]
#List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
#List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

#EXERCISE-3:----------------------------------------------------------------------------------------------------------
#Slice list into 3 equal chunks and reverse each chunk


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#Expected Outcome:

#Chunk  1 [11, 45, 8]
#After reversing it  [8, 45, 11]
#Chunk  2 [23, 14, 12]
#After reversing it  [12, 14, 23]
#Chunk  3 [78, 45, 89]
#After reversing it  [89, 45, 78]

#CODE:-
#*Get the length of a list using a len() function
#*Divide the length by 3 to get the chunk size
#*Run loop three times
#*In each iteration, get a chunk using a slice(start, end, step) function and reverse it using the reversed() function
#*In each iteration, start and end value will change

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)

    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
#OUTPUT:-
#Original list  [11, 45, 8, 23, 14, 12, 78, 45, 89]
#Chunk  0 [11, 45, 8]
#After reversing it  [8, 45, 11]
#Chunk  1 [23, 14, 12]
#After reversing it  [12, 14, 23]
#Chunk  2 [78, 45, 89]
#After reversing it  [89, 45, 78]

#EXERCISE-4:------------------------------------------------------------------------------------------------------------
#Count the occurrence of each element from a list
#Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#Expected Output:

#Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
#CODE:-
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)
#OUTPUT:-
#Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
#Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

#EXERCISE-5:------------------------------------------------------------------------------------------------------------
#Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
#Expected Output:

#Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
#CODE:-
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)
#OUTPUT:-
#First List  [2, 3, 4, 5, 6, 7, 8]
#Second List  [4, 9, 16, 25, 36, 49, 64]
{(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

#EXERCISE-6:------------------------------------------------------------------------------------------------------------
#Find the intersection (common) of two sets and remove those elements from the first set
#See: Python Set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

#Expected Output:
#Intersection is  {57, 83, 29}
#First Set after removing common element  {65, 42, 78, 23}
#CODE:-
#*Get the common items using the first_set.intersection(second_set)
#*Next, iterate common items using a for loop
#*In each iteration, use the remove() method of on first set and pass the current item to it.
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)
#OUTPUT:-
#First Set  {65, 42, 78, 83, 23, 57, 29}
#Second Set  {67, 73, 43, 48, 83, 57, 29}
#Intersection is  {57, 83, 29}
#First Set after removing common element  {65, 42, 78, 23}

#EXERCISE-7:------------------------------------------------------------------------------------------------------------
#Checks if one set is a subset or superset of another set. If found, delete all elements from that set


first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
#Expected Output:

#First set is subset of second set - True
#Second set is subset of First set -  False

#First set is Super set of second set -  False
#Second set is Super set of First set -  True

#First Set  set()
#Second Set  {67, 73, 43, 48, 83, 57, 29}
#CODE:-
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
#OUTPUT:-
#*First Set  {57, 83, 29}
#*Second Set  {67, 73, 43, 48, 83, 57, 29}
#*First set is subset of second set - True
#*Second set is subset of First set -  False
#*First set is Super set of second set -  False
#*Second set is Super set of First set -  True
#*First Set  set()
#*Second Set  {67, 73, 43, 48, 83, 57, 29}

#EXERCISE-8:------------------------------------------------------------------------------------------------------------
#Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#Expected Outcome:

#After removing unwanted elements from list [47, 69, 76, 97]
#CODE:-
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)
#OUTPUT:-
List: [47, 64, 69, 37, 76, 83, 95, 97]
Dictionary: {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#after removing unwanted elements from list: [47, 69, 76, 97]

#EXERCISES-9:-----------------------------------------------------------------------------------------------------------
#Get all values from the dictionary and add them to a list but don’t add duplicates


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#Expected Outcome:

[47, 52, 44, 53, 54]
#CODE:-
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)
#OUTPUT:-
#Dictionary's values -  dict_values([47, 52, 47, 44, 52, 53, 54, 44, 54])
#unique list [47, 52, 44, 53, 54]

#EXERCISE-10:-----------------------------------------------------------------------------------------------------------
#Remove duplicates from a list and create a tuple and find the minimum and maximum number


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#Expected Outcome:

#unique items [87, 45, 41, 65, 99]
#tuple (87, 45, 41, 65, 99)
#min: 41
#max: 99

#CODE:-
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sample_list)

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))







