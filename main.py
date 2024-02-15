# while True:
#     a = int(input('Введите число от 1 до 9: '))
#     if 1 <= a <= 9:
#         print(a)
#         break
#     else:
#         print('Неправильно')

# numb = int(input('Введите число: '))
#
# for i in range(1, 11):
#     print(f'{numb} * {i} = {numb *i}')

# while True:
#     b = int(input('Выберете валюту какую вам надо поменять грн[1], $[2],: '))
#     c = int(input('Выберете валюту какую вам надо получить грн[1], $[2],: '))
#     a = int(input('Введите сумму: '))
#     if b == 1 and c == 2:
#         change = 0.27 * a
#         print(change)
#     elif b == 2 and c == 1:
#         change = 35.56 * a
#         print(change)

# numb1 = int(input('Введите число1'))
# numb2 = int(input('Введите число2'))
# while True:
#     numb3 = int(input('Введите число3'))
#     if numb3 > numb2 or numb3 < numb1:
#         print()
#     else:
#         break
#
# for i in range(numb1, numb2+1):
#     if i == numb3:
#         print('!', i, '!', end = ' ')
#     else:
#         print(i, end=' ')

import random
number = random.randint(1, 500)
print(number)
import time
start = time.time()
end = time.time()

while True:
    numb = int(input('Введите число'))
    if number-numb < 10 or number-numb > -10:
        print('Горячо')
    elif number-numb < 20 or number-numb > -20:
        print('Тепло')
    elif number-numb < 20 or number-numb > -50:
        print('холодно')
    elif numb == number:
        break


print(f'Пройшло{round(end - start, 2)}сек')



