# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def check_simple_number(num) -> str:
    if num == 0:
        flag = "Impossible to check!"
    if num == 1:
        flag = "no" 
    if num > 3:
        for i in range(2, num//2+1):
            if num % i == 0:
                flag = "no"
                break
            else:
                flag = "yes"
    elif num in (2,3):
        flag = "yes"
    return flag

user_num = int(input("Input your number to check: "))
print(check_simple_number(user_num))

