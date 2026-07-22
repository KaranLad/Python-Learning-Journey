
# ======================================================
# Project Name : Bank Management System
# Version      : V1.0
# Author       : Karan Lad
#
# Features:
# ✓ Create Account
# ✓ Deposit Money
# ✓ Withdraw Money
# ✓ Change PIN
# ✓ Transaction History
# ✓ Menu-Driven Program
# ======================================================

# ===== Bank Account Class =====

class BankAccount:
    # ===== Constructor =====
    def __init__(self):
        self.name = ""
        self.__pin = ""
        self.__balance = 0
        self.account_created = False
        self.history = []

# ===== Create Account =====
    def create_account(self):
        if not self.account_created:
            self.name = input("Enter Name : ")
            self.__pin = (input("Enter PIN : "))
            print("Account created successfully")
            self.account_created = True
        else:
            print("Account is already Exists!")

# ===== Display Account Details =====
    def display(self):
        print(" ====== Account Details ====== \n")
        print(f"Name : {self.name}")
        print(f"Balance : {self.__balance}")

        # ===== Deposit Money =====

    def deposit(self):
        if self.account_created:
            enter_pin = input("Enter PIN : ")
            if enter_pin == self.__pin :
                add_money = int(input("Add Amount : "))
                self.history.append(f"Deposit : +{add_money}")
                self.__balance += add_money
                print("Amount Deposit Successfully! \n")
                print(f"After Balance : {self.__balance}")
            else:
                print("Invalid PIN!")
        else:
            print("Please Create Account First")

# ===== Withdraw Money =====
    def withdraw(self):
        if self.account_created:
            enter_pin = input("Enter PIN : ")
            if enter_pin == self.__pin :
                withdraw_amount = int(input("Withdraw Amount : "))
                if  withdraw_amount <= self.__balance:
                    self.history.append(f"Withdraw : -{withdraw_amount}")
                    self.__balance -= withdraw_amount
                    print("Withdraw Successfully!")
                    print(f"After Balance : {self.__balance}")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid PIN!")
        else:
            print("Please Create Account First")

# ===== Transaction History =====
    def transaction_history(self):
        print(" ===== Transaction History =====\n")
        if self.history:
            for item in self.history:
                    print(item)
        else:
            print("No Transactions Found!")

# ===== Change PIN =====
    def change_pin(self):
        if self.account_created:
            old_pin = input("Enter old pin : ")
            if old_pin == self.__pin:
                new_pin = input("Enter new pin : ")
                self.__pin = new_pin
                print("PIN updated Sccessfully!")
            else:
                print("Invalid Old PIN")
        else:
            print("Please Create Account First")

# ===== Exit =====
    def exit(self):
        print("Exit!")


account = BankAccount()
# ===== Main Program =====
while True:
    print("========= BANK MENU =========")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Change PIN")
    print("6. Display History")
    print("7. Exit")
    choice = 0

    choice = int(input("enter choice : "))
    print()

    if choice == 1:
        account.create_account()
    elif choice == 2:
        account.deposit()
    elif choice == 3:
        account.withdraw()
    elif choice == 4:
        account.display()
    elif choice == 5:
        account.change_pin()
    elif choice == 6:
        account.transaction_history()
    elif choice == 7:
        account.exit()
        break
    else:
        print("Invalid Choice!. Please try again ")

