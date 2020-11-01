"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1: int, arg2: int, arg3: int):
    if arg1 >= arg3 and arg2 >= arg3:
        print(arg1 + arg2)
        return arg1 + arg2
    elif arg1 > arg2 and arg2 < arg3:
        print(arg1 + arg3)
        return arg1 + arg3
    else:
        print(arg2 + arg3)
        return arg2 + arg3


if __name__ == '__main__':
    arg1 = int(input('Введите число 1'))
    arg2 = int(input('Введите число 2'))
    arg3 = int(input('Введите число 3'))
    my_func(arg1, arg2, arg3)