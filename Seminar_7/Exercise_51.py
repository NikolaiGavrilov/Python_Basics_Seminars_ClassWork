# Задача №51. Общее обсуждение
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same

# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if objects == new_objects:
#         print('same')
#     else:
#         print('different')

# values = [0, 2, 10, 6]
# user_characteristic = lambda x: x
# same_by(user_characteristic, values)

def same_by(characteristic, objects):
    new_objects = list(filter(characteristic, objects))
    print(new_objects)

    if new_objects == objects:
        return True
    return False

def user_characteristic(x):
    return x % 2 == 0

values = [0, 2, 10, 6]
print(same_by(user_characteristic, values))