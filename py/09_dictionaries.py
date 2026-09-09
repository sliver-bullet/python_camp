
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}

# Accessing and modifying
print(student["name"])              # "Alice"
print(student.get("age"))           # 20
student["age"] = 21                 # Modify value
student["email"] = "alice@email.com"# Add new key-value


keys = student.keys()                   # Get all keys
values = student.values()               # Get all values
items = student.items()                 # Get all key-value pairs

print(keys)
print(values)
print(items)


# Iterating through dictionaries
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")


company = {
    "employee": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 25, "department": "HR"}    
    },
    "department": ["IT", "HR", "Finance"]
}

print(company["employee"].items())
print(company["department"])


student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# Add a new student 
# "student_003" with name "Mike", 
# age 18, major "Math", grades [82,79, 91]

# Update Joh's age to 20


# Loop through the dictionary and print each student's information 
# in this format:
# Student ID:
# Name:
# Major: