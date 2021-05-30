"""
Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""


# Код работает, но атрибут color не нашла куда влепить ) Попробую 2-ой вариант ниже...
#
# from time import sleep
#
#
# class TrafficLight:
#
#     def running(self):
#         while True:
#             print('Красный')
#             sleep(7)
#             print('Желтый')
#             sleep(2)
#             print('Зеленый')
#             sleep(5)
#             print('Желтый')
#             sleep(2)
#
#
# trafficlight = TrafficLight()
# trafficlight.running()


from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Красный', 7), ('Желтый', 2), ('Зеленый', 5), ('Желтый', 2))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color)
            sleep(sec)


trafficlight = TrafficLight()
trafficlight.running()
