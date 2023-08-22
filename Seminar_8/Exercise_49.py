# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной



# import json

# phonebook = {"Дядя Петя": {"phone_numbers": ["12345", "12346"], "birthday": "01.03/1996", "e-mail": "petya@mail.ru"} }

# with open("phonebook.json", "w", encoding = "utf-8") as phonebookjson:
#     phonebookjson.write(json.dumps(phonebook, ensure_ascii = False))

def new_contact (list_names, list_phone_numbers):
    new_info_name = input('Введите ФИО: ')
    new_info_phone = int(input('Введите номер телефона: '))
    print('Контакт успешно добавлен')
    list_names.append(new_info_name)
    list_phone_numbers.append(new_info_phone)
    with open('Seminar_8\phone_book.txt', 'a', encoding = "utf-8") as phonebook:
        phonebook.write(f'{new_info_name}, ')
        phonebook.write(f'{new_info_phone}\n')

def find_contact():
    contact_to_find = input('Введите имя, фамилию или телефонный номер для поиска: ')
    phonebook = open('Seminar_8\phone_book.txt', encoding = 'utf-8').readlines()
    contact_found = False
    for i in iter(phonebook):
        if contact_to_find in i:
            contact_found = True
            print(f'Найден абонент {i}')
    if contact_found == False:
        print('Абонент не найден')

phone_book_names = ['Иванов Иван Иванович', 'Петров Пётр Петрович', 'Сергеев Сергей Сергеевич']
phone_book_numbers = [88005553535, 89999999, 89220010103]
print('1 - Добавить контакт, 2 - найти контакт')
choice = int(input('Введите номер своего выбора: '))
if choice == 1:
    new_contact(phone_book_names, phone_book_numbers)
elif choice == 2:
    find_contact()
else:
    print('Ошибка ввода') 
    
# def find_contact_general(list_names, list_phone_numbers):
#     print('Как будем искать? 1 - по ФИО, 2 - по телефону')
#     choice = int(input('Введите номер выбора: '))
#     if choice == 1:
#        find_contact_name(list_names, list_phone_numbers)
#     elif choice == 2:
#         find_phone_number(list_names, list_phone_numbers)

# def find_contact_name(list_names, list_phone_numbers):
#     info_name = input('Введите ФИО для поиска: ')
#     for i in range(len(list_names)):
#         if info_name == list_names[i]:
#             remember_index = i
#     print(f'Найден абонент {list_names[remember_index]}, {list_phone_numbers[remember_index]}')

# def find_phone_number(list_names, list_phone_numbers):
#     info_phone = int(input('Введите номер телефона для поиска: '))
#     for i in range(len(list_phone_numbers)):
#         if info_phone == list_phone_numbers[i]:
#             remember_index = i
#     print(f'Найден абонент {list_names[remember_index]}, {list_phone_numbers[remember_index]}')


