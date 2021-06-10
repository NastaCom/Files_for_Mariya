"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class DivideError(Exception):
    zero = 'На ноль делить нельзя!'

    def __str__(self):
        return self.zero


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise DivideError

        return Number(float(self) / float(other))


while True:
    try:
        divident, divider = map(Number, input('Введите числитель и знаменатель через пробел: ').split())
        print(divident / divider)
    except DivideError as e:
        print(e)
    except ValueError as e:
        print(e)
        break
