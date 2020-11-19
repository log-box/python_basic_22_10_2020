"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


from datetime import date


class Data:

    @staticmethod
    def check_date(stroka: str):
        check = stroka.split('-')
        year, month, day = check
        try:
            date(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    def __init__(self, data: str):
        self.data = data
        self.true_data = ''
        if not isinstance(self.data, str):
            raise TypeError('ОШИБКА: Вы ввели не строку')
        if len(self.data.split('-')) != 3:
            raise ValueError('ОШИБКА: В вашей строке не три разделителя "-"')
        try:
            for __ in self.data.split('-'):
                int(__)
            print('Объект класса успешно создан')
            self.true_data = self.data
        except ValueError:
                print('ОШИБКА: Вы пытаетесь вводить не числовое представление даты')

    @classmethod
    def date_to_int(cls, class_object):
        if isinstance(class_object, cls):
            param = class_object.true_data
            if Data.check_date(param) == True:
                year, month, day = param.split('-')
                return int(year), int(month), int(day)


            else:
                print('Вы ввели дату в не правильном формате\nПравильный формат: year-month-day')
        else:
            raise ValueError('Вы передали в метод не объект класса!')






a = Data('12-12-12')
b = Data('1990-01-30')
print(Data.date_to_int(a))
print(Data.date_to_int(b))


