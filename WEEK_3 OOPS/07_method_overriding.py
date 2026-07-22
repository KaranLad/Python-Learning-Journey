class Animal:
    def speak(self):
        print("Animal can speak")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d1 = Dog()
d1.speak()