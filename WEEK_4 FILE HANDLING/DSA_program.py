# ====== do numbers find karne hain jinka sum target ke equal ho. ======
# numbers = [2, 7, 11, 15]
# target = 18

# for i in range(len(numbers)):
#     for j in range(i + 1,len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print([numbers[i],numbers[j]])


# ====== Move all zeros to the end  ======
# numbers = [0, 1, 0, 3, 12]
# result = []
# count_zero=0
# for i in range(len(numbers)):
#     if numbers[i] != 0:
#         result.append(numbers[i])
#     else:
#         count_zero = count_zero + 1

# for i in range(count_zero):
#     result.append(0)
# print(result)


# ====== Rotate List Right by first 1 or 2 ======
# numbers = [10, 20, 30, 40, 50]
# right_rotate = []
# right_rotate.append(numbers[(len(numbers)-2)])
# right_rotate.append(numbers[(len(numbers)-1)])
# for i in range(0,len(numbers)-2):
#     right_rotate.append(numbers[i])
# print(right_rotate)


# ====== Rotate List left by first 1 or 2  ======
# numbers = [10, 20, 30, 40, 50]
# left_rotate = []
# for i in range(2,len(numbers)):
#     left_rotate.append(numbers[i])
# left_rotate.append(numbers[0])
# left_rotate.append(numbers[1])

# print(left_rotate)

# ====== general rotation by k positions ======

# numbers = [10, 20, 30, 40, 50]
# k = 3
# result = []

# for i in range(k, len(numbers)):
#     result.append(numbers[i])

# for i in range(k):
#     result.append(numbers[i])

# print(result)

# ====== Linear Search ======
# numbers = [10, 20, 30, 40, 50,60]
# target = 30

# low = 0
# high = len(numbers)-1
# while low <= high:
#     mid = (low + high)//2
#     if target > numbers[mid]:
#         low = mid+1
#     elif target < numbers[mid]:
#         high = mid-1
#     else:
#         print(mid)
#         break
# else:
#     print(f"{target} is not found")


# ====== Palindrome List ======
# numbers = [1, 2, 3, 0, 1]
# is_palindrome = True
# for i in range(len(numbers) //2):
#     if numbers[i] == numbers[len(numbers)-1-i]:
#         is_palindrome = True
#     else:
#         is_palindrome = False
#         break
# print(is_palindrome)
        
# ====== find Duplicate ======
# numbers = [10, 20, 10, 30, 20, 10]
# duplicate = []
# for i in range(len(numbers)):
#     for j in range(i + 1,len(numbers)):
#         if numbers[i] == numbers[j]:
#             if numbers[i] not in duplicate:
#                 duplicate.append(numbers[i])
# print(duplicate)

# ====== Find missing number ======
# numbers = [1, 2, 3, 5, 6]
# actual_total = 0
# total = 0
# for i in range(1,7):
#     actual_total = actual_total + i
# for i in range(len(numbers)):
#     total = total + numbers[i]

# missing_number = actual_total - total
# print(missing_number)

# ====== Smallest and Second Smallest ======

# numbers = [10, 25, 7, 40, 15]

# largest_number = numbers[0]
# second_largest_number = numbers[0]

# for i in numbers:
#     if i > largest_number:
#         second_largest_number = largest_number
#         largest_number = i
#     elif i > second_largest_number:
#         second_largest_number = i

# print(second_largest_number)

# ====== Smallest and Second Smallest ======

# numbers = [10, 5, 20, 3, 15]
# smallest = numbers[0]
# second_smallest = numbers[0]
# for i in numbers:
#     if i < smallest:
#         second_smallest = smallest
#         smallest = i
#     elif i < second_smallest:
#         second_smallest = i
# print(f"Smallest : {smallest}")
# print(f"Second_smallest : {second_smallest}")

# ====== Find pairs with given sum ======

# numbers = [2, 4, 3, 5, 7, 8]
# target = 10

# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print([numbers[i],numbers[j]])

# ====== Merge Two Sorted Lists =====

# list1 = [1, 3, 5]
# list2 = [2, 4, 6, 9, 10]

# i = 0
# j = 0
# merged = []
# while i < len(list1) and j < len(list2):
    
#     if list1[i] < list2[j]:
#         merged.append(list1[i])
#         i = i + 1
#     elif list1[i] > list2[j]:
#         merged.append(list2[j])
#         j = j + 1
#     elif list1[i] == list2[j]:
#         merged.append(list1[i])
#         i = i + 1
#         j = j + 1

# while i < len(list1):
#     merged.append(list1[i])
#     i = i+1
# while j < len(list2):
#     merged.append(list2[j])
#     j = j + 1
# print(merged)


# ====== Reverse String ======
# text = "python"
# rev_str = " "

# for i in range(len(text)-1,-1,-1):
#     rev_str = rev_str + text[i]
# print(rev_str)


# ====== Check Palindrom ======
# text = "madam"
# pdrm_text = ""
# is_palindrom = True
# for i in range(len(text)//2):
#     if text[i] == text[len(text)-1-i]:
#         is_palindrom = True
#     else:
#         is_palindrom = False
#         break
# print(is_palindrom)


# ====== Count Vowels ======
text = "programming"
vowel = "aeiou"
count = 0
for i in text:
    if i in vowel:
        count = count + 1
print(count)
if count == 0:
    print("No vowels in text")