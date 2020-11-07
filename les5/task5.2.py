"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('task5.2_file.txt', 'r')
content = my_file.readlines()
my_file.close()
print(f'Количество строк в файле {len(content)}')
my_file = open('task5.2_file.txt', 'r')

x = 1
for line in my_file:
    print(f'Количеыство слов в строке №{x} равно: {len(line.split())}')
    x += 1
my_file.close()
