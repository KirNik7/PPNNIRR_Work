# Задание 1.3
# Параметрически заданные функции
# Вариант 7
# Функция x:= cos(3t), y:= sin(5t), t:= 0..2pi

import numpy as np
import matplotlib.pyplot as plt


# Определение функции x(t)
def func_x(t):
    return np.cos(3 * t)


# Определение функции y(t)
def func_y(t):
    return np.sin(5 * t)


# Построение графика функции
def plot_func(func_x, func_y, t_min, t_max):
    t = np.linspace(t_min, t_max)
    x = func_x(t)
    y = func_y(t)
    plt.plot(x, y)
    plt.title('График параметрической функции')
    plt.xlabel('Значения t')
    plt.ylabel('Значения функции')
    plt.grid(True)
    plt.show()


# Основная функция программы
if __name__ == '__main__':

    # Построение графика функции
    t_min = 0
    t_max = 2 * np.pi
    plot_func(func_x, func_y, t_min, t_max)
