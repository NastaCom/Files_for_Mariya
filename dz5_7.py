"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""


import json

with open('dz5_7.json', 'w', encoding='utf-8') as fjs:
    with open('dz5_7.txt', 'r', encoding='utf-8') as f:

#        firm_dict = {}
        firm_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}

        prof_dict = {}
        prof = 0
        count = 0
        for value in firm_dict.values():
            if int(value) >= 0:
                prof += value
                count += 1
        av_prof = prof / count
        prof_dict['average_profit'] = round(av_prof)
        result = [firm_dict, prof_dict]
        print(result)

    json.dump(result, fjs, indent=3, ensure_ascii=False)
