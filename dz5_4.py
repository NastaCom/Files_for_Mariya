"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def my_func():
    with open('dz5_4_1.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            yield line


def convert(eng_str):
    rus_dict = {
            'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре',
            'Five': 'Пять',
            'Six': 'Шесть',
            'Seven': 'Семь',
            'Eight': 'Восемь'
}
    for key, val in rus_dict.items():
        if key in eng_str:
            rus_str = eng_str.replace(key, val)
            return rus_str


with open('dz5_4_2.txt', 'w', encoding='utf-8') as f2:
    try:
        for i in my_func():
            f2.write(f'{convert(i)}')
    except FileNotFoundError:
        print('Файл не найден')



#from googletrans import Translator

#with open('dz5_4_2.txt', 'w', encoding='utf-8') as f2:
#    with open('dz5_4_1.txt','r', encoding='utf-8') as f1:
#        text = f1.read()
#    translator = Translator()
#    a = translator.translate(text)
#    print(a)
#*********************************************************************************************************
#Не могу разобраться с данной ошибкой в коде ((( Хотя googletrans добавила в библиотеку, ошибка все же есть
#************************************************************************************************************
#Traceback (most recent call last):
#  File "C:\Users\user\PycharmProjects\osnovy_python\osnovy_python3\dz_5\dz5_4.py", line 18, in <module>
#    a = t.translate(text)
#  File "C:\Users\user\Desktop\Обучение. Подготовка\python\lib\site-packages\googletrans\client.py", line 182, in translate
#    data = self._translate(text, dest, src, kwargs)
#  File "C:\Users\user\Desktop\Обучение. Подготовка\python\lib\site-packages\googletrans\client.py", line 78, in _translate
#    token = self.token_acquirer.do(text)
#  File "C:\Users\user\Desktop\Обучение. Подготовка\python\lib\site-packages\googletrans\gtoken.py", line 194, in do
#    self._update()
#  File "C:\Users\user\Desktop\Обучение. Подготовка\python\lib\site-packages\googletrans\gtoken.py", line 62, in _update
#    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
#AttributeError: 'NoneType' object has no attribute 'group'
