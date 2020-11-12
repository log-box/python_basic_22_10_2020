"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'{self.name} Поехал')
        #return f'{self.name} Поехал'

    def stop(self):
        print(f'{self.name} Остановился')
        #return f'{self.name} Остановился'

    def turn(self, direction):
        print(f'{self.name} Поменял направление на {direction}')
        #return f'{self.name} Поменял направление на {direction}'

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} КМ/Ч')
        #return f'{self.name} едет со скоростью {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} КМ/Ч')
        #return f'{self.name} едет со скоростью {self.speed}'
        if self.speed > 60:
            print(f'{self.name} едет c превышением скорости!!!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name, ):
        super().__init__(speed, color, name)
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} КМ/Ч')
        #return f'{self.name} едет со скоростью {self.speed}'
        if self.speed > 40:
            print(f'{self.name} едет c превышением скорости!!!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


a = Car(100, 'Красный', 'Чувак')
a.go()
a.stop()
a.turn('На запад')
a.show_speed()

b = TownCar(120, 'Синий','Агент Смитт')
b.show_speed()
с = PoliceCar(120, 'ченый воронок','Дядя Стёпа')
с.show_speed()