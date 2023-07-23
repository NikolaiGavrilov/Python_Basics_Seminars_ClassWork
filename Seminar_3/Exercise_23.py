# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

length = int(input('Set the length of your sequence:'))
list_of_numbers = []
i = 0
for i in range(length):
    list_of_numbers.append(int(input(f'Input number {i}: ')))
print(list_of_numbers)

count = 0
for i in range(length-1):
    temp_1 = list_of_numbers[i]
    temp_2 = list_of_numbers[i+1]
    if list_of_numbers[i] < list_of_numbers[i+1]:
        count +=1
        print (f"{temp_1} < {temp_2}")
print(f"Result: {count} counts" )


# Второй вариант решения:
# nums = [1, 2, 3, 1, 2]
# count = 0
# for i in range(1, len(nums)):
#     if nums[i - 1] < nums[i]:
#         count += 1
# print(count)
