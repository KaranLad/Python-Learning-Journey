class Animal:                 #Grand Parent class
    def eat(self):
        print("Animal Eats")

class Mammal(Animal):
    def walk(self):           #Parent class
        print("Mammal Walks")

class Dog(Mammal):     #Child Class
    pass

d1 = Dog()

d1.eat()
d1.walk()