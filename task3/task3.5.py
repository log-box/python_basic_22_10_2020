"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""


def string_sum():
    sum_result = 0
    exit = False
    while exit == False:
        numbers = input('Введите числа или Q для выхода - ').split(' ')
        res = 0
        for i in numbers:
            if i == 'q' or i == 'Q':
                exit = True
                break
            else:
                res = res + int(i)
        sum_result = sum_result + res
        print(f'Текущая сумма равна: {sum_result}')
    print(f'В итоге сумма получиласьтакой: {sum_result}')


if __name__ == '__main__':
    string_sum()