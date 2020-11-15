"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param


    def __add__(self, second):
        return f'Для пошива пальто и костюма нужно:{self.param / 6.5 + 0.5 + 2 * second.param + 0.3 :.2f} ткани'

    @property
    def consumption(self):

        pass

    @abstractmethod
    def abstract(self):
        return 'pass'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return f'Заглушка для асбтрактного метода {Coat.abstract.__name__} для класса {Coat.__name__}'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        return f'Заглушка для асбтрактного метода {Costume.abstract.__name__} для класса {Costume.__name__}'


coat = Coat(666)
costume = Costume(100)

print(coat.consumption())
print(costume.consumption())
print(coat + costume)
print(coat.abstract())
print(costume.abstract())