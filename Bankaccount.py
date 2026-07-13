
def withdraw(balance,amount):
    print(f"Balance before   : {balance}")
    print(f"Withdraw         : {amount}")

    if amount <= 0 :
        print("Invalid Withdraw Amount")
        
    elif amount <= balance:
        print("Withdraw Successful")
        print(f"Balance after    : {balance - amount}")

    else:
        print("Insufficient Balance")
        print(f"Current Balance   : {balance}")

#withdraw function call
withdraw(1000,500)
print("-"*30)
withdraw(4000,1500)
print("-"*30)
withdraw(6000,-500)
print("-"*30)
withdraw(20000,100000)
print("-"*30)
withdraw(30000,30000)

