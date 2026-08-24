# import json

# with open("student.json","r") as file:
#     student = json.load(file)
# print(student)
# print(student["name"])
# print(student["age"])
# print(student["city"])

import json

with open("student.json","r") as file:
    student = json.load(file)
print(student)
print(student["name"])
print(student["age"])
print(student["city"])