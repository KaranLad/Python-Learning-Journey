class Animal:                 #Parent class
    def eat(self):
        print("Animal Eats")

class Dog(Animal):            #child_1 class
    def bark(self):
        print("Dog Barks")

class Cat(Animal):            #child_2 class
    def meow(self):
        print("Cat Meows")

d1 = Dog()
c1 = Cat()

d1.eat()
d1.bark()

c1.eat()
c1.meow()