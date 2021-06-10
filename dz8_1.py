"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, data):
        self.data_dmy = data
        try:
            self.d, self.m, self.y = tuple(map(int, data.split('-')))
        except ValueError:
            raise ValueError('Дата введена некорректно. Введите дату в формате дд-мм-гггг')
        self.validator(self.d, self.m, self.y)

    @classmethod
    def method(cls, data):
        res = cls(data)
        return f"День: {res.d:02} Месяц: {res.m:02} Год: {res.y}"

    @staticmethod
    def validator(d, m, y):
        try:
            if d > 31:
                raise ValueError('В месяце меньше дней!')
            elif m > 12:
                raise ValueError('В году 12 месяцев!')
            elif y > 2021:
                raise ValueError('Введите год до 2021')
        except ValueError:
            raise ValueError('Дата введена некорректно!')


my_date = '01-01-1988'
date_obj = Data(my_date)
print(date_obj.method(my_date))
