# 1. Assign the integer 42 to a variable and print its type
a = 42
print(type(a))


# 2. Divide 7 by 3 and print the result and its data type
c = 7 / 3
print(c)
print(type(c))


# 3. Convert the float 8.75 to an integer and print it
a = 8.75
print(int(a))


# 4. Multiply an int and a float and print the result and type
a = 5
b = 2.5
c = a * b
print(c)
print(type(c))


# 5. Use type casting to add string '4' and integer 3
a = "4"
b = 3
print(int(a) + b)


# 6. Print 'World' from 'HelloWorld' using slicing
a = "HelloWorld"
print(a[5:])


# 7. Convert 'PYTHON' to lowercase
a = "PYTHON"
print(a.lower())


# 8. Check if 'data' exists in 'data science'
a = "data science"
print("data" in a)


# 9. Concatenate 'Data' and 'Type' with a space
a = "Data"
b = "Type"
print(a + " " + b)


# 10. Print the length of 'Boolean'
print(len("Boolean"))


# 11. Assign True to a variable and print its type
a = True
print(type(a))


# 12. Evaluate (10 > 2) and (3 == 4)
print((10 > 2) and (3 == 4))


# 13. Assign None and check if it equals 0
a = None
print(a == 0)


# 14. Print results of bool('') and bool('Python')
print(bool(""))
print(bool("Python"))


# 15. Compare float(3.0) == int(3)
print(float(3.0) == int(3))


# 16. Append 4 to the list [1, 2, 3]
a = [1, 2, 3]
a.append(4)
print(a)


# 17. Print first and last element of the list
a = [10, 20, 30, 40]
print(a[0])
print(a[-1])


# 18. Replace the second element of the list with 'z'
a = ['a', 'b', 'c']
a[1] = 'z'
print(a)


# 19. Create a tuple and attempt to change its second element
a = (1, 2, 3)
a[1] = 4


# 20. Add key 'c' with value 3 to a dictionary
a = {'a': 1, 'b': 2}
a['c'] = 3
print(a)
print("Answers for dict questions")
# 1. Function to calculate the square of a number
def square(num):
    return num ** 2

print("Square:", square(5))


# 2. Function that returns True if a number is even
def is_even(num):
    return num % 2 == 0

print("Is Even:", is_even(10))


# 3. Function that accepts a name and prints a welcome message
def greet(name):
    print("Welcome,", name)

greet("Manoj")


# 4. Function to return the maximum of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print("Maximum:", max_of_three(10, 25, 15))


# 5. Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reversed String:", reverse_string("Python"))


# 6. Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is Prime:", is_prime(7))


# 7. Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# 8. Function that accepts a list of numbers and returns their average
def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average([10, 20, 30, 40]))


# 9. Lambda function to add two numbers
add = lambda a, b: a + b

print("Addition:", add(5, 3))


# 10. Function that accepts any number of arguments and returns their sum
def sum_all(*args):
    return sum(args)

print("Sum:", sum_all(1, 2, 3, 4, 5))

# Write a for loop to print the squares of numbers from 1 to 10.
print("Squares from 1 to 10:")
for i in range(1, 11):
  print(i * i)

# Use a while loop to count backwards from 10 to 1.
print("\nCounting backwards from 10 to 1:")
count = 10
while count >= 1:
  print(count)
  count -= 1

# Print all vowels in a given string using a loop.
input_string = "This is a sample string."
vowels = "aeiouAEIOU"
print(f"\nVowels in '{input_string}':")
for char in input_string:
  if char in vowels:
    print(char)

# Create a multiplication table for 5 using nested loops.
print("\nMultiplication table for 5:")
for i in range(1, 11):
  print(f"5 * {i} = {5 * i}")

# Find the sum of digits for a number entered by the user.
num_str = input("\nEnter a number to find the sum of its digits: ")
sum_of_digits = 0
for digit in num_str:
  if digit.isdigit(): # Ensure the character is a digit
    sum_of_digits += int(digit)
print(f"The sum of the digits is: {sum_of_digits}")