def divide_numbers():
  """Takes two numbers as input and divides the first by the second."""
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  print("running loop")
divide_numbers()

print("--------------------")
elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
index= input("Enter an index between 0 and 4: ")
try:
    index = int(index)
    print(f"Element at index {index}: {elements[index]}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except IndexError:
    print("Index out of range. Please enter an index between 0 and 4.")
""" Exception           Name & When It Occurs
    ValueError	        Invalid value (e.g., int('a'))
    TypeError	        Wrong type (e.g., adding int and str)
    IndexError	        Index out of range in list
    KeyError	        Accessing missing dict key
    ZeroDivisionError	Division by zero
    FileNotFoundError	File or directory not found"""