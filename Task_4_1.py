# Задание 4.1
# Определенный интеграл
# Вариант 14
# Интеграл:
# I = int_1^2 e**x dx


import numpy as np
import matplotlib.pyplot as plt


# Построение графика подынтегральной функции на интервале интегрирования
def plot_func(func, x_min, x_max):
    x = np.linspace(x_min, x_max)
    y = func(x)
    plt.plot(x, y)
    plt.title('График подынтегральной функции')
    plt.xlabel('Аргумент функции (x)')
    plt.ylabel('Значение функции (y)')
    plt.grid(True)
    plt.show()


# Подынтегральная функция
def func_line(x):
    return np.exp(x)


# Основная функция программы
if __name__ == '__main__':

    # Вычисление интеграла
    I = np.exp(2) - np.exp(1)
    print('Значение интеграла: ', I)

    # Построение графика функции
    x_min = 1
    x_max = 2
    plot_func(func_line, x_min, x_max)
