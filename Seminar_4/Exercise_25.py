# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


user_string = 'a a a b c a a d c d d'.split()
my_dict, my_list = {}, []
for char in user_string:
    if char not in my_dict:
        my_list.append(char)
        my_dict[char] = 0
    else:
        my_dict[char] += 1
        my_list.append(f"{char}_{my_dict[char]}")

print(*my_list)
print(' '.join(my_list))
