"""
 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""

def user_info(name, surname, year, city, email, telephone):
    year = str(year)
    telephone = str(telephone)
    result = ' '.join([surname, name, year, city, email, telephone])
    print(result)
    return ' '.join([surname, name, year, city, email, telephone])




if __name__ == '__main__':
    name = input('Введите имя')
    surname = input('Введите фамилию')
    year = int(input('Введите Ваш год рождения'))
    city = input('Введите город проживания')
    email = input('Введите Ваш email')
    telephone = input('Введите Ваш номер телефона')

    user_info(name, surname, year, city, email, telephone)