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