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
        'Принтеры': {0: 0,
                     },
        'Сканеры': {0: 0,
                    },
        'Копиры': {0: 0,
                   },
    }

class OfficeEquimp:
    def __init__(self, manufactor: str, model: str, serial_number: str, price: int):
        self.manufactor = manufactor
        self.model = model
        self.serial_number = serial_number
        self.price = price

class Printers(OfficeEquimp):
    def __init__(self, manufactor:str, model: str, serial_number: str, price: int, type: str):
        super().__init__(manufactor, model, serial_number, price)
        self.manufactor = manufactor
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.type = type

class Scaners(OfficeEquimp):
    def __init__(self, manufactor: str, model: str, serial_number: str, price: int, dimension: str):
        super().__init__(manufactor, model, serial_number, price)
        self.manufactor = manufactor
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.dimension = dimension

class Copyers(OfficeEquimp):
    def __init__(self, manufactor: str, model: str, serial_number: str, price: int, color: str):
        super().__init__(manufactor, model, serial_number, price)
        self.manufactor = manufactor
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.color = color



stor = Storage()

print(stor._Storage__STORAGE)