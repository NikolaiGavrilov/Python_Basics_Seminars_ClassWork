# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random
length = int(input('Input the length of your list:'))
list_of_numbers = []
i = 0
for i in range(length):
    list_of_numbers.append(int(input('Input your number: ')))
print(list_of_numbers)

count = 0
temp = 0

print(len(set(list_of_numbers)))


