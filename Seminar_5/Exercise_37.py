# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def reverse_order(number_of_numbers) -> list:
    if number_of_numbers == 2:
        num = int(input('Input your number: '))
        next_num = int(input('Input your number: '))
        # temp = num
        # num = next_num
        # next_num = temp
        return next_num, num

user_number_of_nums = 2
print(reverse_order(user_number_of_nums))