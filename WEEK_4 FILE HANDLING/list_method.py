# numbers = [10, 25, 7, 40, 15]
# min_num=numbers[0]
# for i in numbers:
#     if i < min_num:
#         min_num = i
# print(min_num)/

# numbers = [10, 15, 22, 31, 40, 55, 60]
# total = 0
# count = 0
# for i in numbers:
#     total = total + i
#     count=count + 1

# avg = total/count
# print(total)
# print(count)
# print(avg)

# ===== find 25 in list =====

# numbers = [10, 20, 30, 40, 50]

# target = 40
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print(i)

# ====== find unique value and in new list ======

# numbers = [10, 20, 10, 30, 20, 10]
# unique =[]
# for i in range(0,len(numbers)-1,1):
#     if numbers[i] not in unique:
#         unique.append(numbers[i])
# print(unique)

# # ====== find frequency ======
# numbers = [10, 25, 7, 40, 15]
# largest_number = numbers[0]
# second_largest_number = numbers [0]
# for i in numbers:
#     if i > largest_number:
#         second_largest_number = largest_number
#         largest_number = i
#     elif i > second_largest_number:
#         second_largest_number = i
# print(second_largest_number)


# ====== find even or odd ======
# numbers = [10, 15, 22, 31, 40, 55, 60]
# even = []
# odd = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even.append(numbers[i])
#     else:
#         odd.append(numbers[i])
# print(even)
# print(odd)

# ====== common value find ======

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]
# list=[]
# for i in list1:
#     if i in list2:
#         list.append(i)
# print(list)

# ====== add list ======
# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# list3 = []

# for i in list1:
#     list3.append(i)
# for i in list2:
#     list3.append(i)
# print(list3)