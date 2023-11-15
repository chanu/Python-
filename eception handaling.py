a=int(input())
b=int(input())

try:
    print(a/b)
except :
    print("division by zero")

#runt time error
# value error.....
try:
    number = int(input("enter the number:"))
    print(number*2)
except ValueError :
    print("enter the number not a string;")

# logic error example..........//
try:
   numbers = [5,6,7,7,88,8]
   result = numbers+sum
   print(result)
except :
    print("logic error;")
    numbers = [5,6,7,7,88,8]
    result = sum(numbers)
    print(result)

# runtime error........
# index not found.......
try:
    numbers = [1, 2, 3, 4, 5, 6]

    print(numbers[7])
except IndexError:
    print("please enter the validindex")