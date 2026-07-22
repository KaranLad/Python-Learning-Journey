# ==== SUPER CUNSTRUCTOR ====

class Animal:
    def __init__(self):
        print("Animal Constructor")

# ==== NEW CLASS ====

class Dog(Animal):
    def __init__(self):
        super().__init__()   #Call parent class method
        print("Dog Constuctor")

d1 = Dog()