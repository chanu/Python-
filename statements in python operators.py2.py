# Variables
a = 10
b = 5
c = 10
d = [1, 2, 3]
e = [1, 2, 3]

# Arithmetic operators
addition_result = a + b
subtraction_result = a - b
multiplication_result = a * b
division_result = a / b
modulo_result = a % b
power_result = a ** b

# Assignment operators
c += 5  # Equivalent to c = c + 5

# Comparison operators
equal_check = a == c
not_equal_check = a != b
greater_than_check = a > b
less_than_check = a < c
greater_than_equal_check = a >= c
less_than_equal_check = a <= b

# Logical operators
and_result = (a > b) and (a == c)
or_result = (a > b) or (a == c)
not_result = not (a == c)

# Identity operators
identity_result = d is e  # Checks if both variables refer to the same object

# Membership operators
membership_result = 2 in d  # Checks if the value 2 is present in the list d

# Bitwise operators
bitwise_and_result = a & b
bitwise_or_result = a | b
bitwise_xor_result = a ^ b
bitwise_not_result = ~a

# Print the results
print("Arithmetic Results:")
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)
print("Modulo:", modulo_result)
print("Power:", power_result)

print("\nAssignment Result:")
print("Updated c:", c)

print("\nComparison Results:")
print("Equal Check:", equal_check)
print("Not Equal Check:", not_equal_check)
print("Greater Than Check:", greater_than_check)
print("Less Than Check:", less_than_check)
print("Greater Than or Equal Check:", greater_than_equal_check)
print("Less Than or Equal Check:", less_than_equal_check)

print("\nLogical Results:")
print("Logical AND:", and_result)
print("Logical OR:", or_result)
print("Logical NOT:", not_result)

print("\nIdentity Result:")
print("Identity Check:", identity_result)

print("\nMembership Result:")
print("Membership Check:", membership_result)

print("\nBitwise Results:")
print("Bitwise AND:", bitwise_and_result)
print("Bitwise OR:", bitwise_or_result)
print("Bitwise XOR:", bitwise_xor_result)
print("Bitwise NOT:", bitwise_not_result)