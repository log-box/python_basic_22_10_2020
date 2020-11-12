"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': wage, 'Премия': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.surname + ' ' + self.name)
        return self.surname + ' ' + self.name

    def get_total_income(self):
        print(self._income.get('Оклад') + self._income.get('Премия'))
        return self._income.get('Оклад') + self._income.get('Премия')



a = Position('Artem', 'Logvin', 'IT-master', 250000, 50000)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()