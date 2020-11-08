"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task5.5_file.txt', 'w') as file:
    try:
        line = input('Введите числа разделенные пробелами\n')
        file.writelines(line)
        numbers = line.split()
        print(sum(map(int,numbers)))
    except ValueError:
        print('Вы ввели не число(а)')

