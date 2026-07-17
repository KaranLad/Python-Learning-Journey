def menu():
    print("======= MENU =======")

menu()
menu()
menu()

# === create function with parameter "name" === 
def student(name):
    print("Welcome",name)

#function call with different arguments
student("Karan")
student("Latish")
student("Vivek")

# === create function with parameter "name","age" === 

def student(name,age):
    print(f"name:{name}")
    print(f"age: {age}")


#function call with different arguments
student("Karan",22)
student("Latish",25)
student("Vivek",23)

# calculator function
print("===== Calculator =====")
def calculator(num1,num2):
    print(f"Addition      : {num1 + num2}")
    print(f"Subtraction   : {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division      : {num1 / num2}\n")

calculator(20,10)
calculator(30,4)
calculator(10,5)

# === create function with parameter "name","age" === 

def student(name,marks):
    print(f"name  : {name}")
    print(f"marks : {marks}")
    if marks >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")

#function call with different arguments
student("Karan",62)
student("Latish",95)
student("Vivek",73)
