x = 50
if x>=45:
  print("pass")
else:
  print("fail")
print("---------------------")
temp = input("Please enter the temperature: ")
temp = int(temp)
if temp > 35:
  print("Hot")
elif temp >= 20 & temp <=35:
  print("Warm")
elif temp >= 19 & temp <=10:
  print("Cool")
else:
  print("Cold")
print("-----------------------------")
print("nested conditional statements")
num = -25
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")
print("-----------------------------")
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income (in ₹): "))
credit_score = int(input("Enter your credit score: "))
if age >= 18:
    if income >= 25000:
        if credit_score >= 700:
            print("You are eligible for the loan!")
        else:
            print("Sorry, your credit score is too low.")
    else:
        print("Sorry, your income is too low.")
else:
    print("Sorry, you must be at least 18 years old to apply.")
print("--------------------------")

while True:
  print("\nSimple Calculator")
  print("1. Add")
  print("2. Subtract")
  print("3. Exit")
  choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
 num1 = int(input("enter first number: "))
 num2 = int(input("enter second number: "))
 result = num1 + num2
print(f"Result: {result}")
if choice == 2:
 num1 = int(input("enter first number: "))
 num2 = int(input("enter second number: "))
 result = num1 - num2
print(f"Result: {result}")
if choice == 3:
  print("Exit from calculator")
if choice != 1 and choice != 2 and choice != 3:
  print("Invalid choice! Please select 1 or 2 or 3")
print("--------------------------")
#prompt: Take three subject marks, compute average, use if-elif-else to assign grades and give feedback.

# Take three subject marks as input
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Compute the average
average_marks = (mark1 + mark2 + mark3) / 3

print(f"The average marks are: {average_marks:.2f}")

# Assign grades based on the average
if average_marks >= 90:
  grade = "A"
  feedback = "Excellent work! Keep it up."
elif average_marks >= 80:
  grade = "B"
  feedback = "Very good performance."
elif average_marks >= 70:
  grade = "C"
  feedback = "Good effort, can improve further."
elif average_marks >= 60:
  grade = "D"
  feedback = "You passed, but consider focusing on weak areas."
else:
  grade = "F"
  feedback = "You need to work harder. Please seek help."

print(f"Grade: {grade}")
print(f"Feedback: {feedback}")
