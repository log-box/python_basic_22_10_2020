"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, _str):
        self.str = _str

def division(arg1, arg2):
    try:
        if arg2 == 0:
            raise MyError('Вы пытаетесь делить на ноль')
        else:
            res = arg1 / arg2
            return res

    except MyError as err:
        return err

a = division(1,2)
print(a)
b = division(1,0)
print(b)