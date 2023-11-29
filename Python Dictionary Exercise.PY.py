#DICTIONARY EXERCISES-1:------------------------------------------------------------------------------------------------

#Convert two lists into a dictionary
#Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#Expected output:

#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#CODE:-
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
#OUTPUT:-
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#DICTIONARY EXERCISES-2:------------------------------------------------------------------------------------------------
# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#CODE:-
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)
#OUTPUT:-
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#DICTIONARY EXERCISES-3:------------------------------------------------------------------------------------------------
 #Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
#Expected output:
80
#CODE:-
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])
#OUTPUT:-
80

#DICTIONARY EXERCISES-4:------------------------------------------------------------------------------------------------
#Initialize dictionary with default values
#In Python, we can initialize the keys with the same values.

#Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
#CODE:-
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])
#OUTPUT:-
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
{'designation': 'Developer', 'salary': 8000}

#DICTIONARY EXERCISES-5:------------------------------------------------------------------------------------------------
#Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

#Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
#Expected output:

#{'name': 'Kelly', 'salary': 8000}
#CODE-1:-
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)
#OUTPUT:-
{'name': 'Kelly', 'salary': 8000}
#CODE-2:-
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)
#OUTPUT:-
{'name': 'Kelly', 'salary': 8000}

#DICTIONARY EXERCISES-6:------------------------------------------------------------------------------------------------
#Delete a list of keys from a dictionary
#Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
#Expected output:
{'city': 'New york', 'age': 25}
##CODE:--

#Solution 1: Using the pop() method and loop

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

#Solution 2: Dictionary Comprehension

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)
#OUTPUT:-
{'city': 'New york', 'age': 25}

#DICTIONARY EXERCISES-7:------------------------------------------------------------------------------------------------
#Check if a value exists in a dictionary

#We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

#Write a Python program to check if value 200 exists in the following dictionary.

#Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
#Expected output:200 present in a dict
#CODE:-
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():

    print('200 present in a dict')
#OUTPUT:-
#200 present in a dict

#DICTIONARY EXERCISES-8:------------------------------------------------------------------------------------------------
#Rename key of a dictionary
#Write a program to rename a key city to a location in the following dictionary.

#Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#CODE:-
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
#OUTPUT:-
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

#DICTIONARY EXERCISES-9:------------------------------------------------------------------------------------------------
#Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
#Expected output: Math
#CODE:-
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))
#OUTPUT:-
# Math

#DICTIONARY EXERCISES-10:------------------------------------------------------------------------------------------------
#Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.


#Given:

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
#Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
#CODE:-
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
#OUTPUT:-
{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}











