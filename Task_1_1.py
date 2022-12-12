# Задание 1.1
# Функции одной переменной в декартовой системе координат
# Вариант 17
# Функция f(x) = (x+1)/((x**2) + 10)
import numpy as np
import matplotlib.pyplot as plt


# Посторение графика по функции
def plot_func(func, x_min, x_max):
    x = np.linspace(x_min, x_max)
    y = func(x)
    plt.plot(x, y)
    plt.title('График одной функции')
    plt.xlabel('Аргумент функции (x)')
    plt.ylabel('Значение функции (y)')
    plt.grid(True)
    plt.show()


# Функция для построения графика
def func_line(x):
    return (x+1)/((x**2) + 10)


# Диапазон значений функции
def range_func(func, x_min, x_max):
    x = np.linspace(x_min, x_max)
    y = func(x)
    return y.min(), y.max()


# Основная функция программы
if __name__ == '__main__':

    # Построение графика функции
    x_min = -5
    x_max = 5
    plot_func(func_line, x_min, x_max)

    print('Область определения функции: от -inf до +inf')
    print('Все аргументы функции на графике с шагом 1: ', np.arange(x_min, x_max, 1))
    print('Диапазон значений функции: ', range_func(func_line, x_min, x_max))
