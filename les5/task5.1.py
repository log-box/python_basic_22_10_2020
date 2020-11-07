"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open('task5.1_file.txt', 'w')
line = input('Введите текст\n') + '\n'
while line:
    my_file.writelines(line)
    line = input('Введите текст\n') + '\n'
    if line == '\n':
        my_file.close()
        break

