# =========================================
# Project : Student Marks Manager
# Author  : Karan Lad
# Version : 2.0
# Date    : 15-07-2026
# =========================================

total_students = int(input("how many students?"))

students = []
def add_students():
    global total_students
    total_students = int(input("how many students?"))
    for i in range(total_students):
        name = input("Enter Student name: ")
        students.append(name)

marks = []
total = 0

def add_marks():
    global total
    global total_students
    for i in range(total_students):
        mark = int(input("Enter Student mark: "))
        marks.append(mark)
        total += mark
    

def show_report():
    Highest_marks = marks[0]
    highest_student = students[0]
    Lowest_marks = marks[0]
    lowest_student = students[0]
    
    for i in range(total_students):
        print(f"{students[i]} - {marks[i]}")
        if marks[i]>Highest_marks:
            Highest_marks=marks[i]
            highest_student=students[i]
        if marks[i]<Lowest_marks:
            Lowest_marks=marks[i]
            lowest_student=students[i]
    
    avg= total/len(marks)

    print("-"*25)
    print(f"Average Marks: {avg}")
    print(f"Highest Marks: {highest_student} - {Highest_marks}")
    print(f"Lowest Marks: {lowest_student} - {Lowest_marks}")
