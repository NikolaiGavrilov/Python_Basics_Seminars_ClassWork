# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random

def fix_academic_performance(grades) -> list:
    max_grade = max(grades)
    min_grade = min(grades)
    
    for i in range(len(grades)):
        if grades[i] == max_grade:
            grades[i] = min_grade

    return grades

length = int(input('How many grades do you have? Input your number:'))
user_grades = []
for i in range(length): 
    user_grades.append(random.randint(1,5))
print (user_grades)
print (fix_academic_performance(user_grades))