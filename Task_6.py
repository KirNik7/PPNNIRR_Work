# Задание 6
# Сплайн-интерполяция
# Вариант 17
# x = [0.0721, 2.895, 8.595, 7.075, 9.21, 0.9356, 0.767, 3.839, 5.151, 1.407]
# y = [3.761, 0.2024, 1.107, 3.721, 0.7304, 2.847, 3.11, 1.004, 3.565, 2.001]

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# График с исходными точками, с линейным сплайном, с параболическим сплайном, с кубическим сплайном
def plot_spline(x, y, x_min, x_max):
    # Линейный сплайн
    f_linear = interp1d(x, y, kind='linear')
    # Параболический сплайн
    f_quadratic = interp1d(x, y, kind='quadratic')
    # Кубический сплайн
    f_cubic = interp1d(x, y, kind='cubic')
    # Создание массива аргументов
    x_new = np.linspace(x_min, x_max)
    # Построение графика
    plt.plot(x, y, 'o', x_new, f_linear(x_new), '-', x_new, f_quadratic(x_new), '--', x_new, f_cubic(x_new), ':')
    plt.legend(['Исходные точки', 'Линейный сплайн', 'Параболический сплайн', 'Кубический сплайн'], loc='best')
    plt.title('График сплайна')
    plt.xlabel('Значения x')
    plt.ylabel('Значения функции')
    plt.grid(True)
    plt.show()


# Основная функция программы
if __name__ == '__main__':
    # Исходные данные
    x = [0.0721, 2.895, 8.595, 7.075, 9.21, 0.9356, 0.767, 3.839, 5.151, 1.407]
    y = [3.761, 0.2024, 1.107, 3.721, 0.7304, 2.847, 3.11, 1.004, 3.565, 2.001]
    x_min = min(x)
    x_max = max(x)
    # Построение графика
    plot_spline(x, y, x_min, x_max)
