# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# Вывод: 3 3 2 12

def not_in_list(list_1_check, list_2_check) -> list:
    result = []
    if len(list_1_check) >= len(list_2_check):
        for i in range(len(list_1_check)):
            if list_1_check[i] not in list_2_check:
                result.append(list_1_check[i])
    else:
        for i in range(len(list_2_check)):
            if list_2_check[i] not in list_1_check:
                result.append(list_2_check[i])
    return result


list_1 = [3, 1, 3, 4, 2, 4, 12]
print(list_1)
list_2 = [4, 15, 43, 1, 15, 1]
print(list_2)

list_3 = not_in_list(list_1, list_2)
print(list_3)
