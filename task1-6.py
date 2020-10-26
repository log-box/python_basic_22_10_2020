def timeconvert(timeInSec):
    seconds = timeInSec % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print('{0}:{1}:{2}'.format(hour,minutes,seconds))

def summa(number):
    number = int(number)
    if number > 9:
        print('Нужно было ввести число от 1 до 9')
    else:
        number = str(number)
        num1 = number*2
        num2 = number*3
        print((int(number)) + (int(num1)) + (int(num2)))
def maxnumber(number):
    lastnumber = number % 10
    ostatok = number // 10
    while ostatok > 0:
        if ostatok % 10 > lastnumber:
            lastnumber = ostatok % 10
        ostatok = ostatok // 10
    print(lastnumber)
def finance(take, cost):
    take = float(take)
    cost = float(cost)
    finResult = take - cost
    rentable = None
    if take > cost:
        rentable = finResult / take
    if rentable == None:
        print('Ваша вирма работает в убыток\n Чистый убыток составил: {}'.format(finResult))
    else:
        print('Ваша вирма приносит доход\n Коэфицент рентабельности составил: {}'.format(rentable))
        workersCount = input('Введите численность работников Вашей фирмы')
        workersCount = int(workersCount)
        renuePer = finResult / workersCount
        print('Прибыль фирмы на одного сотрудника составила:\n{}'.format(renuePer))

def sport(distance, targetdistance):
    distance = int(distance)
    targetdistance = int(targetdistance)
    day = 1
    while distance < targetdistance:
        distance = distance + (distance * 0.1)
        day = day + 1
    print('Лыжник достигнет результата в {0}КМ, через {1} дней'.format(targetdistance, day))





string1 = 'Строковая переменная №1'
int1 = 1
print(string1, '\n', int1)

userInput1 = input('Введите строку\n')

print('Ваша строка == {0}'.format(userInput1))

userInput2 = input('Введите число\n')
userInput2 = int(userInput2)
print('Ваше число == {0}'.format(userInput2))

userInput3 = input('Введие время в секундах\n')
userInput3 = int(userInput3)
timeconvert(userInput3)

userInput4 = input('Введие число от 1 до 9\n')
summa(userInput4)

userInput5 = input('Введие любое число\n')
maxnumber(int(userInput5))

userInput6, userInput7 = input('Введите выручку и издержки фирмы через запятую без пробела\n').split(',')
finance(userInput6, userInput7)

userInput8, userInput9 = input('Введите результат первого дня и целевой результат.\nВводите значения через запятую, без пробела').split(',')
sport(userInput8, userInput9)