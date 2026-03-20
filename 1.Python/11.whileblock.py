count = 5 # intialize
while count > 0:
  print(count)
  count = count -1
print("---------------------")
password = ""
count=3
while password != "python123" and count>0:
  count-=1
  password = input("Enter the password: ")
if password=="python123":
  print("Access granted!")
else :
  print("Maximun tries reaches") 