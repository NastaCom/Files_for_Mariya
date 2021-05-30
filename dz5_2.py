"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""


with open('dz5_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print('В тексте', len(lines), 'строки')
for words, line in enumerate(lines, 1):
    print('в {} строке {} слов.'.format(words, len(line.split())))
