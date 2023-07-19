# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

days_num = int(input("Input the number of days: "))

temperature_list = [] 
for i in range(days_num):
    temperature_list.append(int(input(f"Input temperature (day {i+1}):")))

temperature_measurement_day = 0
count = 0

for i in temperature_list:
    if i > 0:
        count += 1
    else:
        if count > temperature_measurement_day:
            temperature_measurement_day = count
        count = 0
if count > temperature_measurement_day:
            temperature_measurement_day = count

print(temperature_measurement_day)