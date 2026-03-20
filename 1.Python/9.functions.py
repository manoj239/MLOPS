#what is a function
#A function is a block of reusable code that performs a specific task.
#Functions help you write clean, modular, and DRY (Don't Repeat Yourself) code.
def greet(student_name):
    print("Welcome to the class, " + student_name)
greet("Manoj")
print("------------------------------")
def sum3(a=0,b=0,c=0):
  sum3 = a+b+c
  return(sum3)
a= sum3(3,24,3)
print(a)
print("------------------------------")
def square(num=0):
    return num ** 2
result = square(5)
print("Square:", result)
print("------------------------------")
def student(name, grade):
    print(f"{name} scored {grade}")
student(grade="A", name="Ravi")
print("------------------------------")
def greet(name, message):
  print(f"Hello {name}, {message}")
greet(message = "hope you're having a great day!",name = "Alice")
print("------------------------------")
def sum_all(*args):
    return sum(args)
result = sum_all(1, 2, 5)
print(result)
print("------------------------------")
# prompt: # you have a dictionary that goes as an input and you need to print all the key value pairs

def print_dict_items(input_dict):
  """
  Prints all key-value pairs from a dictionary.

  Args:
    input_dict: The dictionary to print.
  """
  for key, value in input_dict.items():
    print(f"{key}: {value}")

# Example usage:
my_dictionary = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
print_dict_items(my_dictionary)
print("----------------------------------")
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
print_details(name="Ricky", age=7)
print("----------------------------------")
# local scope
def demo():
  x = 5
  print(x)
demo()
#print(x) will get error as x is declared inside function
print("----------------------------------")
# global scope
x = 10
def show():
  print(x)
show()
x
print("----------------------------------")