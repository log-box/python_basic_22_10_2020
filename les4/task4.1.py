"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv

def salary():
    try:

        time_works = float(argv[1])
        salary_per_hour = float(argv[2])
        bonus = float(argv[3])

        salary = round(((time_works * salary_per_hour) + bonus), 2)
        print(f'Зарплата сотрудника равна: {salary}')

    except ValueError:
        print('Вы ввели не число(а)')


if __name__ == '__main__':
    salary()
