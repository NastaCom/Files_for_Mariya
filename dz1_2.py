# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

my_time = int(input('Введи время в секундах - '))
hours = (my_time // 3600)
my_time = my_time - (hours * 3600)
minutes = my_time // 60
seconds = my_time % 60
my_time = my_time - seconds
print(f'{hours}:{minutes}:{seconds}')
