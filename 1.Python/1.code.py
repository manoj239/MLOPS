a=2
print(a)
print(type(a))
print("--------------------------")
def reverse_string(s):
  return s[::-1]

# Get input from the user
user_input = input("Enter a string to reverse: ")

# Reverse the string using the function
reversed_str = reverse_string(user_input)

# Print the reversed string
print(f"The reversed string is: {reversed_str}")
print("--------------------------")
a=5.14
b=5
print(a+b)
print(a*b)
print(a/b)
print(a**b)
print(complex(a))
integer_part = a // b
print(f"The integer part of {a}/{b} is: {integer_part}")
decimal_part = (a / b) - integer_part
print(f"The decimal part of {a}/{b} is: {decimal_part}")
division_result = a / b
# Use round() to get the nearest integer
nearest_integer = round(division_result)
print(a/b)
print(f"The nearest integer when {a}/{b} is: {nearest_integer}")
a = 10
b = 3
import math
division_result = a / b
higher_integer = math.ceil(division_result)
print(f"The higher integer (ceil) when {a}/{b} is: {higher_integer}")
print(10 == 9)
print(10 < 9)
print(10!=10)
multiline_string = """This is a string
that spans across
multiple lines."""
print(multiline_string)
print("--------------------------")
Division (/) in Python always returns a float
Even when both operands are integers