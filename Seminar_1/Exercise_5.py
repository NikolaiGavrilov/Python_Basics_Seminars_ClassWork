# Задача №5. 
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6
# 1 2 3 4 5 6
# 6 5 4 3 2 1

carriage_from_end = int(input('Input the number of carriage from train\'s end: '))
carriage_from_head = int(input('Input the number of carriage from train\'s head: '))

if carriage_from_end != carriage_from_head:
    result = (carriage_from_head + carriage_from_end - 1)
    print(result)
else:
    print("It's impossible to count the number of carriages in the train")