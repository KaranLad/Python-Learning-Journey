class Car:
    def __init__(self, brand_name):   #call the object after created 
        self.brand_name = brand_name

c1 = Car("BMW")
c2 = Car("TATA")

print(c2.brand_name)