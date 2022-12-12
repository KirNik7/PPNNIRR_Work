# Задание 2.2
# Решение СЛАУ методом Гаусса
# Вариант 14
# СЛАУ:
# A =
# |  16  -7  -3  10   8   6 |
# |   7   7   4  -6   3 -10 |
# |   9   0 -10  -1   3  14 |
# |  -2  -9   3  -2   5   8 |
# |   0   6  -7  10   4   1 |
# | -10   0  -3  -2  -8   0 |
# b =
# |  77 |
# | -97 |
# | -40 |
# |  14 |
# |   7 |
# |  29 |

import numpy as np


# Определение матрицы A
def matrix_A():
    return np.array([[16, -7, -3, 10, 8, 6],
                     [7, 7, 4, -6, 3, -10],
                     [9, 0, -10, -1, 3, 14],
                     [-2, -9, 3, -2, 5, 8],
                     [0, 6, -7, 10, 4, 1],
                     [-10, 0, -3, -2, -8, 0]])


# Определение вектора b
def vector_b():
    return np.array([77, -97, -40, 14, 7, 29])


# Решение СЛАУ методом Гаусса
def gauss(A, b):
    # Прямой ход
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            c = A[j][i] / A[i][i]
            for k in range(len(A)):
                A[j][k] -= c * A[i][k]
            b[j] -= c * b[i]
    print('Матрица, полученная в результате прямого хода:')
    print(A)

    # Обратный ход
    x = np.zeros(len(A))
    for i in range(len(A) - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, len(A)):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


# Основная функция программы
if __name__ == '__main__':
    A = matrix_A()
    b = vector_b()
    print('Матрица A:')
    print(A)
    print('Вектор b:')
    print(b)
    print('Решение СЛАУ методом Гаусса:')
    print(gauss(A, b).reshape(-1, 1))
