"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""
"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Storage:
    __STORAGE = {
        'Название': 'Склад ОРГТЕХНИКИ',
        'Принтеры': [
                    ],
        'Сканеры': [
                    ],
        'Копиры': [
                ]

    }

class OfficeEquimp:
    def __init__(self):
        self.manufactor = ''
        self.model = ''
        self.serial_number = ''
        self.price = 0
        self.depart = ''
    def adding_to_storage(self):
        try:
            self.manufactor = input(f'Введите производителя ')
            self.model = input(f'Введите модель устройства ')
            self.serial_number  = input(f'Введите серийный номер ')
            self.price = int(input(f'Введите цену '))
            device_parram = {'Производитель': self.manufactor, }


class Printers(OfficeEquimp):
    def __init__(self):
        super().__init__()
        self.manufactor = ''
        self.model = ''
        self.serial_number = ''
        self.price = 0
        self.type = ''

class Scaners(OfficeEquimp):
    def __init__(self):
        super().__init__()
        self.manufactor = ''
        self.model = ''
        self.serial_number = ''
        self.price = 0
        self.dimension = ''

class Copyers(OfficeEquimp):
    def __init__(self):
        super().__init__()
        self.manufactor = ''
        self.model = ''
        self.serial_number = ''
        self.price = 0
        self.color = ''



stor = Storage()

print(stor._Storage__STORAGE)