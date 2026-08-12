

class FileHandaling:
    def __init__(self):
        self.name=" "
        self.student_added=False

    def add_student(self):
        with open("students_records.txt","a") as file:
            self.name=input("Enter student name: ")
            file.write(self.name+"\n")
            self.student_added=True

    def show_student_details(self):
        if self.student_added:
            with open("students_records.txt","r") as file:
                print(file.read())
                
        else:
            print("don't add student name!,please create file")
    def exit(self):
        print("Exits!")


student_details = FileHandaling()
while True:
    print(" ===== MENU ===== ")
    print("1.Add student")
    print("2.Show students")
    print("3.exit")


    choice = int(input("enter choice : "))
    print()
    
    if choice == 1:
        student_details.add_student()
    elif choice == 2:
        student_details.show_student_details()
    elif choice == 3:
        student_details.exit()
        break
    else:
        print("invalid choice!")