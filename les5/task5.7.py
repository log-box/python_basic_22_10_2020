"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""


import json

average_count=0
result = {}
averege_profit_dict = {}
average_profit = 0
result_list = []
with open('task5.7_file.txt', 'r') as file:
    for line in file:
        name, own_type, gain, costs = line.split()
        profit = int(gain) - int(costs)
        result[name] = profit
    result_list.append(result)
    for pro in result.values():
        if pro > 0:
            average_profit = average_profit + pro
            average_count += 1
    averege_profit_dict['average_profit'] = (average_profit/average_count)
    print(averege_profit_dict)
    result_list.append(averege_profit_dict)
    print(result_list)

with open("task5.7_file.json", "w") as json_file:
    json.dump(result_list, json_file)


