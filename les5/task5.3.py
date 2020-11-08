"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_file = open('task5.3_file.txt', 'r')

names = []
average = 0
i = 0
for line in my_file:
    worker = line.split()
    if int(worker[1]) < 20000:
        names.append(worker[0])
    average = average + int(worker[1])
    i += 1

print('===Бедолаги===')
for name in names:

    print(name)
print('==============')
print(f'Средняя зарплата равна: {round(average/i,2)}')
