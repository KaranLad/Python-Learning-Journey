# =========================================
# Project : Student Marks Manager
# Author  : Karan Lad
# Version : 1.0
# =========================================

#====== Add Students ======

total_students = int(input("How many students?: "))
total = 0
students= []
print("-"*25)
for i in range(total_students):
    name=input("Enter Student name: ")
    students.append(name)

#====== Add Marks ======

marks= []

for i in range(total_students):
    mark=int(input("Enter Student marks: "))
    marks.append(mark)

    total+=mark
avg=total/len(marks)

#====== Show Report ======

for i in range(total_students):
    print(f"Students name: {students[i]} Marks: {marks[i]}")

#Average marks
print("-"*25)
print(f"Average marks:{avg:.2f}")

#check which student have highest marks or lowest marks

Highest=marks[0]
highest_student=students[0]
Lowest=marks[0]
lowest_student=students[0]

for i in range(total_students):
    if marks[i]>Highest:
        Highest=marks[i]
        highest_student=students[i]

    if marks[i]<Lowest:
        Lowest=marks[i]
        lowest_student=students[i]

print("-"*25)
print(f"Highest Marks: {highest_student}-{Highest}")
print(f"Lowest Marks: {lowest_student}-{Lowest}")
