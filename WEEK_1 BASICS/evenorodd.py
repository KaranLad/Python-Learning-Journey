#function createa
def is_even(number):
    
    #check the number are even or odd
    if number % 2 == 0:
      return True
    else:
      return False

#function call 
print(is_even(10))
print(is_even(7))
print(is_even(0))