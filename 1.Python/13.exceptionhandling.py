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