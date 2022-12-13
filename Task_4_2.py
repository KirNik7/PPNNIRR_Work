# Задание 4.2
# Неопределенный интеграл
# Вариант 17
# Интеграл:
# I = int (2*x^2 + x + 3) / ((x+2)(x^2 + x + 1)) dx


import numpy as np
import sympy as sp


# Определение интеграла
def integral():
    x = sp.Symbol('x')
    return sp.integrate((2*x**2 + x + 3) / ((x+2)*(x**2 + x + 1)), x)


# Определение первообразной
def primitive():
    x = sp.Symbol('x')
    return sp.integrate(2*x**2 + x + 3, x) - sp.integrate(x**2 + x + 1, x)


# Основная функция программы
if __name__ == '__main__':
    # Вычисление интеграла
    I = integral()
    print('Значение интеграла: ', I)

    # Вычисление первообразной
    P = primitive()
    print('Значение первообразной: ', P)
