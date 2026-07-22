# ======= Inheritance + Method Overriding = Runtime Polymorphism =======

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog Barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat Meows")


# d1 = Dog()
# c1 = Cat()

# d1.speak()
# c1.speak()

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()      #super() is call to animal speak()
        print("Dog Barks")

class Cat(Animal):
    def speak(self):
        print("Cat Meows")


d1 = Dog()
c1 = Cat()

d1.speak()
c1.speak()