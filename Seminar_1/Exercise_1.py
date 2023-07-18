# Задача №1. 
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math
dist_per_day = int(input('Set the distance per day: '))
overall_dist = int(input('Set the distance your car needs to overcome: '))
result = math.ceil(overall_dist/dist_per_day)
print(f'You will need {result} days')
