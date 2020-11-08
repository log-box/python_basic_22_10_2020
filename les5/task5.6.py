"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

tasks = {}

with open('task5.6_file.txt', 'r') as file:
    for line in file:
        task, lection, practics, labs = line.split()
        if lection != '—':
            lection = lection.split('(')
        else:
            lection = [0,]
        if practics != '—':
            practics = practics.split('(')
        else:
            practics = [0,]
        if labs != '—':
            labs = labs.split('(')
        else:
            labs = [0,]
        tasks[task] = int(lection[0]) + int(practics[0]) + int(labs[0])
print(tasks)
