# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10

import math

def filter_list(list_to_filter):
    list_edited = list(filter(lambda x: x[0] != x[1], list_to_filter))
    return list_edited

def find_sq(list_to_find_sq):
    sq_found_list = list(map(lambda x: x[0]*x[1]*math.pi, list_to_find_sq))
    return sq_found_list

def find_planet (orbits_sq_list, max_sq_data):
    for i in range(len(orbits_sq_list)):
        if orbits_sq_list[i] == max_sq_data:
            return i

def find_farthest_orbit(orbits):
    orbits_filtered = filter_list(orbits)
    orbits_sq = find_sq(orbits_filtered)
    max_sq = max(orbits_sq)
    index_of_planet_max_sq = find_planet(orbits_sq, max_sq)
    return orbits_filtered[index_of_planet_max_sq]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))



# orbits_filtered = filter_list(orbits)
# print(f'Orbits with no equal axis: {orbits_filtered}')
# orbits_sq = find_sq(orbits_filtered)
# print(f'Square of orbits: {orbits_sq}')
# max_sq = max(orbits_sq)
# print(f'Max square is: {max_sq}')
# index_of_planet_max_sq = find_planet(orbits_sq, max_sq)
# print(f'Planet with max square is planet {orbits_filtered[index_of_planet_max_sq]}')
