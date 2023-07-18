# Задача №7. 
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

natural_number = int(input('Input a natural number: '))
while natural_number < 1:
    natural_number = int(input('Your number is not natural. Try another number: '))

if natural_number % 4 == 0 and natural_number % 100 != 0 or natural_number % 400 == 0:
    print('Yes')
else:
    print('No')
