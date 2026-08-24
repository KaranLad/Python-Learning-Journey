# ====== json.dumps() ====== 
# import json

# student = {"name": "Karan Lad","age" : 22,"city": "surat"}

# with open("Student.json","w") as file:
#     student=json.dump(student)
# # with open("Student.json","r") as file:
# #     student = json.load(file)
# print(student)

# ====== json.loads() ======

# import json
# student = '{"name": "Karan", "age": 22}'

# # data = json.dumps(student)
# data = json.loads(student)
# print(data)
# print(type(data))

# ========== PROBLEM 1 ==========


# import json

# response = '''
# {
#     "name": "Karan",
#     "age": 22,
#     "skills": ["Python", "Java", "Node.js"],
#     "address": {
#         "city": "Surat",
#         "state": "Gujarat"
#     }
# }
# '''

# data = json.loads(response)
# # print(data["skills"][0])
# # print(data["skills"][2])
# # print(data["address"]["city"])
# # print(data["address"]["state"])

# ===== use for loop and if ======

# for skill in data["skills"]:
#     if "Python" in skill:
#         print(f"{skill} is my skill")


# ========== PROBLEM 1 ==========


import json

response = '''
[
    {
        "name": "Karan",
        "age": 22,
        "skill": "Python"
    },
    {
        "name": "Rahul",
        "age": 23,
        "skill": "Java"
    },
    {
        "name": "Amit",
        "age": 21,
        "skill": "Python"
    }
]
'''

students = json.loads(response)

# def find_python_students(students):
#     for student in students:
#         if student["skill"] == "Python":
#             print(student['name'])

# find_python_students(students)

# ======= RETURN USE =======
# 
# def find_python_students(students):
#     python_students = []
#     for student in students:
#         if student["skill"] == "Python":
#             python_students.append(student["name"])
#     return python_students

# result = find_python_students(students) 
# print(result)


# ======== counting python students ========

# def count_python_students(students):
#     count = 0
#     for student in students:
#         if student["skill"] == "Python":
#             count = count + 1
#     return count

# result = count_python_students(students) 
# print(result)

# ======= find avg. age of python students ======== 

# def average_python_age(students):    
#     count = 0
#     total_age = 0
#     for student in students:
#         if student["skill"] == "Python":
#             total_age = total_age + student["age"]
#             count = count + 1
#     avg = total_age / count
#     return avg

# result = average_python_age(students) 
# print(result)


# ========== PROBLEM 3 ==========

import json

response = '''
[
    {
        "name": "Karan",
        "department": "IT",
        "skills": ["Python", "Node.js"],
        "salary": 30000
    },
    {
        "name": "Rahul",
        "department": "HR",
        "skills": ["Excel", "Communication"],
        "salary": 25000
    },
    {
        "name": "Amit",
        "department": "IT",
        "skills": ["Python", "Java"],
        "salary": 35000
    }
]
'''

employees = json.loads(response) 

# def find_python_employees(employees):
#     python_employees = [] 
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             python_employees.append(employee['name'])
#     return python_employees

# result = find_python_employees(employees)
# print(result)
    

# # ========== total salary of python developer =========

# def calculate_python_salary(employees):
#     total_salary = 0
    
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             total_salary = total_salary + employee["salary"]    
#     return total_salary

# result = calculate_python_salary(employees)
# print(result)


# # ========== Python employees ki highest salary =========

# def highest_python_salary(employees):
#     highest_salary = 0
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             if employee["salary"] > highest_salary:
#                 highest_salary = employee["salary"]    
#     return highest_salary

# result = highest_python_salary(employees)
# print(result)

# ======== highest salary wale employee ka naam + salary ========
# def highest_python_salary(employees):
#     highest_salary = 0
#     highest_salary_name = ""
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             if employee["salary"] > highest_salary:
#                 highest_salary = employee["salary"]
#                 highest_salary_name = employee["name"]    
#     return highest_salary, highest_salary_name

# result1, result2 = highest_python_salary(employees)
# print(result1,result2)

# ======== # Filter Python employees and sort by salary ========

# def find_python_employees(employees):
#     python_employees = []
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             python_employees.append(f"{employee['name']} - {employee['salary']}")
#     sorted_list = sorted(python_employees)
#     return sorted_list

# result = find_python_employees(employees)
# print(result)


# # ======== find python employees according to desc selary ========

# def find_python_employees(employees):
#     python_employees = []
#     for employee in employees:
#         if "Python" in employee["skills"]:
#             python_employees.append(employee)
#     sorted_list = sorted(python_employees,key = lambda employee: employee["salary"],
#     reverse=True)
#     return sorted_list

# result = find_python_employees(employees)

# for employee in result:
#     print(f"{employee['name']} - {employee['salary']}")



# ======== find python employees according to desc selary ========

# def find_it_employees(employees):
#     it_employees = []
#     for employee in employees:
#         if "IT" in employee["department"]:
#             it_employees.append(employee["name"])
#     return it_employees

# result = find_it_employees(employees)
# print(result)




# ======== find python employees according to desc selary ========

# def find_it_employees(employees):
#     total_salary = 0
#     for employee in employees:
#         if "IT" in employee["department"]:
#             total_salary = total_salary + employee["salary"]
#     return total_salary

# result = find_it_employees(employees)
# print(result)