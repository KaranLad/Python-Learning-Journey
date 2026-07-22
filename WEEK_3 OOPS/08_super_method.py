# ==== PARENT CLASS ====

class Animal:
    def speak(self):
        print("Animal can speak")

# ==== CHILD CLASS ====

class Dog(Animal):
    def speak(self):
        super().speak()   #Call parent class method
d1 = Dog()
d1.speak()