"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""

def my_func(num):
    num.remove(min(num))
    return sum(num)


first_num = int(input('Введите число - '))
second_num = int(input('Введите еще число - '))
third_num = int(input('И еще раз введите число - '))
print(f'Сумма двух наибольших чисел = ', my_func([first_num, second_num, third_num]))
