"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import  ABC, abstractmethod
class Clothes(ABC):
    _total = 0


    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def __add__(self, other):
        return Coat(self.V + other.V)


    @property
    def expense(self):
        return round(self.V / 6.5) + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    def __add__(self, other):
        return Suit(self.H + other.H)


    @property
    def expense(self):
        return round((2 * self.H) + 0.3)


coat = Coat(V=90)
suit = Suit(H=150)
total_expense = coat.expense + suit.expense

print(f'Расход ткани на пальто с учетом размера: {coat.expense}')
print(f'Расход ткани на костюм с учетом роста: {suit.expense}')
print(f'Общий расход ткани: {total_expense}')
