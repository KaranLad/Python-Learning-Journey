# try-execute 
# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))
# result = (num1/num2)
# print(result)

try:
    age=int(input("enter your age : "))

    if age < 18:
        raise ValueError("not eligible for voting")
    print("Congratulation!")
    print("Eligible for voting")

except ValueError as e:
    print(e)
print("Program End")
