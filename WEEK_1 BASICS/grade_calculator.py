#enter the student name
name = input("Enter your name: ")
#enter the marks of each subject(0-100)
maths = float(input("Enter your maths marks: "))
if maths < 0 or maths > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
science = float(input("Enter your science marks: "))
if science < 0 or science > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
hindi = float(input("Enter your hindi marks: "))
if hindi < 0 or hindi > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
gujarati = float(input("Enter your gujarati marks: "))
if gujarati < 0 or gujarati > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
english = float(input("Enter your english marks: "))
if english < 0 or english > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
sanskrit = float(input("Enter your sanskrit marks: "))
if sanskrit <0 or sanskrit > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

total_marks = maths + science + hindi + gujarati + english + sanskrit
print(f"Total marks obtained: {total_marks}")

#calculate the percentage
max_marks = 600
percentage = (total_marks / max_marks) * 100
print(f"Percentage: {percentage} %")

#check the grade based on the percentage
if percentage >= 90:
    grade = "A"

elif percentage >= 80:
    grade = "B"

elif percentage >= 70:
    grade = "C"

elif percentage >= 60:
    grade = "D"

elif percentage >= 50:
    grade = "E"

else:
    grade = "FAIL"

print(f"Grade: {grade}")
print(f"{name}, your grade is {grade}")

#summary of the marks
print(f"Summary of marks for {name}:")
print("\n========== RESULT ==========")
print(f"Student Name : {name}")
print(f"Total Marks  : {total_marks}/600")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print("============================")