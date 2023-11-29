#SET EXERCISE-1:--------------------------------------------------------------------------------------------------------

#Add a list of elements to a set
#Given a Python list, Write a program to add all its elements into a given set.
#Given:

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
#Expected output:

##(Note: Set is unordered).

{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
##CODE:-
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)
#OUTPUT:-
{'Yellow', 'Red', 'Black', 'Green', 'Blue', 'Orange'}
#SET EXERCISE-2:--------------------------------------------------------------------------------------------------------
#Return a new set of identical items from two sets
#Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:

{40, 50, 30}
##CODE:--
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
#OUTPUT:-
{40, 50, 30}

#SET EXAMPLE-3:---------------------------------------------------------------------------------------------------------
#Get Only unique items from two sets
#Write a Python program to return a new set with unique items from both sets by removing duplicates.

#Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:

{70, 40, 10, 50, 20, 60, 30}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))
#OUTPUT:-
{70, 40, 10, 50, 20, 60, 30}
# SET EXAMPL-4:---------------------------------------------------------------------------------------------------------
#Update the first set with items that don’t exist in the second set
#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.


#Given:

set1 = {10, 20, 30}
set2 = {20, 40, 50}
#Expected output:
# set1 {10, 30}
#CODE:-
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)
#OUTPUT:-
{10, 30}

#SET EXAMPL-5:----------------------------------------------------------------------------------------------------------
#Remove items from the set at once
#Write a Python program to remove items 10, 20, 30 from the following set at once.

set1 = {10, 20, 30, 40, 50}
#Expected output:
{40, 50}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)
#OUTPUT:-
{40, 50}
#SET EXAMPLE-6:---------------------------------------------------------------------------------------------------------
#Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:

{20, 70, 10, 60}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))
#OUTPUT:-
{20, 70, 10, 60}
#SET EXAMPLE-7:---------------------------------------------------------------------------------------------------------
#Check if two sets have any elements in common. If yes, display the common elements
#Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
#Expected output:

#Two sets have items in common
{10}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))
#OUTPUT:-
#Two sets have items in common
{10}
#SET EXAMPLE-8:-----------------------------------------------------------------------------------------------------------
#Update set1 by adding items from set2, except common items
#Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:

{70, 10, 20, 60}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)
#OUTPUT:-
{70, 10, 20, 60}
#SET EXAMPLE-9:---------------------------------------------------------------------------------------------------------
#Remove items from set1 that are not common to both set1 and set2

#Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:

{40, 50, 30}
#CODE:-
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)
#OUTPUT:-
{40, 50, 30}











