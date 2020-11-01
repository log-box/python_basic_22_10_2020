"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(numetor, denomitor):
    if not numetor.isalpha() and not denomitor.isalpha():
        num = int(numetor)
        den = int(denomitor)
        try:
            result = num / den
            print('результат: ', result)
            return result
        except ZeroDivisionError:
            print('Вы пытались разделить на ноль! Не надо так')
    else:
        print('Вы ввели не чилсло(а)')

if __name__ == '__main__':
    num = input('Введите числитель')
    den = input('Введите знаменатель')

    division(num, den)