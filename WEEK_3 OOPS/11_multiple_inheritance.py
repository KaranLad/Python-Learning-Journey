class Father:                 #Grand Parent class
    def work(self):
        print("Father Works")

class Mother:
    def cook(self):           #Parent class
        print("Mother Cooks")

class Child(Father,Mother):     #Child Class
    pass

c1 = Child()

c1.work()
c1.cook()