class Student:
    def __init__(self):
        self.__name = "Karan"    # __name is a private variable
    
    def get_name(self):          # return value
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name          # return value

s1 = Student()
print(s1.get_name())

new_name = input("Enter Updated Name : ")
s1.set_name(new_name)
print(s1.get_name())
