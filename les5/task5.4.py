"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
old_file = open('task5.4_file1.txt', 'r')
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file_list = []

for line in old_file:
    number = line.split(' ', 1)
    new_file_list.append(rus[number[0]] + ' ' + number[1])

new_file = open('task5.4_file2.txt', 'w')
new_file.writelines(new_file_list)
new_file.close()
old_file.close()


