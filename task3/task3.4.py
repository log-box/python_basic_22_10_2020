"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
def my_func(x, y):#для любой степени
    count = 1
    for i in range(abs(y)): # Получаем модуль (положительное) степени
        count *= x # уозвоздим в степень в цикле
    if y >= 0:
        return count # если положительная степень
    else:
        return 1 / count # делим если отрицательная степень

def my_func1(x, y): #только для положительной степени
    if y == 0:
        return 1
    return x * my_func(x, y-1) #рекурсивный вызов уможения (возведения в степень) и уменьшения множителя


if __name__ == '__main__':
    x = int(input('Введите число'))
    y = int(input('Введите степень числа'))
    print(my_func(x, y))
