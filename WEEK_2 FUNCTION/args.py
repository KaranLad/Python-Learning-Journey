# *args Example

def add(*numbers): # *args = *number
    total = 0

    for num in numbers:
        total += num

    print("Total:", total)


add(10, 20)
add(10, 20, 30)
add(5, 10, 15, 20)