"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

numbers = [random.randint(1,200) for _ in range(random.randint(10,250))]
with open('task5.5_file.txt', 'w') as file:
    numbers = ' '.join(map(str, numbers))
    file.write(numbers)

with open('task5.5_file.txt', 'r') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))



"""try:
        line = input('Введите числа разделенные пробелами\n')
        file.writelines(line)
        numbers = line.split()
        print(sum(map(int,numbers)))
    except ValueError:
        print('Вы ввели не число(а)')
"""
