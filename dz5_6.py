"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


my_dict = {}


with open('dz5_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        elements = [i for i in stats if i == ' ' or '0' <= i <= '9']
        name_sum = sum(map(int, "".join(elements).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')
