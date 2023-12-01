#EXERCISE-1(A):------------------------------------------------------------------------------------------------------------
#Create a string made of the first, middle and last character
#Write a program to create a new string made of an input string’s first, middle, and last character.

str1 = "James"
#Expected Output:
#Jms
#CODE:-
#Use string indexing to get the character present at the given index.
#Use str1[0] to get the first character of a string and add it to the result variable
#Next, get the middle character’s index by dividing string length by 2. x = len(str1) /2. Use str1[x] to get the middle character and add it to the result variable
#Use str1[len(str1)-1] to get the last character of a string and add it to the result variable
#print result variable to display new string

#str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)
#OUTPUT:-
#Original String is James
#New String: Jms

#EXERCISE-1(B):------------------------------------------------------------------------------------------------------------
#Create a string made of the middle three characters
#Write a program to create a new string made of the middle three characters of an input string.
#Case 1

str1 = "JhonDipPeta"
#Output

#Dip
#Case 2

str2 = "JaSonAy"
#Output

#Son
#CODE:-
#Get the middle character’s index using x = len(str1) /2.
#Use string slicing to get the middle three characters starting from the middle index to the next two character str1[middle_index-1:middle_index+2]
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")
#OUTPUT:-
#Original String is JhonDipPeta
#Middle three chars are: Dip
#Original String is JaSonAy
#Middle three chars are: Son


#EXERCISE-2:------------------------------------------------------------------------------------------------------------
#Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"
#Expected Output:
#AuKellylt
#CODE:-
#First, get the middle index number of s1 by dividing s1’s length by 2
#Use string slicing to get the character from s1 starting from 0 to the middle index number and store it in x
#concatenate x and s2. x = x + s2
#concatenate x and remeaning character from s1
#print x
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # middle index number of s1
    mi = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")
#OUTPUT:-
#Original Strings are Ault Kelly
#After appending new string in middle: AuKellylt

#EXERCISES-3:----------------------------------------------------------------------------------------------------------
#Create a new string made of the first, middle, and last characters of each input string

#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.


#s1 = "America"
#s2 = "Japan"

#CODE:-
#Get the first character from both strings, concatenate them, and store them in variable x
#Get the middle character from both strings, concatenate them, and store them in variable y
#Get the last character from both strings, concatenate them, and store them in variable x
#In the end, join x, y, and z and save it in the result variable
#print the result
def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)
#OUTPUT:-
#Mix String is  AJrpan

#EXERCISES-4:-----------------------------------------------------------------------------------------------------------
#Arrange string characters such that lowercase letters should come first
#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.



#str1 = PyNaTive

#Expected Output:
#yaivePNT
#CODE:-
#*Create two lists lower and upper
#*Iterate a string using a for loop
#*In each loop iteration, check if the current character is the lower or upper case using the islower() string function.
#*If a character is the lower case, add it to the lower list, else add it to the upper list
#*to join the lower and upper list using a join() function.
#*convert list to string
#*print the final string
str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)
#OUTPUT:-
#Original String: PYnAtivE
#Result: ntivPYAE

#EXERCISES-5:-----------------------------------------------------------------------------------------------------------
#Count all letters, digits, and special symbols from a given string


str1 = "P@#yn26at^&i5ve"
#Expected Outcome:

#Total counts of chars, digits, and symbols

Chars = 8
Digits = 3
Symbol = 4

#CODE:-
#Iterate each character from a string using a for loop
#In each loop iteration, check if the current character is the alphabet using an isalpha() function. If yes, increase the character counter. Check if it is a digit using the isdigit() function and increase the digit counter; otherwise, increase the symbol counter.
#Print the value of each counter
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)
#OUTPUT:-
#total counts of chars, Digits, and symbols

#Chars = 8 Digits = 2 Symbol = 3


#STRING EXERCISE-6:-----------------------------------------------------------------------------------------------------
#Create a mixed String using the following rules
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.



s1 = "Abc"
s2 = "Xyz"
#Expected Output:

#AzbycX

#CODE:-
s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

#OUTPUT:- AzbycX

#STRING EXERCISE-7:-----------------------------------------------------------------------------------------------------
#String characters balance Test
#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
#Case 1:

s1 = "Yn"
s2 = "PYnative"
#Expected Output:

True
#Case 2:

s1 = "Ynf"
s2 = "PYnative"

#Expected Output:

False

#code:-
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

#output:-
#s1 and s2 are balanced: True
#s1 and s2 are balanced: False

#STRING EXERCISE-8:-----------------------------------------------------------------------------------------------------
#Find all occurrences of a substring in a given string by ignoring the case
#Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
#Expected Outcome:
#The USA count is: 2

#CODE:-
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

#OUTPUT:-
#The USA count is: 2

#STRING EXERCISE-9:-----------------------------------------------------------------------------------------------------
#Calculate the sum and average of the digits present in a string
#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.



str1 = "PYnative29@#8496"
#Expected Outcome:

#Sum is: 38 Average is  6.333333333333333

#CODE:-
##Solution 1: Use string functions

#*Iterate each character from a string s1 using a loop
#*In the body of a loop, check if the current character is digit using the isdigit() function
#*If it is a digit, then add it to the sum variable
#*In the end, calculate the average by dividing the total by the count of digits

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)

#OUTPUT:-
#Sum is: 38 Average is  6.333333333333333

###SOLUTION-2:-Use regular expression

import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)
#OUTPUT:-
Digits: [2, 9, 8, 4, 9, 6]
#Sum is: 38 Average is  6.333333333333333

#STRIG EXERCISE-10:------------------------------------------------------------------------------------------------------
#Write a program to count occurrences of all characters within a string


#str1 = "Apple"
#Expected Outcome:

#{'A': 1, 'p': 2, 'l': 1, 'e': 1}

#CODE:-
#*create an empty dictionary to store the result. character is the key, and the count is the value
#*Iterate each character from a string s1 using a loop
#*In the body of a loop, use the count() function to find how many times a current character appeared in a string
#*Add key-value pair in a dictionary

str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

#OUTPUT:-
Result: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

#STRING EXERCISE-11:----------------------------------------------------------------------------------------------------
#Reverse a given string


str1 = "PYnative"
#Expected Output:

#evitanYP
#CODE:-1:- Negative String slicing

str1 = "PYnative"
print("Original String is:", str1)

str1 = str1[::-1]
print("Reversed String is:", str1)
#OUTPUT:-
#Original String is: PYnative
#Reversed String is: evitanYP

#CODE:-2:-Using the reversed() function

str1 = "PYnative"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)
#OUTPUT:-
#Original String is: PYnative
#Reversed String is: evitanYP


#STRING EXERCISE-12:----------------------------------------------------------------------------------------------------
#Find the last position of a given substring
#Write a program to find the last position of a substring “Emma” in a given string.

#Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
#Expected Output:

#Last occurrence of Emma starts at index 43

#CODE:-
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)

#OUTPUT;-
#Original String is: Emma is a data scientist who knows Python. Emma works at google.
#Last occurrence of Emma starts at index: 43

#STRING EXERCISE-13:----------------------------------------------------------------------------------------------------
#Split a string on hyphens
#Write a program to split a given string on hyphens and display each substring.

#Given:


#str1 = Emma-is-a-data-scientist
#Expected Output:

#*Displaying each substring

#*Emma
#*is
#*a
#*data
#*scientist

#CODE:-
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)

#OUTPUT:-
#Original String is: Emma-is-a-data-scientist
#Displaying each substring
#Emma
#is
#a
#data
#scientist

#STRING EXERCISE-14:----------------------------------------------------------------------------------------------------
#Remove empty strings from a list of strings
#Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#Expected Output:

#Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

#After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

#CODE:- Solution 1: Using the loop and if condition

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)
#OUTPUT:-
['Emma', 'Jon', 'Kelly', 'Eric']
#CODE:-Using the built-in function filter()

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)
#OUTPUT:-
#After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

#STRING EXERCISE-15:----------------------------------------------------------------------------------------------------
#Remove special symbols / punctuation from a string
#Given:

str1 = "/*Jon is @developer & musician"
#Expected Output:

"Jon is developer musician"
#CODE:-Solution 1: Use string functions translate() and maketrans().

#The string.punctuation constant contain all special symbols.

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)
#OUTPUT:-
# Original string is  /*Jon is @developer & musician
#New string is  Jon is developer  musician


#CODE:-Solution 2: Using regex replace pattern in a string

import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)
#OUTPUT:-
# Original string is  /*Jon is @developer & musician
#New string is  Jon is developer  musician

#STRING EXERCISE-16:----------------------------------------------------------------------------------------------------
#Removal all characters from a string except integers
#Given:

str1 = 'I am 25 years and 10 months old'

#Expected Output:

2510
#CODE:-
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)

#OUTPUT:-
#Original string is I am 25 years and 10 months old
2510


#STRING EXERCISE-17:----------------------------------------------------------------------------------------------------
#Find words with both alphabets and numbers
#Write a program to find words with both alphabets and numbers from an input string.

#Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
#Expected Output:

#Emma25
#scientist50

#CODE:-
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
#OUTPUT:-
#The original string is : Emma25 is Data scientist50 and AI Expert
#Displaying words with alphabets and numbers
#Emma25
#scientist50

#STRING EXERCISE-18:----------------------------------------------------------------------------------------------------
#Replace each special symbol with # in the following string
#Given:

str1 = '/*Jon is @developer & musician!!'
#Expected Output:

##Jon is #developer # musician##

#CODE:-
#Use the string.punctuation constant to get the list of all punctuations
#Iterate each symbol from a punctuations
#Use string function replace() to replace the current special symbol in a string with #
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
#OUTPUT:-
#The original string is :  /*Jon is @developer & musician!!
#The strings after replacement :  ##Jon is #developer # musician##



































