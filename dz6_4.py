"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Автомобиль: {self.name} Цвет: {self.color} Полицейская машина - {self.is_police}')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f"{self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'Черный', 'BMW')
town_car.go()
town_car.show_speed()
town_car.turn(0)
town_car.stop()
