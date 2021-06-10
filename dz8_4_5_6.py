"""
Задача 8_4
------------------------------------------------------------------------------------------------------------------
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

Задача 8_5
------------------------------------------------------------------------------------------------------------------
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру (например, словарь).

Задача 8_6
-------------------------------------------------------------------------------------------------------------------
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:
    def __init__(self):
        self.equipment = []

    def accept(self):
        self.equipment.append(dict(printer=Printer.dictionary, scanner=Scanner.dictionary_2, xerox=Xerox.dictionary_3))
        return self.equipment


class OfficeEquipment:
    def __init__(self, brand, price, count):
        self.brand = brand
        self.price = price
        self.count = count


class Printer(OfficeEquipment):
    def __init__(self, color, value, brand, price, count):
        super().__init__(brand, price, count)
        self.color = color
        self.value = value
        self.parameter_1 = []

    def dictionary(self):
        try:
            self.parameter_1.append(dict(color_b=self.color, format_pr=self.value, brands=self.brand,
                                    prices=int(self.price), _count=int(self.count)))
        except ValueError:
            print('Данные для принтера введены некорректно!')
        return self.parameter_1


class Scanner(OfficeEquipment):
    def __init__(self, pixel, brand, price, count):
        super().__init__(brand, price, count)
        self.pixel = pixel
        self.parameter_2 = []

    def dictionary_2(self):
        try:
            self.parameter_2.append(dict(pixels=int(self.pixel), brands=self.brand, prices=int(self.price),
                                         _count=int(self.count)))
        except ValueError:
            print('Данные для сканера введены некорректно!')
        return self.parameter_2


class Xerox(OfficeEquipment):
    def __init__(self, color, brand, price, count):
        super().__init__(brand, price, count)
        self.color = color
        self.parameter_3 = []

    def dictionary_3(self):
        try:
            self.parameter_3.append(dict(color_d=self.color, brands=self.brand, prices=int(self.price),
                                         _count=int(self.count)))
        except ValueError:
            print('Данные для ксерокса введены некорректно!')
        return self.parameter_3


printer = Printer(input('Введите цвет корпуса принтера: '), input('Введите формат печати принтера: '),
                  input('Введите марку принтера: '), input('Введите цену принтера: '),
                  input('Введите количество единиц: '))
scanner = Scanner(input('Введите разрешение сканера: '), input('Введите марку сканера: '),
                  input('Введите цену сканера: '), input('Введите количество единиц: '))
xerox = Xerox(input('Введите цвет чернил ксерокса: '), input('Введите марку ксерокса: '),
              input('Введите цену ксерокса: '), input('Введите количество единиц: '))
store = Warehouse()
print(store.accept())
print(printer.dictionary())
print(scanner.dictionary_2())
print(xerox.dictionary_3())
