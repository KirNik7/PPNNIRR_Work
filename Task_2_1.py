# Задание 2.1
# Решение СЛАУ методом Крамера
# Вариант 17
# СЛАУ:
# A =
# | -7  5  2 -5 |
# |  5  6  2 -6 |
# |  1  0 -1  3 |
# | -1  6  3  4 |
# b =
# | -49 |
# |  -6 |
# |   2 |
# | -28 |

import numpy as np


# Определение матрицы A
def matrix_A():
    return np.array([[-7, 5, 2, -5],
                     [5, 6, 2, -6],
                     [1, 0, -1, 3],
                     [-1, 6, 3, 4]])


# Определение вектора b
def vector_b():
    return np.array([-49, -6, 2, -28])


# Определение определителя матрицы A
def det_A(A):
    return round(np.linalg.det(A))


# Определение определителя матрицы A1
def det_A1_def(A, b):
    A1 = A.copy()
    A1[:, 0] = b
    return round(np.linalg.det(A1))


# Определение определителя матрицы A2
def det_A2_def(A, b):
    A2 = A.copy()
    A2[:, 1] = b
    return round(np.linalg.det(A2))


# Определение определителя матрицы A3
def det_A3_def(A, b):
    A3 = A.copy()
    A3[:, 2] = b
    return round(np.linalg.det(A3))


# Определение определителя матрицы A4
def det_A4_def(A, b):
    A4 = A.copy()
    A4[:, 3] = b
    return round(np.linalg.det(A4))


# Определение решения СЛАУ методом Крамера
def solve_cramer(A, b):
    det_A = np.linalg.det(A)
    det_A1 = det_A1_def(A, b)
    det_A2 = det_A2_def(A, b)
    det_A3 = det_A3_def(A, b)
    det_A4 = det_A4_def(A, b)
    x1 = det_A1 / det_A
    x2 = det_A2 / det_A
    x3 = det_A3 / det_A
    x4 = det_A4 / det_A
    return np.array([x1, x2, x3, x4]).reshape(-1, 1)


# Основная функция программы
if __name__ == '__main__':
    A = matrix_A()
    b = vector_b()
    print('Матрица A:')
    print(A)
    print('Вектор b:')
    print(b.reshape(-1, 1))
    print('Решение СЛАУ методом Крамера:')
    print(solve_cramer(A, b))
