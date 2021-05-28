"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def sum_num():
    an = 0
    while True:
        numbers = input('Введите числа используя пробелы или введите "Z" для выхода: ').split()
        for num in numbers:
            if num.upper() == 'Z':
                return an
            else:
                try:
                    an += int(num)
                except ValueError:
                    print('Нажмите "Z" для выхода')
        print(f'Сумма чисел = {an}')
print(sum_num())
