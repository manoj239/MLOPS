try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully!")
finally:
    print("Closing file (if it was opened).")
    if 'file' in locals():
        file.close()
print("-------------------------------")
# prompt: Create exception handling for any error that may arise:
# try:
#     file = open("data.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print("File read successfully!")
# finally:
#     print("Closing file (if it was opened).")
#     if 'file' in locals():
#         file.close()

try:
    file = open("data.txt", "r")
    content = file.read()
except Exception as e: # Catch any other potential exceptions
    print(f"An error occurred: {e}")
else:
    print("File read successfully!")
finally:
    print("Closing file (if it was opened).")
    if 'file' in locals() and not file.closed: # Check if 'file' exists and is not already closed
        file.close()
print("codes")
print("-----------------")
country_capitals = {
    "USA": "Washington D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

country_name = input("Enter a country name: ")

try:
  capital = country_capitals[country_name]
  print(f"The capital of {country_name} is {capital}.")
except KeyError:
  print(f"Sorry, the capital of {country_name} is not in our dictionary.")