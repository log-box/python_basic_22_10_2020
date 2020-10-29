"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

user_input = True
while user_input:
    user_input = input('Введите число, или введите break для выхода из программы\n')
    if user_input == 'break':
        break
    user_input = int(user_input)
    if my_list.count(user_input) == 0:
        my_list.append(user_input)
    else:
        if my_list.count(user_input) == 1:
            i = my_list.index(user_input)
            my_list.insert(i, user_input)
        elif my_list.count(user_input) > 1:
            first_index = my_list.index(user_input) + my_list.count(user_input)
            my_list.insert(first_index, user_input) #определить индекс для вставляния! надо воткнуть после последнего
    str_list = [str(a) for a in my_list]
    str_list = sorted(str_list)
    str_list.reverse()
    print('Пользователь ввел число {0}. Результат: {1}.'.format(user_input, (', '.join(str_list))))