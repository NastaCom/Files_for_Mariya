"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_arg(arg1, arg2):
    if arg2 == 0:
        print('На 0 делить нельзя!')
    else:
        return arg1 / arg2


num_arg1 = int(input('Введите делитель - '))
num_arg2 = int(input('Введите делимое - '))
print(my_arg(num_arg1, num_arg2))
