import random

# 1. randint()
number = random.randint(1, 10)
print("Random integer:", number)

# 2. choice()
names = ["Karan", "Rahul", "Amit"]
selected_name = random.choice(names)
print("Selected name:", selected_name)

# 3. shuffle()
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# 4. random()
value = random.random()
print("Random float:", value)