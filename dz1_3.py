# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

my_num = int(input('Введите любое число - '))
my_numb = str(my_num)
my_num1 = my_numb * 2
my_num2 = my_numb * 3
my_number = my_num + int(my_num1) + int(my_num2)
print(f'{my_num}+{my_num1}+{my_num2}={my_number}')
