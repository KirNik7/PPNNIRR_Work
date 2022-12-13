# Задание 5
# Дифференцирование
# Вариант 14
# y = ln(tg((2x+1)/4)); x0 = 10


import numpy as np
import math


# Определение производной функции
def derivative(x):
    return 1 / (math.cos((2*x+1)/4)**2 * math.log(math.cos((2*x+1)/4)))


# Определение первой производной в точке x0
def first_derivative(x0):
    h = 0.01
    return (derivative(x0 + h) - derivative(x0)) / h


# Определение второй производной в точке x0
def second_derivative(x0):
    h = 0.01
    return (first_derivative(x0 + h) - first_derivative(x0)) / h


# Основная функция программы
if __name__ == '__main__':
    x0 = 10
    print('Первая производная в точке x0 = 10: ', first_derivative(x0))
    print('Вторая производная в точке x0 = 10: ', second_derivative(x0))
