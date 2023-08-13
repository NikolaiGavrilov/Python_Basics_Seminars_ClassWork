
# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

def fill_list() -> list:
    list_to_fill = []
    for i in range(5):
        list_to_fill.append(int(input(f"Input number {i+1}: ")))
    return list_to_fill

def check_pairs(list_to_check) -> int:
    pair_sum = 0
    occurence_num = 0
    for i in range(len(list_to_check)):
        temp = list_to_check[i-1]
        if i != len(list_to_check)-1:
            i = i+1
        if temp == list_to_check[i]:
            occurence_num +=1
        if occurence_num == 2:
            pair_sum += 1
    return pair_sum

user_list = fill_list()
print("Your list is: {}".format(user_list))
print("Your result is: {} pairs".format(check_pairs(user_list)))



