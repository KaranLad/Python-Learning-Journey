# class Car:
#     def __init__(self,brand_name):
#         self.brand_name = brand_name
#     def display(self):
#         print(f"Car Brand : {self.brand_name}")  

# c1 = Car("BMW")
# c2 = Car("TATA")

# c1.display()
# c2.display()



# ====== Methods with Parameters ======

class Car:
    def __init__(self,brand_name):
        self.brand_name = brand_name
    def change_brand(self,new_brand):
        self.brand_name = new_brand 
    def display(self):
        print(f"Car Brand : {self.brand_name}")  


c1 = Car("BMW")
c1.display()
c1.change_brand("TATA")
c1.display()