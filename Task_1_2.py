# Задание 1.2
# Поверхности
# Вариант 7
# Функция z:= x^3 * y + x * y
import numpy as np
import matplotlib.pyplot as plt


# Задание 1.2
# Построение поверхности
def plot_surface(func, x_min, x_max, y_min, y_max):

    # Создание массивов агрументов
    x = np.linspace(x_min, x_max)
    y = np.linspace(y_min, y_max)

    x, y = np.meshgrid(x, y)
    z = func(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    plt.title('График поверхности')
    plt.xlabel('Значение X')
    plt.ylabel('Значение Y')
    plt.show()


# Функция для построения поверхности
def func_surface(x, y):
    return (x**3) * y + x * y


# Основная функция программы
if __name__ == '__main__':

    # Построение поверхности
    x_min = -5
    x_max = 5
    y_min = -5
    y_max = 5
    plot_surface(func_surface, x_min, x_max, y_min, y_max)
