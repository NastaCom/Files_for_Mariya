# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение
# прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного
# сотрудника.

plus_money = int(input('Введите выручку фирмы - '))
minus_money = int(input('Введите издержку фирмы - '))
renta = plus_money / minus_money
if plus_money > minus_money:
    print('Фирма прибыльная.', 'Рентабельность фирмы:', renta)
    num_people = int(input('Введите численность сотрудников: '))
    people_money = renta / num_people
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: ', people_money)
elif plus_money < minus_money:
    print('Фирма убыточная')
else:
    print('нет прибыли и убытков, но стабильно')
print('финансовый результат фирмы известен')
