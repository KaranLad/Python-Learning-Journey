num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

#check which number is larger
if num1 > num2:
    print(num1, "is larger than", num2)

elif num2 > num1:
    print(num2, "is larger than", num1)

else:
    print("Both numbers are equal.")