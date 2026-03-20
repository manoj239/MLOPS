for number in range(1,11):
  if number ==5:
    break
  print(number)
print("---------------")
count = 1
while count < 11:
    if count == 5:
        break
    print(count)
    count = count+ 1
print("-------------------------------")
for number in range(1, 6):
    if number == 3:
        pass  # You can add code here later
    print(number)
print("-------------------------------")
letter="bangalore"
for i in letter:
  if i == "a":
    continue
  else:
    print(i)