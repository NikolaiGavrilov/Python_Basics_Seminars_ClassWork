# Задача №3. 
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32



print('Input the number of students in class 1: ')
class_1 = int(input())
print('Input the number of students in class 2: ')
class_2 = int(input())
print('Input the number of students in class 3: ')
class_3 = int(input())

# Вариант с math
# import math
# result = (math.ceil(class1/2) + math.ceil(class2/2) + math.ceil(class3/2))

result = ((class_1 // 2) + (class_1 % 2)) + ((class_2 // 2) + (class_2 % 2)) + ((class_3 // 2) + (class_3 % 2))

print(f"You will need {result} tables")