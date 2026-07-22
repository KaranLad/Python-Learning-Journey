
print("\n===== Car Management =====")
print("1. Display Brand")
print("2. Change Brand")
print("3. Exit")
print("="*25)
class Car:
    def __init__(self,brand_name):
        self.brand_name = brand_name
    def change_brand(self,new_brand):
        self.brand_name = new_brand 
    def display(self):
        print(f"Car Brand : {self.brand_name}")  


c1 = Car("BMW")

while True:
    choice=0

    print("Select choice")
    choice = int(input("Enter choice: "))

    if choice==1:
        c1.display()

    elif choice == 2:
        new_brand = input("Enter your favourite brand: ")
        print("Brand Updated Successfully")
        c1.change_brand(new_brand)

    elif choice == 3:
        print("Exit")
        break

    else :
        print("Invalid choice ! Pleace try again ")
        

