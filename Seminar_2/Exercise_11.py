# Задача 11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
    
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

your_num = int(input("Input a natual number: "))
while your_num < 0:
    your_num = int(input("Your number is not natual. Try again: "))

previous_num = 0
next_num = 1
summ_num = 0
count = 2
if your_num == 1:
    print(f"Your number is №2 and №3 in the sequence of Fibbonacci numbers.")
elif your_num == 0:
    print(f"Your number is №1 in the sequence of Fibbonacci numbers.")
else:
    while summ_num < your_num:
        summ_num = previous_num + next_num
        previous_num = next_num
        next_num = summ_num
        count +=1
    else:
        if your_num == next_num:
            print(f"Your number {your_num} is a Fibonacci number.")
            print(f"It is №{count} in the sequence of Fibbonacci numbers.")
        else:
            print("Your number is not a Fibonacci number")
            print(-1)
