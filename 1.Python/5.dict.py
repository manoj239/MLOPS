student = {
    "name": ["AK","BK"],
    "age": 7,
    "grade": 2,
    123: "roll no"
}
print(student)
print(type(student))
print(student["age"])
student['gender']= 'female'
print(student)
del student["gender"]
print(student)
student.pop("age")
print(student)
print(student)
print(student.keys())
print(student.values())
print(student.items())
print("--------------------------")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2) # Merge the two dictionaries using the update() method
print("Merged dictionary using update():", dict1)
merged_dict_unpacking = {**dict1, **dict2}
# Display the merged dictionary
print("Merged dictionary using unpacking operator:", merged_dict_unpacking)
print("----------------------------")
student = {
    "name": "Alice",
    "contact": {
        "email": "alice@example.com",
        "phone": "123-456-7890"
    },
    "courses": ["Math", "Science", "History"]
}

print(student)
print(student["contact"]["email"])