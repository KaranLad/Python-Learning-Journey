#login system

print("======= LOGIN SYSTEM ======= \n")
print("======= REGISTRATION SYSTEM ======= \n")

#Register 

Full_Name = input("Enter full name: ")
print(f"welcome {Full_Name} in Registraion form!")

#Enter your phone number
while True:
    Phone_No = input("Enter your phone Number: ")
    if len(Phone_No) == 10 and Phone_No.isdigit():
        break
    print("Phone number must contain exactly 10 digits.")

#Enter your gemail id
while True:
    Email_ID = input("Enter your Gmail_ID: ")
    if "@gmail.com" in Email_ID:
        break 
    print("Invalid Email! Please enter a Gmail address.")
#Create password

create_password = input("Create a Password: ")
same_password = input("Re_enter your password: ")
Password1 = ("")

while True:

    if create_password == same_password:
        Register_Password = create_password
        print("Password is created...")
        break
    print("Passwords do not match.")
    
    

print("Register Seccefully \n")

print("====== Login Form ======\n")
attempt = 1
while True:
    Login_ID = input("Enter Login ID: ")
    if Login_ID == Email_ID:
        break
    print("Wrong email_ID! Check email_ID..")
    while attempt <=3:
            Enter_Password = input("Enter your Password: ")
            if Enter_Password == Register_Password:
                print("Login Successfully...")
                break

            print("Wronge Password! ")
            attempt += 1
            if attempt > 3:        
                print("your account is locked")    
   

