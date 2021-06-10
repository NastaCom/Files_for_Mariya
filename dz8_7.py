"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self):
        return self.num_1 + self.num_2

    def __mul__(self):
        return self.num_1 * self.num_2


com_num=ComplexNumber(complex(5, 4), complex(3, 6))
print(f'{com_num.num_1}+{com_num.num_2}={com_num.__add__()}')
print(f'{com_num.num_1}*{com_num.num_2}={com_num.__mul__()}')
