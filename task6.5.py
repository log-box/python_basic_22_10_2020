"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title='Пальцем'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title='Пальцем'):
        super().__init__(title)
        self.title = Pen.__name__

    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}')

class Pencil(Stationery):
    def __init__(self, title='Пальцем'):
        super().__init__(title)
        self.title = Pencil.__name__
    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}')

class Handle(Stationery):
    def __init__(self, title='Пальцем'):
        super().__init__(title)
        self.title = Handle.__name__
    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}')

x=Stationery()
x.draw()
a=Pen()
a.draw()
b=Pencil()
b.draw()
c=Handle()
c.draw()