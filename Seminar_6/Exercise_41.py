# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод: 
# 5 
# 1 2 3 4 5 
# Ввод:
# 5
# 1 5 1 5 1
# Вывод: 
# 0 
# Вывод:
# 2

def fill_list() -> list:
    list_1 = []
    for i in range(5):
        list_1.append(int(input(f'Input number {i+1}: ')))
    return list_1

def check_neighbours(list_to_check) -> int:
    equal_neighbour_cases = 0
    for i in range(len(list_to_check)):
        if list_to_check[i-2] == list_to_check[i]:
            equal_neighbour_cases += 1
    return(equal_neighbour_cases)

user_list = fill_list()
print(user_list)
user_result = check_neighbours(user_list)
print(f'Your result is {user_result} cases with equal neighbours')



